# 10 – Memory Management in Python

## 1. Python Memory Model

Python manages memory through a **private heap**. All Python objects live on this heap;
the programmer never allocates or frees memory directly.

```
Source code
    │
    ▼
Variables (names) ──►  References (pointers)  ──►  Objects on the heap
```

When you write `x = 42`, Python:
1. Creates an `int` object with value `42` somewhere on the heap.
2. Binds the *name* `x` to that object (stores a reference).

The variable is not the object – it is just a label pointing at the object.

---

## 2. Garbage Collection

Python uses two complementary strategies:

### 2a. Reference Counting (primary)
Every object keeps an internal counter of how many references point to it.
- Reference created → counter +1
- Reference destroyed (variable deleted / reassigned / goes out of scope) → counter -1
- Counter hits **0** → object is immediately deallocated.

```python
import sys
x = []
print(sys.getrefcount(x))   # at least 2 (x + the getrefcount argument)
y = x                        # now 3 (x, y, argument)
del y                        # back to 2
```

### 2b. Cyclic Garbage Collector (secondary)
Reference counting cannot handle **cycles** (A → B → A). Python's `gc` module runs
periodically to find and break such cycles. You can interact with it via `import gc`.

---

## 3. `id()` and Object Identity

`id(obj)` returns the **memory address** of the object (an integer, unique for the
lifetime of the object). Two objects live at the same address only if one has been
deallocated before the other was created.

```python
x = 1000
y = 1000
print(id(x), id(y))       # may differ (two separate objects)
print(id(x) == id(y))     # often False for large ints
```

---

## 4. `is` vs `==`

| Operator | Checks               | Uses           |
|----------|----------------------|----------------|
| `is`     | Identity (same object)| `id(a) == id(b)` |
| `==`     | Equality (same value) | `__eq__` method  |

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  – same value
print(a is b)   # False – different objects

c = a
print(a is c)   # True  – same object
```

**Rule:** use `is` only for `None`, `True`, `False` comparisons (singletons). Use `==`
for value comparisons.

---

## 5. Mutable vs Immutable Types

| Immutable                        | Mutable                        |
|----------------------------------|-------------------------------|
| `int`, `float`, `complex`        | `list`                        |
| `bool`, `str`                    | `dict`                        |
| `tuple`                          | `set`                         |
| `frozenset`                      | `bytearray`                   |
| `bytes`                          | User-defined classes (usually)|

**Immutable** objects cannot be changed in place – operations create new objects.
**Mutable** objects can be modified without creating a new object.

```python
s = "hello"
id_before = id(s)
s += " world"            # creates a NEW string object
print(id(s) == id_before)  # False

lst = [1, 2]
id_before = id(lst)
lst.append(3)            # modifies IN PLACE
print(id(lst) == id_before)  # True
```

---

## 6. Small Integer Caching and String Interning

CPython caches small integers in the range **[-5, 256]** and interns many short strings
at startup. Objects in this cache are singletons:

```python
a = 100; b = 100
print(a is b)    # True  – cached
a = 300; b = 300
print(a is b)    # False – NOT cached (implementation detail, may vary)
```

String interning: identifiers and small string literals are often interned automatically.
Force interning with `sys.intern(s)`.

> **Important:** never rely on caching behaviour in production code. It is an
> implementation detail of CPython and may differ in PyPy, Jython, etc.

---

## 7. Variable Assignment (Binding to Objects)

Assignment (`=`) never *copies* an object – it creates a new **binding** (reference) to
the same object.

```python
x = [1, 2, 3]
y = x          # y and x point at the SAME list
y.append(4)
print(x)       # [1, 2, 3, 4]  – x "sees" the change because they share the object
```

Augmented assignment (`+=`, `-=`, etc.) behaves differently for mutables vs immutables:
- Immutable: `x += 1` creates a new object and rebinds `x`.
- Mutable: `lst += [4]` extends the list **in place** (calls `__iadd__`).

---

## 8. Shallow Copy vs Deep Copy

The `copy` module provides two copy strategies:

| Function          | What it copies                                      |
|-------------------|-----------------------------------------------------|
| `copy.copy(obj)`  | Shallow – new container, same inner object refs     |
| `copy.deepcopy(obj)` | Deep – recursively copies everything            |

```python
import copy
original = [[1, 2], [3, 4]]
shallow  = copy.copy(original)
deep     = copy.deepcopy(original)

original[0].append(99)
print(shallow[0])  # [1, 2, 99]  – shared inner list
print(deep[0])     # [1, 2]      – independent copy
```

List slicing `lst[:]` and `list(lst)` also produce shallow copies.

---

## 9. Reference Counting with `sys.getrefcount()`

```python
import sys
x = object()
print(sys.getrefcount(x))   # 2: one for x, one for the getrefcount argument
y = x
print(sys.getrefcount(x))   # 3
del y
print(sys.getrefcount(x))   # 2
```

The count is always **at least 1** when passed to `getrefcount` because the function
call itself creates a temporary reference.

---

## 10. Memory Leaks and How to Avoid Them

Python's GC handles most cleanup, but leaks can still occur:

1. **Global variables accumulating data** – avoid growing globals indefinitely.
2. **Circular references with `__del__`** – before Python 3.4, objects with `__del__`
   that formed cycles were not collected. Fixed in Python 3.4+.
3. **Unclosed resources** – file handles, socket connections, database cursors not
   released. Always use `with` statements.
4. **Caches without eviction** – unbounded caches (`dict`, `list`) that grow forever.
   Use `functools.lru_cache` with a `maxsize`, or `weakref.WeakValueDictionary`.

---

## 11. The `del` Statement

`del x` removes the **name binding**, not necessarily the object itself. The object is
only deallocated when its reference count drops to zero.

```python
x = [1, 2, 3]
y = x
del x            # removes name 'x'; object still alive because 'y' holds a reference
print(y)         # [1, 2, 3]
del y            # now ref count hits 0 → object is freed
```

---

## 12. `__del__` Method

Called by the garbage collector just before reclaiming the object. **Avoid** relying on
it for critical cleanup (timing is non-deterministic; exceptions inside `__del__` are
silently ignored). Prefer context managers (`__enter__` / `__exit__`).

---

## 13. Memory Optimisation Tips

1. **`__slots__`** – eliminates per-instance `__dict__`, saving ~50–70 bytes per object:
   ```python
   class Point:
       __slots__ = ("x", "y")
       def __init__(self, x, y): self.x, self.y = x, y
   ```
2. **Generators instead of lists** – `(x*2 for x in range(10**6))` uses O(1) memory.
3. **`array` module** for homogeneous numeric data (more compact than `list`).
4. **`sys.getsizeof(obj)`** – inspect memory usage of an object.
5. **`weakref` module** – weak references do not increment ref count; useful for caches.

---

## 14. Common Mistakes

1. **Using `is` for value comparison**
   ```python
   # WRONG
   if x is "hello":   # may or may not be True due to interning
   # CORRECT
   if x == "hello":
   ```

2. **Expecting `del` to free memory immediately** – it only removes the name. The GC
   decides when to free.

3. **List aliasing bug**
   ```python
   matrix = [[0] * 3] * 3   # WRONG – all rows are the SAME object
   matrix[0][0] = 1
   print(matrix)              # [[1,0,0],[1,0,0],[1,0,0]]
   ```

4. **Assuming shallow copy is always safe** – if inner objects are mutable and shared,
   mutations propagate across the original and the copy.

5. **Circular imports holding references** – can prevent cleanup in large applications.
