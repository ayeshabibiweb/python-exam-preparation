# Topic 15: Debugging, Testing & Optimization

## 1. Debugging Techniques

### Print Debugging
The simplest technique: insert `print()` statements to inspect values at key points.

```python
def calculate(x, y):
    print(f"[DEBUG] x={x}, y={y}")   # temporary diagnostic
    result = x / y
    print(f"[DEBUG] result={result}")
    return result
```

**Pros:** Quick, zero setup. **Cons:** Clutters code, must be removed manually.

### The `logging` Module (Preferred over print)
`logging` provides severity levels, timestamps, and easy enable/disable:

```python
import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

logging.debug("Detailed info for diagnosing problems")
logging.info("General operational messages")
logging.warning("Something unexpected, but program still works")
logging.error("Serious problem, function could not complete")
logging.critical("Program may not be able to continue")
```

Levels in order (lowest → highest): DEBUG < INFO < WARNING < ERROR < CRITICAL.  
Setting `level=logging.WARNING` silences DEBUG and INFO automatically.

---

## 2. The `pdb` Debugger

Python's built-in interactive debugger. Insert a breakpoint with:

```python
breakpoint()        # Python 3.7+ (preferred)
import pdb; pdb.set_trace()   # older style
```

### Essential pdb Commands

| Command | Action |
|---|---|
| `n` (next) | Execute current line, stay in same function |
| `s` (step) | Step into a function call |
| `c` (continue) | Run until next breakpoint |
| `p expr` | Print value of expression |
| `pp expr` | Pretty-print expression |
| `l` (list) | Show current code context |
| `q` (quit) | Exit debugger |
| `b line` | Set breakpoint at line number |
| `h` | Help |

---

## 3. `unittest` Module

Python's built-in testing framework. Tests live in classes that inherit from `unittest.TestCase`.

```python
import unittest

class TestMyFunc(unittest.TestCase):
    def setUp(self):        # runs before EACH test
        self.data = [1, 2, 3]

    def tearDown(self):     # runs after EACH test
        pass

    def test_length(self):
        self.assertEqual(len(self.data), 3)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

if __name__ == "__main__":
    unittest.main()
```

### Common Assertions

| Method | Checks |
|---|---|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x)` is True |
| `assertFalse(x)` | `bool(x)` is False |
| `assertIsNone(x)` | `x is None` |
| `assertIn(a, b)` | `a in b` |
| `assertRaises(Exc)` | block raises exception |
| `assertAlmostEqual(a, b)` | floats nearly equal |

---

## 4. pytest Basics

`pytest` is more concise — plain functions, no class required.

```bash
pip install pytest
pytest test_mymodule.py    # run tests
pytest -v                  # verbose output
```

```python
# test_example.py
def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0
```

### Fixtures (setup/teardown without classes)

```python
import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3]

def test_sum(sample_list):
    assert sum(sample_list) == 6
```

### Parametrize Decorator

```python
@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_param(x, y, expected):
    assert add(x, y) == expected
```

---

## 5. Performance Profiling

### `timeit` — Measure Small Code Snippets

```python
import timeit

# Quick one-liner
time_taken = timeit.timeit("[x**2 for x in range(1000)]", number=1000)
print(f"List comp: {time_taken:.4f}s")

# Using a callable
def my_func():
    return sum(range(10000))

print(timeit.timeit(my_func, number=500))
```

### `cProfile` — Full Program Profiling

```python
import cProfile
cProfile.run("my_function()")
```

Output shows: number of calls, total time, cumulative time per function.

---

## 6. Big O Notation Basics

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | Dictionary lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | List scan |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops |

---

## 7. Common Optimization Techniques

- **Use built-ins**: `sum()`, `map()`, `filter()` are implemented in C — faster than loops.
- **List comprehensions** are faster than equivalent `for` + `append` loops.
- **Generators** (`yield`) use O(1) memory vs O(n) for lists — use when iterating once.
- **Dictionary lookups** are O(1); avoid linear search with `in list` when possible.
- **`join()` for string concatenation**: `"".join(parts)` is faster than `+=` in a loop.
- **Local variables** are faster than global lookups inside tight loops.
- **`lru_cache`** (`functools`) caches expensive function results (memoization).

---

## 8. Test-Driven Development (TDD)

TDD cycle — **Red → Green → Refactor**:
1. **Red**: Write a failing test for the feature not yet implemented.
2. **Green**: Write the minimum code to make the test pass.
3. **Refactor**: Clean up the code while keeping tests green.

Benefits: forces clear requirements, creates a regression safety net, encourages modular design.

---

## 9. Common Mistakes

- Testing implementation details instead of behavior.
- Not isolating tests (tests that depend on each other or on external state).
- Ignoring `setUp`/`tearDown` — leads to shared mutable state between tests.
- Using `time.time()` instead of `timeit` for benchmarks (affected by system noise).
- Optimizing before profiling — "premature optimization is the root of all evil" (Knuth).
- Not handling `AssertionError` vs domain exceptions correctly in tests.
