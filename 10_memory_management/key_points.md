# 10 – Memory Management Key Points (Quick Reference)

## The Golden Rule

> A variable is a **name** (label) bound to an **object** on the heap.
> Assignment (`=`) creates a binding; it never copies an object.

---

## Identity vs Equality

| Operator | Checks         | Example                  |
|----------|----------------|--------------------------|
| `is`     | Same object    | `x is None`              |
| `is not` | Different obj  | `x is not None`          |
| `==`     | Equal value    | `x == y`                 |
| `!=`     | Unequal value  | `x != y`                 |

**Use `is` only for singletons: `None`, `True`, `False`.**

---

## Mutability Quick Table

| Immutable                              | Mutable                        |
|----------------------------------------|-------------------------------|
| `int`, `float`, `complex`, `bool`      | `list`, `dict`, `set`         |
| `str`, `bytes`                         | `bytearray`                   |
| `tuple`, `frozenset`                   | most user-defined classes     |

---

## Copy Methods Compared

| Method                 | Container copied? | Inner objects copied? | Use when                                |
|------------------------|-------------------|-----------------------|-----------------------------------------|
| Assignment `y = x`     | ❌                | ❌                    | You want a shared reference             |
| `lst[:]` / `list(lst)` | ✅                | ❌ (shallow)          | Simple list, no nested mutables         |
| `copy.copy(obj)`       | ✅                | ❌ (shallow)          | General shallow copy                    |
| `copy.deepcopy(obj)`   | ✅                | ✅ (recursive)        | Nested structures that must be independent |

---

## Reference Counting Cheatsheet

```python
import sys
x = object()
sys.getrefcount(x)   # always ≥ 2 (x itself + the call argument)
```

- Reference count **increases** when: assigned to name, passed as argument, appended to container.
- Reference count **decreases** when: `del name`, name rebound, function returns, container shrinks.
- Hits **0** → object freed immediately.

---

## Small Integer Cache (CPython)

- Integers **-5 to 256** are cached singletons.
- Many short string literals are interned (implementation detail).
- Never rely on `is` for comparing integers outside this range.

---

## Memory Optimisation Tools

| Tool / Technique          | Benefit                              |
|---------------------------|--------------------------------------|
| `__slots__`               | No per-instance `__dict__`; saves ~50–70 bytes/obj |
| Generators                | O(1) memory vs O(n) for lists        |
| `sys.getsizeof(obj)`      | Inspect object size (shallow)        |
| `weakref.ref(obj)`        | Reference without preventing GC      |
| `functools.lru_cache`     | Bounded cache with eviction          |
| `gc` module               | Inspect/control cyclic GC            |

---

## Common Pitfalls Checklist

- [ ] `is` used for value comparison instead of `==`
- [ ] `[[0]*n]*m` – all rows are the same list object
- [ ] Shallow copy assumed safe when inner objects are mutable
- [ ] `del x` expected to immediately free memory
- [ ] Unclosed file/socket/DB connection (use `with`)
- [ ] Unbounded cache / growing global list causing memory leak
- [ ] `__del__` used for critical cleanup instead of context manager
