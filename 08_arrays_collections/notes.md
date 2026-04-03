# 08 – Arrays & Collections

## Overview

Python provides four built-in collection types that cover almost every data-organisation need: **lists**, **tuples**, **sets**, and **dictionaries**. Choosing the right one for the job is a key skill — each has distinct performance characteristics and semantic meaning.

---

## Lists

A **list** is an ordered, mutable sequence of any objects.

```python
fruits = ["apple", "banana", "cherry"]
mixed  = [1, "two", 3.0, True, None]
empty  = []
nested = [[1, 2], [3, 4], [5, 6]]
```

### Indexing and Slicing

Lists use the same `[start:stop:step]` slice syntax as strings.

```python
fruits[0]       # "apple"
fruits[-1]      # "cherry"
fruits[1:3]     # ["banana", "cherry"]
fruits[::-1]    # reversed copy
```

### Core List Methods

| Method | Description |
|---|---|
| `.append(x)` | Add x to the end |
| `.extend(iterable)` | Add all items of iterable to end |
| `.insert(i, x)` | Insert x before index i |
| `.remove(x)` | Remove first occurrence of x (ValueError if absent) |
| `.pop(i=-1)` | Remove and return item at index i (default: last) |
| `.sort(key=None, reverse=False)` | In-place sort |
| `.reverse()` | In-place reverse |
| `.index(x)` | Index of first occurrence of x |
| `.count(x)` | Number of occurrences of x |
| `.copy()` | Shallow copy |
| `.clear()` | Remove all items |

`sorted(lst)` returns a **new** sorted list; `lst.sort()` sorts **in place**.

### Mutability Note

Lists are mutable: items can be added, removed, or changed after creation. Assigning `b = a` makes both variables point to the **same** list — use `b = a.copy()` or `b = a[:]` for a shallow copy.

---

## Tuples

A **tuple** is an ordered, **immutable** sequence. Use them for data that should not change.

```python
point  = (3, 4)
rgb    = (255, 128, 0)
single = (42,)    # comma is required for single-element tuple
empty  = ()
```

- Faster than lists for iteration and access.
- Can be used as dictionary keys (because they are hashable).
- Tuple unpacking: `x, y = point`

### Named Tuples

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
p.x, p.y   # access by name AND by index
```

---

## Sets

A **set** is an unordered collection of **unique**, hashable objects.

```python
primes = {2, 3, 5, 7, 11}
empty_set = set()   # NOT {} — that creates an empty dict
```

### Set Operations

| Operation | Syntax | Operator |
|---|---|---|
| Union | `a.union(b)` | `a \| b` |
| Intersection | `a.intersection(b)` | `a & b` |
| Difference | `a.difference(b)` | `a - b` |
| Symmetric difference | `a.symmetric_difference(b)` | `a ^ b` |
| Subset test | `a.issubset(b)` | `a <= b` |
| Superset test | `a.issuperset(b)` | `a >= b` |

Membership test `x in s` is O(1) for sets vs O(n) for lists — prefer sets for large lookups.

### frozenset

An immutable set; can be used as a dictionary key.

```python
fs = frozenset([1, 2, 3])
```

---

## Dictionaries

A **dict** maps unique, hashable keys to values. As of Python 3.7+, insertion order is preserved.

```python
student = {"name": "Alice", "age": 21, "gpa": 3.8}
empty_dict = {}
from_keys = dict.fromkeys(["a", "b", "c"], 0)
```

### CRUD Operations

```python
student["major"] = "CS"       # Create / Update
student["name"]               # Read → "Alice"
student.get("phone", "N/A")   # Read with default if key missing
del student["age"]            # Delete
student.pop("gpa", None)      # Delete and return (safe: no KeyError)
```

### Core Dict Methods

| Method | Description |
|---|---|
| `.keys()` | View of all keys |
| `.values()` | View of all values |
| `.items()` | View of all (key, value) pairs |
| `.get(k, default)` | Value or default if key absent |
| `.update(other)` | Merge another dict (in place) |
| `.pop(k, default)` | Remove key and return value |
| `.setdefault(k, v)` | Return value for k; set k=v if absent |
| `.copy()` | Shallow copy |
| `.clear()` | Remove all items |

---

## Comprehensions

Comprehensions are concise, readable ways to create collections.

### List Comprehension

```python
[expression for item in iterable if condition]

squares   = [x**2 for x in range(10)]
even_sq   = [x**2 for x in range(10) if x % 2 == 0]
flattened = [n for row in matrix for n in row]
```

### Dict Comprehension

```python
{key_expr: value_expr for item in iterable if condition}

word_lengths = {w: len(w) for w in words}
inverted     = {v: k for k, v in my_dict.items()}
```

### Set Comprehension

```python
{expression for item in iterable if condition}

unique_lengths = {len(w) for w in words}
```

Note: there is no **tuple comprehension** — `(x for x in ...)` creates a **generator**.

---

## Nested Data Structures

```python
students = [
    {"name": "Alice", "scores": [90, 85, 92]},
    {"name": "Bob",   "scores": [70, 75, 68]},
]

# Access nested data
students[0]["name"]          # "Alice"
students[0]["scores"][2]     # 92

# Build with comprehension
averages = {s["name"]: sum(s["scores"]) / len(s["scores"]) for s in students}
```

---

## Choosing the Right Collection

| Need | Use |
|---|---|
| Ordered, mutable, allows duplicates | **list** |
| Ordered, immutable, hashable | **tuple** |
| Fast membership test, no duplicates | **set** |
| Key → value mapping | **dict** |
| Immutable set (dict key, element of set) | **frozenset** |
| Named fields, lightweight | `namedtuple` or `dataclass` |

---

## Performance Considerations

| Operation | list | set | dict |
|---|---|---|---|
| `x in collection` | O(n) | O(1) | O(1) for keys |
| `append` / `add` | O(1) amortised | O(1) amortised | O(1) amortised |
| `insert(0, x)` | O(n) | — | — |
| `remove(x)` | O(n) | O(1) | O(1) |
| `sort` | O(n log n) | — | — |

For large membership tests, convert a list to a set first.

---

## Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| `empty_set = {}` | Creates empty dict, not set | `empty_set = set()` |
| `b = a` (list copy) | Both point to the same list | `b = a.copy()` or `b = a[:]` |
| Modifying a list while iterating | Skips elements or IndexError | Iterate over a copy: `for x in lst[:]` |
| `dict[missing_key]` | KeyError | Use `.get(key, default)` |
| Unhashable list as dict key | TypeError | Use a tuple instead |
| `list.sort()` on non-comparable types | TypeError | Provide a `key=` function |

---

## Summary

- **list**: general-purpose ordered collection; use when order and mutability matter.
- **tuple**: immutable sequences; great for multi-value returns and as dict keys.
- **set**: fast deduplication and membership tests; unordered.
- **dict**: key → value mapping; the workhorse for structured data.
- Comprehensions are idiomatic Python — prefer them over `for`-loop appends.
- Membership tests are O(1) in sets/dicts vs O(n) in lists — choose wisely.
