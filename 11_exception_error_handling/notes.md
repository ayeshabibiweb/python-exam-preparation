# 11 – Exception and Error Handling

## 1. Python Exception Hierarchy

All exceptions inherit from `BaseException`. The subtree you normally work with inherits
from `Exception`:

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── AttributeError
    ├── NameError
    ├── OSError  (also IOError)
    │   └── FileNotFoundError
    ├── RuntimeError
    │   └── RecursionError
    ├── StopIteration
    ├── ImportError
    │   └── ModuleNotFoundError
    └── ... (many more)
```

---

## 2. `try / except / else / finally` Blocks

```python
try:
    # Code that might raise
    result = risky_operation()
except SomeError as e:
    # Handle the error; 'e' holds the exception object
    print(f"Error: {e}")
except (AnotherError, YetAnotherError):
    # Handle multiple exception types together
    pass
else:
    # Runs only if NO exception was raised in 'try'
    print("Success:", result)
finally:
    # ALWAYS runs, even if an exception occurred (or a return was hit)
    cleanup()
```

Execution flow:
- `else` block runs only on **success** (no exception).
- `finally` block runs **always** – even if `return` or `break` or another exception
  occurs inside `except`.

---

## 3. Catching Specific vs Generic Exceptions

Prefer **specific** exceptions over broad ones:

```python
# Too broad – hides unexpected bugs
try:
    data = process(x)
except Exception:
    pass

# Better – only handle what you expect
try:
    data = process(x)
except ValueError as e:
    handle_bad_value(e)
except TypeError as e:
    handle_wrong_type(e)
```

Bare `except:` (without a type) catches even `SystemExit` and `KeyboardInterrupt` –
almost always wrong.

---

## 4. Exception Chaining (`raise … from`)

When handling one exception and raising another, chain them to preserve context:

```python
try:
    value = int(user_input)
except ValueError as e:
    raise RuntimeError("Configuration load failed") from e
```

The traceback will show "The above exception was the direct cause of …".

Use `raise X from None` to suppress the original context when it would be confusing.

---

## 5. Custom Exception Classes

Define custom exceptions by inheriting from `Exception` (or a more specific built-in):

```python
class AppError(Exception):
    """Base class for all application errors."""

class ValidationError(AppError):
    def __init__(self, field: str, message: str):
        self.field   = field
        super().__init__(f"Validation error on '{field}': {message}")

class NotFoundError(AppError):
    pass
```

Benefits:
- Callers can catch your specific error without catching all exceptions.
- You can add structured data (field name, error code, etc.).
- Keeps error handling predictable and documented.

---

## 6. `raise` Statement

```python
raise ValueError("Bad value")               # raise a new exception
raise                                        # re-raise the current exception (inside except)
raise TypeError("Wrong type") from original  # chained exception
```

---

## 7. `assert` Statement

```python
assert condition, "Optional message"
```

`assert` raises `AssertionError` if the condition is `False`.

**When to use:** internal consistency checks, invariants during development and testing.

**When NOT to use:**
- Input validation from users or external sources (use proper exceptions).
- Side effects should never go inside assertions (they are stripped with `python -O`).
- Security-critical checks (optimised builds skip them).

---

## 8. Context Managers for Cleanup

Instead of `try/finally`, use `with`:

```python
# Without context manager
f = open("file.txt")
try:
    data = f.read()
finally:
    f.close()

# With context manager (preferred)
with open("file.txt") as f:
    data = f.read()   # f.close() called automatically, even on exception
```

Custom context managers: use `contextlib.contextmanager` decorator or implement
`__enter__`/`__exit__`.

---

## 9. Built-in Exceptions Reference

| Exception            | Common cause                                      |
|----------------------|---------------------------------------------------|
| `ValueError`         | Right type, wrong value (`int("abc")`)            |
| `TypeError`          | Wrong type passed (`"a" + 1`)                     |
| `KeyError`           | Dict key not found (`d["missing"]`)               |
| `IndexError`         | List index out of range (`lst[99]`)               |
| `AttributeError`     | Object has no attribute (`None.split()`)          |
| `NameError`          | Variable not defined (`print(undefined_var)`)     |
| `ZeroDivisionError`  | Division by zero (`1 / 0`)                        |
| `FileNotFoundError`  | File path does not exist (`open("no.txt")`)       |
| `ImportError`        | Module cannot be imported                         |
| `RecursionError`     | Maximum recursion depth exceeded                  |
| `StopIteration`      | Iterator exhausted                                |
| `OverflowError`      | Numeric result too large for float                |
| `MemoryError`        | Ran out of memory                                 |
| `NotImplementedError`| Abstract method not overridden                    |
| `RuntimeError`       | Generic runtime error                             |

---

## 10. Logging Exceptions

Use the `logging` module rather than printing:

```python
import logging

logger = logging.getLogger(__name__)

try:
    result = risky()
except ValueError:
    logger.exception("Unexpected value error")  # logs with full traceback
```

`logger.exception()` logs at ERROR level and appends the current traceback automatically.
`logger.error("msg", exc_info=True)` is equivalent.

---

## 11. Best Practices

1. **Catch the most specific exception possible.**
2. **Never use bare `except:`** without a very good reason.
3. **Always log or re-raise** – silent `except` blocks hide bugs.
4. **Use `finally`** (or `with`) for resource cleanup.
5. **Use custom exceptions** for your own library/module errors.
6. **Include helpful context** in exception messages.
7. **Chain exceptions** with `raise X from Y` to preserve root cause.
8. **Don't use exceptions for flow control** in performance-critical paths.
9. **Document which exceptions your functions raise** in docstrings.

---

## 12. Common Mistakes

1. **Swallowing exceptions silently**
   ```python
   try:
       risky()
   except Exception:
       pass   # BUG hidden forever
   ```

2. **Too broad catch**
   ```python
   except Exception as e:
       print(e)   # prints but still too broad
   ```

3. **Catching in the wrong place** – handle exceptions where you have enough context
   to recover. Do not scatter `try/except` everywhere "just in case".

4. **Re-raising wrongly**
   ```python
   except SomeError as e:
       raise SomeError(str(e))   # loses the original traceback!
   # Use:
       raise                     # re-raises with original traceback intact
   ```

5. **Using `assert` for user input validation** – asserts can be disabled with `python -O`.

6. **Returning `None` on error instead of raising** – forces callers to check for `None`
   everywhere, and silent failures are introduced when they forget.

7. **Forgetting `else` exists** – putting post-success code inside `try` expands the
   "danger zone" unnecessarily.
