# Topic 13: Advanced Python Concepts

## Generators and Generator Functions

A **generator** is a special type of iterator that yields values one at a time, suspending execution between each yield. This makes them memory-efficient for large or infinite sequences.

### The `yield` Keyword

```python
def count_up(n):
    for i in range(n):
        yield i  # suspends here, resumes on next()
```

When a generator function is called, it returns a generator object without executing the body. Each call to `next()` resumes execution until the next `yield`.

**Key properties:**
- Generator functions contain at least one `yield` statement
- They return a generator object (lazy evaluation)
- State is preserved between `yield` calls (local variables, execution position)
- Once exhausted, they raise `StopIteration`

### Generator Expressions

Similar to list comprehensions, but use parentheses and produce a generator:

```python
squares_list = [x**2 for x in range(10)]        # list – all in memory
squares_gen  = (x**2 for x in range(10))         # generator – lazy
```

Use generator expressions when you only need to iterate once and don't need all values simultaneously.

---

## Iterators and the Iterator Protocol

An **iterator** is any object that implements two methods:

| Method | Purpose |
|---|---|
| `__iter__()` | Returns the iterator object itself |
| `__next__()` | Returns the next value; raises `StopIteration` when done |

An **iterable** is anything you can pass to `iter()` — lists, tuples, dicts, sets, strings, generators, and any class implementing `__iter__`.

```python
my_list = [1, 2, 3]
it = iter(my_list)   # calls my_list.__iter__()
print(next(it))      # calls it.__next__() → 1
```

The `for` loop automatically calls `iter()` on the object and `next()` repeatedly until `StopIteration`.

### Custom Iterator Class

```python
class Counter:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
```

---

## Context Managers

A **context manager** controls setup and teardown around a block of code using the `with` statement. The most common use case is resource management (files, locks, DB connections).

```python
with open("file.txt") as f:
    data = f.read()
# file is automatically closed even if an exception occurs
```

### Implementing with `__enter__` / `__exit__`

```python
class ManagedResource:
    def __enter__(self):
        # setup – called at the start of the `with` block
        return self   # value bound to the `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        # teardown – called even if an exception occurred
        # return True to suppress the exception, False/None to propagate
        return False
```

`__exit__` receives exception info (all `None` if no exception occurred).

### `contextlib.contextmanager` Decorator

A simpler way to create context managers using a generator function:

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Setup")
    try:
        yield "the resource"   # value after `yield` is the `as` value
    finally:
        print("Teardown")      # always runs

with managed_resource() as r:
    print(r)
```

The code before `yield` is `__enter__`; code after (in `finally`) is `__exit__`.

---

## Closures and the LEGB Rule

### LEGB Scope

Python resolves names in this order:
1. **L**ocal – inside the current function
2. **E**nclosing – any enclosing function scopes (inner/outer)
3. **G**lobal – module-level names
4. **B**uilt-in – Python's built-in names (`len`, `print`, etc.)

### Closures

A **closure** is an inner function that captures variables from its enclosing scope, even after the outer function has returned.

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor   # `factor` is a free variable – captured
    return multiply

double = make_multiplier(2)
print(double(5))   # 10
```

### The `nonlocal` Keyword

Use `nonlocal` to assign to a variable in the enclosing (non-global) scope:

```python
def counter():
    count = 0
    def increment():
        nonlocal count   # without this, `count += 1` raises UnboundLocalError
        count += 1
        return count
    return increment
```

---

## Functional Programming Tools

### `map()` and `filter()`

```python
# map(func, iterable) → applies func to each element
squares = list(map(lambda x: x**2, [1, 2, 3, 4]))

# filter(func, iterable) → keeps elements where func returns True
evens = list(filter(lambda x: x % 2 == 0, range(10)))
```

Both return iterators (lazy). Wrap in `list()` to materialise.

### `reduce()` from `functools`

```python
from functools import reduce

total = reduce(lambda acc, x: acc + x, [1, 2, 3, 4, 5])  # 15
```

`reduce` applies a binary function cumulatively: `((((1+2)+3)+4)+5)`.

### `zip()` and `enumerate()`

```python
names = ["Alice", "Bob"]
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")
```

### `sorted()` with `key` Parameter

```python
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)               # sort by length
sorted_words = sorted(words, key=str.lower)         # case-insensitive
students = sorted(students, key=lambda s: s.grade, reverse=True)
```

### `functools.partial`

Creates a new function with some arguments pre-filled:

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)
print(square(5))   # 25
```

---

## Common Mistakes and Gotchas

### 1. Generator Exhaustion
```python
gen = (x for x in range(3))
list(gen)   # [0, 1, 2]
list(gen)   # [] ← already exhausted!
```

### 2. Late Binding in Closures
```python
# Bug: all lambdas capture the same `i`
funcs = [lambda x: x * i for i in range(3)]
funcs[0](1)   # 2, not 0!

# Fix: capture current value with default argument
funcs = [lambda x, i=i: x * i for i in range(3)]
```

### 3. Forgetting `nonlocal`
```python
def outer():
    x = 0
    def inner():
        x += 1      # UnboundLocalError – Python thinks x is local
    inner()
```

### 4. Using `list()` on a Consumed Iterator
Once an iterator is exhausted, you cannot restart it — create a new one.

### 5. `reduce` with Empty Sequence
`reduce` on an empty sequence raises `TypeError` unless you provide an `initializer` as the third argument.

### 6. `map`/`filter` Are Lazy
They return iterator objects, not lists. If you need to iterate multiple times, convert to `list` first.
