# Key Points — Topic 02: Data Types and Variables

Quick-reference cheat sheet. Review this before your exam.

---

## The Five Primitive Types

| Type | Example | Notes |
|------|---------|-------|
| `int` | `42`, `-7`, `0xFF` | Unlimited precision; no overflow |
| `float` | `3.14`, `1.5e-10` | IEEE 754 double; ~15 significant digits |
| `str` | `"hi"`, `'hi'`, `"""multi"""` | Immutable Unicode sequence |
| `bool` | `True`, `False` | Subclass of `int`; True==1, False==0 |
| `NoneType` | `None` | Singleton; use `is`/`is not` to compare |

---

## Type Casting Quick Reference

```python
int("42")        # 42       (str → int; raises ValueError if not numeric)
int(3.9)         # 3        (truncates — does NOT round)
int(True)        # 1
float("3.14")    # 3.14
float(7)         # 7.0
str(42)          # "42"     (works on any object)
bool(0)          # False
bool([])         # False    (empty container)
bool("0")        # True     (non-empty string — even "False" is True!)
```

---

## Falsy Values (everything else is truthy)

```
0    0.0    0j    ""    []    ()    {}    set()    None    False
```

---

## Scope — LEGB Rule

```
L → E → G → B
│    │   │   └─ Built-in  (len, print, range, …)
│    │   └───── Global    (module-level variables)
│    └───────── Enclosing (outer function for nested functions)
└────────────── Local     (inside current function)
```

### Keywords for Non-Local Assignment

```python
# Modify a global from inside a function
global my_var

# Modify an enclosing variable from an inner function
nonlocal my_var
```

Reading a global is free (no declaration needed). Writing requires `global`.

---

## Mutability

| Immutable (can't change in place) | Mutable (can change in place) |
|-----------------------------------|-------------------------------|
| `int`, `float`, `bool`, `str` | `list`, `dict`, `set` |
| `tuple`, `frozenset`, `bytes` | `bytearray` |

```python
# Mutable pitfall — two names, one object
a = [1, 2, 3]
b = a           # b and a point to the SAME list
b.append(4)
print(a)        # [1, 2, 3, 4] — a changed too!

# Fix: copy explicitly
b = a.copy()    # or list(a) or a[:]
```

---

## None Comparisons

```python
# CORRECT
if x is None:     ...
if x is not None: ...

# AVOID (works but not idiomatic)
if x == None:     ...
```

---

## Float Precision

```python
# WRONG
0.1 + 0.2 == 0.3          # False

# CORRECT
import math
math.isclose(0.1 + 0.2, 0.3)         # True
abs((0.1 + 0.2) - 0.3) < 1e-9       # True
```

---

## Common Pitfalls

```python
# 1. int() truncates, not rounds
int(3.9)   # 3, not 4 — use round(3.9) for 4

# 2. Mutable default argument — classic bug
def bad(lst=[]):     # same list reused across calls!
    lst.append(1)
    return lst

def good(lst=None):  # correct pattern
    if lst is None:
        lst = []
    lst.append(1)
    return lst

# 3. input() always returns str
age = input("Age: ")   # "21" — a string!
age = int(input("Age: "))  # 21  — an integer

# 4. bool is a subclass of int
True + True    # 2 — can be surprising
sum([True, False, True, True])  # 3 — useful for counting

# 5. "False" is truthy (non-empty string)
bool("False")  # True — the string "False" is not the value False
```

---

## `id()` and `is`

```python
id(x)      # unique memory address of object x
x is y     # True if x and y are the SAME object (same id)
x == y     # True if x and y have the SAME VALUE

# Small int interning (CPython caches -5 to 256)
a = 256; b = 256; a is b   # True  (cached)
a = 257; b = 257; a is b   # False (not cached — don't rely on this)
```

---

## Tips

- Use `isinstance(x, (int, float))` to check multiple types at once
- `type(x).__name__` returns just `'int'`, `'str'` etc. as a string
- `x is None` is faster than `x == None` (single identity check vs. `__eq__` call)
- Use `f"{val!r}"` in f-strings to get the `repr()` form (shows quotes for strings)
