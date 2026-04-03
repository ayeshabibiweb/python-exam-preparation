"""
Topic 13: Advanced Python Concepts – Examples
Runnable examples demonstrating generators, iterators, context managers,
closures, and functional programming tools.
"""

# ─────────────────────────────────────────────
# Example 1: Generator Function with yield
# ─────────────────────────────────────────────
print("=" * 50)
print("Example 1: Generator Function with yield")
print("=" * 50)

def fibonacci():
    """Infinite Fibonacci generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def count_down(n):
    """Finite generator counting down from n to 1."""
    print(f"  Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("  Countdown complete!")

# Finite generator
for val in count_down(5):
    print(f"  {val}")

# Take first 8 Fibonacci numbers
fib = fibonacci()
first_eight = [next(fib) for _ in range(8)]
print(f"  First 8 Fibonacci: {first_eight}")


# ─────────────────────────────────────────────
# Example 2: Generator Expression
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Example 2: Generator Expression")
print("=" * 50)

import sys

# List comprehension – all values stored in memory
squares_list = [x ** 2 for x in range(1_000)]
print(f"  List size : {sys.getsizeof(squares_list):,} bytes")

# Generator expression – lazy; produces values on demand
squares_gen = (x ** 2 for x in range(1_000))
print(f"  Generator size: {sys.getsizeof(squares_gen):,} bytes")

# Chaining generator expressions (still lazy)
evens = (x for x in range(20) if x % 2 == 0)
doubled = (x * 2 for x in evens)
print(f"  First 5 doubled-evens: {[next(doubled) for _ in range(5)]}")


# ─────────────────────────────────────────────
# Example 3: Custom Iterator Class
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Example 3: Custom Iterator Class")
print("=" * 50)

class Range:
    """A simplified re-implementation of range()."""

    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self          # the iterator IS the iterable here

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


my_range = Range(0, 10, 2)
print(f"  Custom range(0, 10, 2): {list(my_range)}")

# Demonstrate that for-loops use the iterator protocol
for val in Range(1, 6):
    print(f"  {val}", end=" ")
print()


# ─────────────────────────────────────────────
# Example 4: Infinite Generator with islice
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Example 4: Infinite Generator with islice")
print("=" * 50)

from itertools import islice

def natural_numbers(start=1):
    """Yields 1, 2, 3, ... indefinitely."""
    n = start
    while True:
        yield n
        n += 1

def primes():
    """Yields prime numbers indefinitely using trial division."""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for n in natural_numbers(2):
        if is_prime(n):
            yield n

# islice lets us take a slice from an infinite generator safely
first_10_primes = list(islice(primes(), 10))
print(f"  First 10 primes: {first_10_primes}")

first_20_naturals = list(islice(natural_numbers(), 20))
print(f"  First 20 naturals: {first_20_naturals}")


# ─────────────────────────────────────────────
# Example 5: Context Manager with __enter__ / __exit__
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Example 5: Context Manager with __enter__ / __exit__")
print("=" * 50)

import time

class Timer:
    """Measures elapsed time for a block of code."""

    def __enter__(self):
        self.start = time.perf_counter()
        print("  Timer started")
        return self   # available as the `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"  Timer stopped. Elapsed: {elapsed:.6f}s")
        # returning False (or None) lets exceptions propagate
        return False


with Timer() as t:
    total = sum(range(100_000))
print(f"  Sum result: {total}")


class SuppressError:
    """Context manager that suppresses a specific exception type."""

    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.exception_types):
            print(f"  Suppressed {exc_type.__name__}: {exc_val}")
            return True   # suppress the exception
        return False


with SuppressError(ZeroDivisionError):
    result = 10 / 0   # would normally crash
print("  Execution continued after suppressed exception")


# ─────────────────────────────────────────────
# Example 6: contextlib.contextmanager Decorator
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Example 6: contextlib.contextmanager Decorator")
print("=" * 50)

from contextlib import contextmanager

@contextmanager
def indent_output(level=1):
    """Adds indentation markers around a block of output."""
    indent = "  " * level
    print(f"{indent}>>> Block START")
    try:
        yield indent   # code before yield = __enter__
    finally:
        print(f"{indent}>>> Block END")   # always runs = __exit__


with indent_output(2) as prefix:
    print(f"{prefix}Inside the managed block")
    print(f"{prefix}Doing some work...")


@contextmanager
def temporary_list():
    """Provides a list that is cleared after the with block."""
    items = []
    yield items
    items.clear()
    print("  List cleared after block")


with temporary_list() as lst:
    lst.extend([1, 2, 3])
    print(f"  Inside block: {lst}")
print(f"  After block: {lst}")   # cleared


# ─────────────────────────────────────────────
# Example 7: Closure Example
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Example 7: Closures and the nonlocal Keyword")
print("=" * 50)

def make_counter(start=0, step=1):
    """Returns a counter function (closure over `count` and `step`)."""
    count = start

    def counter():
        nonlocal count      # tells Python to use the enclosing `count`
        value = count
        count += step
        return value

    return counter


count_by_one  = make_counter()
count_by_five = make_counter(0, 5)

print(f"  count_by_one: {count_by_one()}, {count_by_one()}, {count_by_one()}")
print(f"  count_by_five: {count_by_five()}, {count_by_five()}, {count_by_five()}")
# Each closure maintains its OWN `count` variable

def make_adder(n):
    """Classic closure: captures `n` from outer scope."""
    return lambda x: x + n

add10 = make_adder(10)
add20 = make_adder(20)
print(f"  add10(5) = {add10(5)}, add20(5) = {add20(5)}")


# ─────────────────────────────────────────────
# Example 8: map() and filter()
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Example 8: map() and filter()")
print("=" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: apply a function to every element
squared = list(map(lambda x: x ** 2, numbers))
print(f"  Squared    : {squared}")

# map with a named function
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

temps_c = [0, 20, 37, 100]
temps_f = list(map(celsius_to_fahrenheit, temps_c))
print(f"  Celsius    : {temps_c}")
print(f"  Fahrenheit : {[round(t, 1) for t in temps_f]}")

# filter: keep only elements that satisfy a predicate
evens  = list(filter(lambda x: x % 2 == 0, numbers))
odds   = list(filter(lambda x: x % 2 != 0, numbers))
print(f"  Evens      : {evens}")
print(f"  Odds       : {odds}")

# Combining map and filter
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(f"  Even squares: {even_squares}")

# Equivalent list comprehension (often more readable)
even_squares_lc = [x ** 2 for x in numbers if x % 2 == 0]
print(f"  Same with LC: {even_squares_lc}")


# ─────────────────────────────────────────────
# Example 9: reduce()
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Example 9: reduce() from functools")
print("=" * 50)

from functools import reduce

nums = [1, 2, 3, 4, 5]

# Sum: ((((1+2)+3)+4)+5) = 15
total = reduce(lambda acc, x: acc + x, nums)
print(f"  Sum    : {total}")

# Product: ((((1×2)×3)×4)×5) = 120
product = reduce(lambda acc, x: acc * x, nums)
print(f"  Product: {product}")

# Maximum without using max()
maximum = reduce(lambda a, b: a if a > b else b, nums)
print(f"  Maximum: {maximum}")

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda acc, x: acc + x, nested)
print(f"  Flattened: {flat}")

# Using initial value (third argument)
total_with_init = reduce(lambda acc, x: acc + x, nums, 100)
print(f"  Sum with initializer 100: {total_with_init}")


# ─────────────────────────────────────────────
# Example 10: Partial Functions and Functional Programming
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("Example 10: Partial Functions and Functional Programming")
print("=" * 50)

from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)

print(f"  square(5) = {square(5)}")
print(f"  cube(3)   = {cube(3)}")
print(f"  square applied to [1..5]: {list(map(square, range(1, 6)))}")

# partial with positional arguments
def log(level, message):
    print(f"  [{level}] {message}")

info  = partial(log, "INFO")
error = partial(log, "ERROR")

info("Application started")
error("Something went wrong")

# Combining partial, map, filter, reduce in a pipeline
data = range(1, 21)

result = reduce(
    lambda acc, x: acc + x,
    map(square, filter(lambda x: x % 3 == 0, data))
)
print(f"  Sum of squares of multiples of 3 (1-20): {result}")

# zip and enumerate
names  = ["Alice", "Bob", "Charlie"]
grades = [92, 85, 78]

print("\n  Student report:")
for rank, (name, grade) in enumerate(zip(names, grades), start=1):
    print(f"    {rank}. {name}: {grade}")

# sorted with key
students = [("Alice", 92), ("Bob", 85), ("Charlie", 78), ("Diana", 95)]
by_grade = sorted(students, key=lambda s: s[1], reverse=True)
print(f"\n  Sorted by grade (desc): {by_grade}")
