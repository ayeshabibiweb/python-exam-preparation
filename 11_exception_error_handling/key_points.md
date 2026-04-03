# 11 – Exception / Error Handling Key Points (Quick Reference)

## try / except / else / finally Skeleton

```python
try:
    result = risky()          # might raise
except SpecificError as e:    # handle known error
    handle(e)
except (OtherError, AnotherError):
    fallback()
else:
    # Only runs if NO exception was raised
    use(result)
finally:
    # ALWAYS runs (cleanup)
    cleanup()
```

---

## Exception Hierarchy (abridged)

```
BaseException
├── SystemExit          ← not a "real" error; raised by sys.exit()
├── KeyboardInterrupt   ← Ctrl+C
└── Exception           ← everything you normally catch
    ├── ValueError      ← right type, wrong value
    ├── TypeError       ← wrong type
    ├── LookupError
    │   ├── KeyError    ← dict key missing
    │   └── IndexError  ← list/str index out of range
    ├── AttributeError  ← object has no such attribute
    ├── NameError       ← variable not defined
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── OSError
    │   └── FileNotFoundError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── RuntimeError
    │   └── RecursionError
    ├── StopIteration
    └── NotImplementedError
```

---

## raise Variants

| Statement                    | Effect                                              |
|------------------------------|-----------------------------------------------------|
| `raise ValueError("msg")`    | Raise a new exception                               |
| `raise`                      | Re-raise current exception (in except block)        |
| `raise B from A`             | Chain: B caused by A                                |
| `raise B from None`          | Raise B, suppress chaining context                  |

---

## Custom Exception Pattern

```python
class AppError(Exception):
    """Base for all app errors."""

class ValidationError(AppError):
    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(f"'{field}': {message}")
```

---

## assert – When to Use / Avoid

| Situation                          | Use assert? |
|------------------------------------|-------------|
| Internal invariant / dev check     | ✅ Yes      |
| User input validation              | ❌ No       |
| Security check                     | ❌ No       |
| Side effects inside condition      | ❌ No       |

---

## Context Manager for Cleanup

```python
with open("file.txt") as f:    # __exit__ called automatically
    data = f.read()

# Custom (generator style)
from contextlib import contextmanager

@contextmanager
def managed():
    setup()
    try:
        yield resource
    finally:
        teardown()
```

---

## Logging Exceptions

```python
import logging
logger = logging.getLogger(__name__)

try:
    risky()
except Exception:
    logger.exception("Something went wrong")  # ERROR level + traceback
```

---

## Best Practices Checklist

- [ ] Catch the most specific exception available
- [ ] Never use bare `except:` (catches KeyboardInterrupt too)
- [ ] Log or re-raise – never silently swallow exceptions
- [ ] Use `finally` / `with` for resource cleanup
- [ ] Prefer custom exceptions for library/module errors
- [ ] Chain exceptions with `raise X from Y`
- [ ] Use `else` for code that should only run on success
- [ ] Document raised exceptions in docstrings (`Raises:` section)
