# 05 – Functions & Methods

## Overview

Functions are the primary building blocks of reusable code in Python. A function encapsulates a block of logic that can be called by name, optionally accepting inputs and producing outputs. Mastering functions is essential for writing clean, testable, and maintainable programs.

---

## Function Definition Syntax

Use the `def` keyword to define a function, followed by the name, parentheses for parameters, and a colon. The body is indented.

```python
def greet(name):
    """Docstring describes what the function does."""
    return f"Hello, {name}!"
```

A **docstring** (triple-quoted string immediately after `def`) is a best practice for documenting purpose, parameters, and return values.

---

## Parameters vs Arguments

- **Parameter**: the variable listed in the function definition (`name` above).
- **Argument**: the actual value passed when calling the function (`"Alice"`).

```python
def add(x, y):   # x and y are parameters
    return x + y

add(3, 4)        # 3 and 4 are arguments
```

---

## Default Parameters

Parameters can have default values, making them optional at call time. Defaults must come **after** required parameters.

```python
def power(base, exp=2):
    return base ** exp

power(3)     # → 9  (uses default exp=2)
power(3, 3)  # → 27
```

> **Warning**: Never use mutable objects (lists, dicts) as defaults — they are created once and shared across calls. Use `None` and create inside the function instead.

---

## *args and **kwargs

`*args` collects extra **positional** arguments into a tuple; `**kwargs` collects extra **keyword** arguments into a dict.

```python
def summarise(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

summarise(1, 2, 3, name="Alice", role="student")
```

Standard parameter order: `(regular, *args, keyword_only, **kwargs)`.

---

## Return Values

A function returns `None` by default if no `return` statement is reached. You can return any object, including tuples for multiple values.

```python
def min_max(numbers):
    return min(numbers), max(numbers)  # returns a tuple

lo, hi = min_max([3, 1, 4, 1, 5])
```

---

## Lambda Functions

A `lambda` is an anonymous single-expression function. Useful for short callbacks.

```python
square = lambda x: x ** 2
double = lambda x: x * 2

sorted_data = sorted(words, key=lambda w: len(w))
```

Lambdas cannot contain statements (no `if`/`else` blocks, no `for` loops), only expressions.

---

## Decorators

A **decorator** is a function that wraps another function to add behaviour before and/or after the original call.

```python
import functools

def timer(func):
    @functools.wraps(func)   # preserves __name__ and __doc__
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))
```

`@functools.wraps(func)` is important — without it, the wrapper replaces the original function's `__name__` and `__doc__`.

The `@decorator` syntax is shorthand for `slow_sum = timer(slow_sum)`.

### Stacking decorators

```python
@decorator_a
@decorator_b
def my_func(): ...
# equivalent to: my_func = decorator_a(decorator_b(my_func))
```

---

## Function Scope and Closures

Python follows **LEGB** scope resolution: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

- Variables assigned inside a function are local by default.
- Use `global x` to modify a global variable inside a function (use sparingly).
- Use `nonlocal x` to modify a variable in the enclosing (but not global) scope.

A **closure** is a function that remembers the enclosing scope's variables even after that scope has finished executing.

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor   # factor is "closed over"
    return multiply

triple = make_multiplier(3)
triple(10)  # → 30
```

---

## Recursion

A recursive function calls itself. Every recursive function needs:
1. A **base case** that stops the recursion.
2. A **recursive case** that moves toward the base case.

```python
def factorial(n):
    if n == 0:        # base case
        return 1
    return n * factorial(n - 1)  # recursive case
```

Python's default recursion limit is 1000 (`sys.getrecursionlimit()`). Deep recursion → `RecursionError`.

---

## First-Class Functions

In Python, functions are objects. They can be:
- Assigned to variables
- Passed as arguments
- Returned from other functions
- Stored in data structures

```python
ops = {"add": lambda a, b: a + b, "mul": lambda a, b: a * b}
ops["add"](2, 3)  # → 5
```

**Higher-order functions** accept or return functions. Built-in examples: `map()`, `filter()`, `sorted(key=...)`.

---

## Common Mistakes

| Mistake | Example | Fix |
|---|---|---|
| Mutable default argument | `def f(lst=[])` | `def f(lst=None): lst = lst or []` |
| Forgetting `return` | `def add(a,b): a+b` | `return a + b` |
| Modifying global without `global` | `count += 1` in a function | Declare `global count` first |
| Lambda with statement | `lambda x: if x>0: ...` | Use `def` or ternary: `lambda x: x if x > 0 else 0` |
| Shadowing builtins | `list = [1,2,3]` | Use a different name like `my_list` |
| Ignoring `functools.wraps` in decorators | Wrapper loses `__name__` | Always use `@functools.wraps(func)` |

---

## Summary

- Use `def` for named functions, `lambda` for short anonymous ones.
- `*args` and `**kwargs` provide flexible call signatures.
- Decorators are a clean pattern for cross-cutting concerns (logging, timing, auth).
- Closures let inner functions remember enclosing-scope variables.
- Recursion needs a base case; prefer iteration for large inputs.
- Functions are first-class objects — embrace higher-order programming.
