"""
Topic 15: Debugging, Testing, and Optimization - Examples
==========================================================
10 runnable examples demonstrating debugging techniques, unit testing,
and performance optimization in Python 3.8+.
"""

import logging
import timeit
import cProfile
import pstats
import io
import unittest


# ── Example 1: Print Debugging ────────────────────────────────────────────────
print("=" * 60)
print("Example 1: Print Debugging")
print("=" * 60)

def find_max(numbers):
    print(f"[DEBUG] Input: {numbers}")          # debug trace
    if not numbers:
        print("[DEBUG] Empty list – returning None")
        return None
    current_max = numbers[0]
    for i, n in enumerate(numbers):
        print(f"[DEBUG] Comparing {n} with current_max={current_max}")
        if n > current_max:
            current_max = n
    print(f"[DEBUG] Result: {current_max}")
    return current_max

result = find_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Max value: {result}\n")


# ── Example 2: logging Module ─────────────────────────────────────────────────
print("=" * 60)
print("Example 2: logging Module")
print("=" * 60)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

def divide(a, b):
    logger.debug("divide(%s, %s) called", a, b)
    if b == 0:
        logger.error("Division by zero attempted")
        return None
    result = a / b
    logger.info("Result: %s", result)
    return result

divide(10, 2)
divide(5, 0)
print()


# ── Example 3: unittest – Basic TestCase ──────────────────────────────────────
print("=" * 60)
print("Example 3: unittest – Basic TestCase")
print("=" * 60)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class TestMathFunctions(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -2), -3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMathFunctions)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
print()


# ── Example 4: assertRaises ───────────────────────────────────────────────────
print("=" * 60)
print("Example 4: Testing Exceptions with assertRaises")
print("=" * 60)

def safe_sqrt(n):
    if n < 0:
        raise ValueError(f"Cannot take square root of {n}")
    return n ** 0.5

class TestSafeSqrt(unittest.TestCase):
    def test_positive(self):
        self.assertAlmostEqual(safe_sqrt(4), 2.0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            safe_sqrt(-1)

    def test_zero(self):
        self.assertEqual(safe_sqrt(0), 0.0)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSafeSqrt)
unittest.TextTestRunner(verbosity=2).run(suite)
print()


# ── Example 5: setUp and tearDown ─────────────────────────────────────────────
print("=" * 60)
print("Example 5: setUp and tearDown")
print("=" * 60)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Runs before EACH test method
        self.account = BankAccount(100)
        print(f"  setUp: account balance = {self.account.balance}")

    def tearDown(self):
        # Runs after EACH test method
        print(f"  tearDown: final balance = {self.account.balance}")

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_overdraft(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

suite = unittest.TestLoader().loadTestsFromTestCase(TestBankAccount)
unittest.TextTestRunner(verbosity=2).run(suite)
print()


# ── Example 6: subTest for Parametrised Tests ─────────────────────────────────
print("=" * 60)
print("Example 6: subTest for Parametrised Testing")
print("=" * 60)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

class TestPalindrome(unittest.TestCase):
    def test_various_cases(self):
        cases = [
            ("racecar", True),
            ("hello",   False),
            ("A man a plan a canal Panama".replace(" ", ""), True),
            ("level",   True),
            ("world",   False),
        ]
        for word, expected in cases:
            with self.subTest(word=word):
                self.assertEqual(is_palindrome(word), expected)

suite = unittest.TestLoader().loadTestsFromTestCase(TestPalindrome)
unittest.TextTestRunner(verbosity=2).run(suite)
print()


# ── Example 7: timeit Module ──────────────────────────────────────────────────
print("=" * 60)
print("Example 7: timeit – Measuring Performance")
print("=" * 60)

# Compare string concatenation methods
def concat_plus(n):
    result = ""
    for i in range(n):
        result += str(i)
    return result

def concat_join(n):
    return "".join(str(i) for i in range(n))

N = 1000
t_plus = timeit.timeit(lambda: concat_plus(N), number=500)
t_join = timeit.timeit(lambda: concat_join(N), number=500)

print(f"String '+' concatenation (500 runs): {t_plus:.4f}s")
print(f"''.join() method       (500 runs): {t_join:.4f}s")
print(f"join() is {t_plus / t_join:.1f}x faster\n")


# ── Example 8: cProfile ───────────────────────────────────────────────────────
print("=" * 60)
print("Example 8: cProfile – Function Profiling")
print("=" * 60)

def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

def fast_sum(n):
    return n * (n - 1) // 2

profiler = cProfile.Profile()
profiler.enable()
slow_sum(100_000)
fast_sum(100_000)
profiler.disable()

stream = io.StringIO()
stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
stats.print_stats(5)
print(stream.getvalue())


# ── Example 9: Generator vs List – Memory Optimisation ────────────────────────
print("=" * 60)
print("Example 9: Generator vs List – Memory & Speed")
print("=" * 60)

import sys

# List comprehension materialises everything in memory
list_comp = [x * x for x in range(100_000)]
# Generator expression is lazy – one value at a time
gen_expr  = (x * x for x in range(100_000))

print(f"List size in memory: {sys.getsizeof(list_comp):,} bytes")
print(f"Generator size:      {sys.getsizeof(gen_expr):,} bytes")

t_list = timeit.timeit(lambda: sum([x*x for x in range(10_000)]), number=200)
t_gen  = timeit.timeit(lambda: sum(x*x for x in range(10_000)),  number=200)
print(f"Sum via list (200 runs): {t_list:.4f}s")
print(f"Sum via gen  (200 runs): {t_gen:.4f}s\n")


# ── Example 10: dict Lookup vs Linear Search ──────────────────────────────────
print("=" * 60)
print("Example 10: O(1) dict Lookup vs O(n) Linear Search")
print("=" * 60)

data = list(range(100_000))
data_set = set(data)

target = 99_999

t_list_search = timeit.timeit(lambda: target in data,     number=1_000)
t_set_lookup  = timeit.timeit(lambda: target in data_set, number=1_000)

print(f"List  'in' (1 000 runs): {t_list_search:.4f}s  – O(n)")
print(f"Set   'in' (1 000 runs): {t_set_lookup:.6f}s – O(1)")
print(f"Set is {t_list_search / t_set_lookup:.0f}x faster for membership test")
