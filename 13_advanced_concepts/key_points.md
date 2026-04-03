# Topic 13: Advanced Concepts – Key Points Quick Reference

## Generator Syntax

```python
# Generator function
def gen_func():
    yield value

# Generator expression
gen = (expr for item in iterable if condition)

# Consuming a generator
for val in gen_func(): ...
list(gen_func())
next(gen_object)            # raises StopIteration when exhausted

# Infinite generator + islice
from itertools import islice
list(islice(infinite_gen(), n))
```

---

## Iterator Protocol

```python
class MyIterator:
    def __iter__(self):
        return self              # required – returns iterator

    def __next__(self):
        if done:
            raise StopIteration
        return next_value

# Built-in functions
it = iter(iterable)            # calls __iter__
val = next(it)                 # calls __next__
val = next(it, default)        # default returned instead of StopIteration
```

---

## Context Manager Syntax

```python
# Using a context manager
with expression as var:
    ...

# Class-based
class CM:
    def __enter__(self):
        return resource         # bound to `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
        return False            # True = suppress exception

# Function-based (contextlib)
from contextlib import contextmanager

@contextmanager
def cm():
    # setup
    yield resource              # value for `as` variable
    # teardown (put in finally: for exception safety)
```

---

## Closures and nonlocal

```python
def outer():
    x = 10
    def inner():
        nonlocal x             # needed to rebind x
        x += 1
        return x
    return inner
```

---

## Functional Tools

```python
from functools import reduce, partial

map(func, iterable)            # lazy – apply func to every element
filter(func, iterable)         # lazy – keep elements where func is True
reduce(func, iterable[, init]) # fold: (((a op b) op c) op d) ...

zip(a, b, ...)                 # pair up iterables
enumerate(iterable, start=0)   # yields (index, value)
sorted(iterable, key=func, reverse=False)

partial(func, *args, **kwargs) # pre-fill arguments
```

---

## Common Gotchas

| Mistake | Fix |
|---|---|
| Reusing exhausted generator | Create a new generator object |
| Late-binding lambda in loop | Use `lambda x, i=i: ...` default arg |
| `x += 1` in closure without `nonlocal` | Add `nonlocal x` |
| `reduce` on empty list | Provide initializer as 3rd argument |
| Assuming `map`/`filter` return lists | Wrap with `list()` if needed |
