# 05 – Functions & Methods: Key Points

## Function Definition

```python
def function_name(param1, param2, param3="default"):
    """Docstring."""
    return value
```

## Parameter Order Rule

```
def f(positional, *args, keyword_only, **kwargs):
```

| Position | Type | Notes |
|---|---|---|
| 1 | Regular positional | Required unless default given |
| 2 | `*args` | Captures extra positionals into a **tuple** |
| 3 | Keyword-only | After `*args`; must be named at call site |
| 4 | `**kwargs` | Captures extra keyword args into a **dict** |

## Lambda Syntax

```python
lambda param1, param2: expression
```

- One expression only; no statements.
- Returns the expression value implicitly.

## Decorator Syntax

```python
import functools

def my_decorator(func):
    @functools.wraps(func)      # preserves __name__, __doc__
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper

@my_decorator
def my_function(): ...
# Equivalent to: my_function = my_decorator(my_function)
```

## Scope (LEGB)

| Letter | Scope |
|---|---|
| L | Local (inside the current function) |
| E | Enclosing (outer function, for closures) |
| G | Global (module level) |
| B | Built-in (Python's `len`, `range`, etc.) |

Use `global x` to assign to a global variable inside a function.  
Use `nonlocal x` to assign to an enclosing (but non-global) variable.

## Recursion Template

```python
def recursive(n):
    if base_condition(n):   # base case — MUST have one
        return base_value
    return recursive(smaller_n)  # must move toward base case
```

## Common Higher-Order Functions

```python
map(func, iterable)        # apply func to every item → iterator
filter(func, iterable)     # keep items where func returns True → iterator
sorted(iterable, key=func) # sort using func as key
functools.reduce(func, iterable)  # fold left: func(func(a,b),c)...
```

## Quick Reminders

- Default mutable arguments are a **bug trap** — use `None` instead.
- `lambda` cannot contain statements; use `def` for anything complex.
- `@functools.wraps(func)` is mandatory inside decorators.
- Python's default recursion limit is **1000**; prefer iteration for deep recursion.
- Functions are first-class: pass them, return them, store them in collections.
