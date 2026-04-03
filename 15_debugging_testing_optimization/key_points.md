# Topic 15: Debugging, Testing & Optimization – Key Points
# ==========================================================

## Debugging Techniques

| Technique | When to Use |
|-----------|-------------|
| `print()` | Quick, simple debugging |
| `logging` | Production code, configurable levels |
| `pdb` / `breakpoint()` | Interactive step-through debugging |
| IDE debugger | Complex logic, GUI breakpoints |

### logging Levels (low → high severity)
```python
import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

logger.debug("Detailed diagnostic info")
logger.info("Confirmation things work")
logger.warning("Something unexpected")
logger.error("Serious problem")
logger.critical("Program may not continue")
```

### pdb Commands
| Command | Action |
|---------|--------|
| `n` | Next line (step over) |
| `s` | Step into function |
| `c` | Continue execution |
| `p expr` | Print expression value |
| `l` | List source around current line |
| `q` | Quit debugger |
| `b N` | Set breakpoint at line N |
| `h` | Help |

```python
breakpoint()   # Python 3.7+ – drops into pdb at this line
```

---

## unittest Quick Reference

### Basic Structure
```python
import unittest

class TestMyModule(unittest.TestCase):
    def setUp(self):      # runs BEFORE each test
        self.data = [1, 2, 3]

    def tearDown(self):   # runs AFTER each test
        pass

    def test_something(self):
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
```

### Assertion Methods
| Method | Checks |
|--------|--------|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIs(a, b)` | `a is b` |
| `assertIsNone(x)` | `x is None` |
| `assertIn(a, b)` | `a in b` |
| `assertRaises(Exc)` | Exception is raised |
| `assertAlmostEqual(a, b)` | `abs(a-b) <= 7 decimal places` |
| `assertGreater(a, b)` | `a > b` |

### Testing Exceptions
```python
with self.assertRaises(ValueError):
    risky_function(-1)
```

### subTest for Parametrised Tests
```python
def test_multiple_cases(self):
    cases = [(1, 1), (2, 4), (3, 9)]
    for n, expected in cases:
        with self.subTest(n=n):
            self.assertEqual(square(n), expected)
```

---

## Performance Profiling

### timeit
```python
import timeit
t = timeit.timeit(lambda: my_function(), number=1000)
print(f"{t:.4f}s for 1000 runs")
```

### cProfile
```python
import cProfile
cProfile.run('my_function()')

# Or with pstats for sorted output:
import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()
my_function()
pr.disable()
s = io.StringIO()
pstats.Stats(pr, stream=s).sort_stats('cumulative').print_stats(10)
print(s.getvalue())
```

---

## Optimisation Tips

| Technique | Instead of | Use |
|-----------|-----------|-----|
| Membership test | `item in list` O(n) | `item in set` O(1) |
| String building | `s += chunk` in loop | `"".join(parts)` |
| Lazy evaluation | `[x for x in ...]` | `(x for x in ...)` |
| Avoid global lookups | `math.sqrt` in loop | `sqrt = math.sqrt` once |
| Cache expensive calls | Recompute every time | `functools.lru_cache` |
| Use builtins | Manual loops | `sum()`, `max()`, `map()` |

### Big-O Quick Reference
| O() | Name | Example |
|-----|------|---------|
| O(1) | Constant | dict/set lookup |
| O(log n) | Logarithmic | binary search |
| O(n) | Linear | list scan |
| O(n log n) | Linearithmic | `list.sort()` |
| O(n²) | Quadratic | nested loops |

### lru_cache
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## Common Mistakes

- **Catching bare `Exception`** – too broad; catch specific types.
- **Ignoring exceptions silently** – at least `logging.exception(e)`.
- **Testing implementation not behaviour** – test public API outcomes.
- **Not resetting state in setUp** – tests depend on each other's side effects.
- **Premature optimisation** – profile first, then optimise the bottleneck.
- **Micro-optimising readable code** – readability > micro-speed in most cases.
