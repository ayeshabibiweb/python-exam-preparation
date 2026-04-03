"""
Topic 15: Debugging, Testing, and Optimization - Practice Problems
==================================================================
8 practice problems with full solutions.
"""

import unittest
import timeit


# ──────────────────────────────────────────────────────────────────────────────
# Problem 1: Debug a buggy function
# ──────────────────────────────────────────────────────────────────────────────
# PROBLEM: The function below is supposed to return the average of a list
# of numbers, but it has bugs. Identify and fix them.
#
# def average(numbers):
#     total = 0
#     for n in numbers:
#         total = total + n
#     return total / len(numbers)   # Bug: crashes on empty list

# SOLUTION:
def average(numbers):
    if not numbers:           # Fix: guard against empty list
        return 0.0
    return sum(numbers) / len(numbers)

print("Problem 1 – Debug average():")
print(average([1, 2, 3, 4, 5]))  # 3.0
print(average([]))                # 0.0 (was ZeroDivisionError)
print()


# ──────────────────────────────────────────────────────────────────────────────
# Problem 2: Write unit tests for a string utility
# ──────────────────────────────────────────────────────────────────────────────
# PROBLEM: Write at least 4 unit tests for the function below.
#
# def reverse_words(sentence):
#     """Return sentence with word order reversed."""

def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

class TestReverseWords(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_single_word(self):
        self.assertEqual(reverse_words("python"), "python")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_multiple_words(self):
        self.assertEqual(reverse_words("one two three"), "three two one")

    def test_extra_spaces(self):
        # str.split() without args collapses whitespace
        self.assertEqual(reverse_words("a  b"), "b a")

print("Problem 2 – TestReverseWords:")
suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseWords)
unittest.TextTestRunner(verbosity=2).run(suite)
print()


# ──────────────────────────────────────────────────────────────────────────────
# Problem 3: Test a custom exception
# ──────────────────────────────────────────────────────────────────────────────
# PROBLEM: Write a function that raises a custom exception for invalid input,
# then write tests that verify both the happy path and the exception.

class NegativeNumberError(ValueError):
    """Raised when a negative number is provided where a positive is required."""
    pass

def factorial(n):
    if n < 0:
        raise NegativeNumberError(f"factorial undefined for {n}")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_negative_raises(self):
        with self.assertRaises(NegativeNumberError):
            factorial(-3)

    def test_large(self):
        self.assertEqual(factorial(10), 3628800)

print("Problem 3 – TestFactorial:")
suite = unittest.TestLoader().loadTestsFromTestCase(TestFactorial)
unittest.TextTestRunner(verbosity=2).run(suite)
print()


# ──────────────────────────────────────────────────────────────────────────────
# Problem 4: setUp / tearDown pattern
# ──────────────────────────────────────────────────────────────────────────────
# PROBLEM: Create a Stack class and a test suite that uses setUp to create a
# fresh stack before each test.

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_push_increases_size(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)

    def test_pop_returns_last(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)

    def test_pop_empty_raises(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

print("Problem 4 – TestStack:")
suite = unittest.TestLoader().loadTestsFromTestCase(TestStack)
unittest.TextTestRunner(verbosity=2).run(suite)
print()


# ──────────────────────────────────────────────────────────────────────────────
# Problem 5: Measure performance with timeit
# ──────────────────────────────────────────────────────────────────────────────
# PROBLEM: Two implementations of finding duplicates in a list are given.
# Use timeit to compare them and explain why one is faster.

def find_duplicates_list(items):
    """O(n²) – checks each pair."""
    duplicates = []
    seen = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.append(item)
    return duplicates

def find_duplicates_set(items):
    """O(n) – uses set for O(1) membership."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

data = list(range(500)) + list(range(250))  # 250 duplicates

t_list = timeit.timeit(lambda: find_duplicates_list(data), number=200)
t_set  = timeit.timeit(lambda: find_duplicates_set(data),  number=200)

print("Problem 5 – Performance Comparison:")
print(f"  List-based (O(n²)): {t_list:.4f}s")
print(f"  Set-based  (O(n)):  {t_set:.4f}s")
print(f"  Set version is {t_list/t_set:.1f}x faster\n")


# ──────────────────────────────────────────────────────────────────────────────
# Problem 6: Optimise a slow function
# ──────────────────────────────────────────────────────────────────────────────
# PROBLEM: The function below is slow. Optimise it and verify the result.
#
# def sum_of_squares_slow(n):
#     return sum([i**2 for i in range(n)])
#
# Hint: use a generator expression instead of a list comprehension.

def sum_of_squares_slow(n):
    return sum([i**2 for i in range(n)])   # builds entire list

def sum_of_squares_fast(n):
    return sum(i**2 for i in range(n))     # lazy generator

N = 50_000
t_slow = timeit.timeit(lambda: sum_of_squares_slow(N), number=100)
t_fast = timeit.timeit(lambda: sum_of_squares_fast(N), number=100)

print("Problem 6 – Optimise sum_of_squares:")
assert sum_of_squares_slow(N) == sum_of_squares_fast(N), "Results differ!"
print(f"  Slow (list): {t_slow:.4f}s")
print(f"  Fast (gen):  {t_fast:.4f}s")
print(f"  Results match: True\n")


# ──────────────────────────────────────────────────────────────────────────────
# Problem 7: Add logging to a function
# ──────────────────────────────────────────────────────────────────────────────
# PROBLEM: Rewrite search_item() to use the logging module instead of print()
# for debug output.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
log = logging.getLogger("search")

def search_item(items, target):
    log.debug("Searching for %r in list of %d items", target, len(items))
    for i, item in enumerate(items):
        if item == target:
            log.info("Found %r at index %d", target, i)
            return i
    log.warning("%r not found", target)
    return -1

print("Problem 7 – Logging:")
search_item(["apple", "banana", "cherry"], "banana")
search_item(["apple", "banana", "cherry"], "grape")
print()


# ──────────────────────────────────────────────────────────────────────────────
# Problem 8: Full test suite with multiple assertion types
# ──────────────────────────────────────────────────────────────────────────────
# PROBLEM: Write a comprehensive test suite for a Temperature class that
# stores a temperature in Celsius and can convert to Fahrenheit/Kelvin.

class Temperature:
    def __init__(self, celsius):
        if celsius < -273.15:
            raise ValueError("Temperature below absolute zero")
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def __repr__(self):
        return f"Temperature({self.celsius}°C)"

class TestTemperature(unittest.TestCase):
    def test_freezing_point(self):
        t = Temperature(0)
        self.assertAlmostEqual(t.to_fahrenheit(), 32.0)
        self.assertAlmostEqual(t.to_kelvin(), 273.15)

    def test_boiling_point(self):
        t = Temperature(100)
        self.assertAlmostEqual(t.to_fahrenheit(), 212.0)

    def test_body_temperature(self):
        t = Temperature(37)
        self.assertAlmostEqual(t.to_fahrenheit(), 98.6, places=1)

    def test_below_absolute_zero_raises(self):
        with self.assertRaises(ValueError):
            Temperature(-300)

    def test_absolute_zero(self):
        t = Temperature(-273.15)
        self.assertAlmostEqual(t.to_kelvin(), 0.0, places=2)

    def test_repr(self):
        t = Temperature(25)
        self.assertIn("25", repr(t))

print("Problem 8 – TestTemperature:")
suite = unittest.TestLoader().loadTestsFromTestCase(TestTemperature)
unittest.TextTestRunner(verbosity=2).run(suite)
