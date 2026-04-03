# 08 – Arrays & Collections: Key Points

## Collection Types at a Glance

| Type | Ordered | Mutable | Duplicates | Hashable | Literal Syntax |
|---|---|---|---|---|---|
| `list` | ✓ | ✓ | ✓ | ✗ | `[1, 2, 3]` |
| `tuple` | ✓ | ✗ | ✓ | ✓ (if all items hashable) | `(1, 2, 3)` |
| `set` | ✗ | ✓ | ✗ | ✗ | `{1, 2, 3}` |
| `frozenset` | ✗ | ✗ | ✗ | ✓ | `frozenset([1,2,3])` |
| `dict` | ✓ (py3.7+) | ✓ | keys: ✗ / values: ✓ | ✗ | `{"k": "v"}` |

## List Methods Quick Reference

```python
lst.append(x)        # add to end
lst.extend(iterable) # add all from iterable
lst.insert(i, x)     # insert before index i
lst.remove(x)        # remove first occurrence (ValueError if absent)
lst.pop(i=-1)        # remove and return item at i (default: last)
lst.sort(key, reverse)   # in-place sort
lst.reverse()        # in-place reverse
lst.index(x)         # index of first x (ValueError if absent)
lst.count(x)         # occurrences of x
lst.copy()           # shallow copy
lst.clear()          # remove all

sorted(lst)          # returns NEW sorted list (original unchanged)
```

## Slicing

```
lst[start : stop : step]   (stop is exclusive)

lst[:3]      first 3          lst[-3:]     last 3
lst[1:-1]    all but ends     lst[::-1]    reversed copy
lst[::2]     every other
```

## Set Operations

```python
a | b   # union            a.union(b)
a & b   # intersection     a.intersection(b)
a - b   # difference       a.difference(b)       (in a, not b)
a ^ b   # symmetric diff   a.symmetric_difference(b)
a <= b  # subset           a.issubset(b)
a >= b  # superset         a.issuperset(b)

s.add(x)       # add element
s.discard(x)   # remove (no error if absent)
s.remove(x)    # remove (ValueError if absent)
```

## Dict Methods Quick Reference

```python
d[key]                # read (KeyError if missing)
d.get(key, default)   # safe read
d[key] = val          # create or update
del d[key]            # delete (KeyError if missing)
d.pop(key, default)   # delete and return (safe with default)
d.keys()              # view of keys
d.values()            # view of values
d.items()             # view of (key, value) pairs
d.update(other)       # merge other into d
d.setdefault(k, v)    # set k=v only if k not present
d | other             # merge, returns new dict (Python 3.9+)
```

## Comprehension Syntax

```python
# List
[expr for x in iterable if condition]

# Dict
{key_expr: val_expr for x in iterable if condition}

# Set
{expr for x in iterable if condition}

# Generator (not a comprehension but same syntax)
(expr for x in iterable if condition)
```

## When to Use Which

| Scenario | Best Choice |
|---|---|
| Ordered collection, items change | `list` |
| Multiple return values from a function | `tuple` |
| Lookup table / mapping | `dict` |
| Membership testing, deduplication | `set` |
| Immutable record with named fields | `namedtuple` or `dataclass` |
| Counting occurrences | `collections.Counter` |
| Default dict values | `collections.defaultdict` |

## Performance at a Glance

| Operation | list | set | dict |
|---|---|---|---|
| `x in c` | O(n) | **O(1)** | **O(1)** keys |
| append / add | O(1)* | O(1)* | O(1)* |
| insert at front | O(n) | — | — |
| delete by value | O(n) | O(1) | O(1) |

`*` = amortised

## Common Pitfalls

- `{}` is an **empty dict**, not a set — use `set()` for empty set.
- `b = a` (list) copies the reference — use `b = a.copy()` or `b = a[:]`.
- Never modify a list while iterating over it — iterate over `lst[:]` copy.
- Unhashable types (`list`, `dict`, `set`) cannot be dict keys or set members — use `tuple` or `frozenset`.
