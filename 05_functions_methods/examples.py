# 05 – Functions & Methods: Examples
# Run this file: python examples.py
# All examples print their output so you can see results immediately.

print("=" * 60)
print("EXAMPLE 1: Basic Function Definition and Calling")
print("=" * 60)

def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"

def add(a, b):
    """Return the sum of a and b."""
    return a + b

print(greet("Alice"))          # Hello, Alice!
print(greet("Bob"))            # Hello, Bob!
print(add(3, 7))               # 10
print(add(-1, 1))              # 0
print(f"greet.__name__ = {greet.__name__}")
print(f"greet.__doc__  = {greet.__doc__}")


print("\n" + "=" * 60)
print("EXAMPLE 2: Default Parameters")
print("=" * 60)

def power(base, exponent=2):
    """Raise base to the given exponent (default: square)."""
    return base ** exponent

def introduce(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(power(4))          # 16  — uses default exponent=2
print(power(2, 10))      # 1024
print(power(3, 3))       # 27

print(introduce("Alice"))                             # Hello, Alice!
print(introduce("Bob", greeting="Hi"))                # Hi, Bob!
print(introduce("Carol", greeting="Hey", punctuation="~"))  # Hey, Carol~

# Demonstrating the mutable-default-argument trap (wrong way):
def bad_append(value, lst=[]):
    lst.append(value)
    return lst

# Correct way using None sentinel:
def good_append(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(bad_append(1))   # [1]
print(bad_append(2))   # [1, 2]  ← bug: shares the same list!
print(good_append(1))  # [1]
print(good_append(2))  # [2]     ← correct: fresh list each time


print("\n" + "=" * 60)
print("EXAMPLE 3: *args — Variable Positional Arguments")
print("=" * 60)

def total(*numbers):
    """Sum any number of positional arguments."""
    print(f"  Received args tuple: {numbers}")
    return sum(numbers)

print(total(1, 2))           # 3
print(total(10, 20, 30))     # 60
print(total(5))              # 5
print(total())               # 0

def first_and_rest(first, *rest):
    print(f"  first={first}, rest={rest}")

first_and_rest("a")
first_and_rest("a", "b", "c", "d")


print("\n" + "=" * 60)
print("EXAMPLE 4: **kwargs — Variable Keyword Arguments")
print("=" * 60)

def display_info(**details):
    """Print key-value pairs passed as keyword arguments."""
    print("  User details:")
    for key, value in details.items():
        print(f"    {key}: {value}")

display_info(name="Alice", age=21, major="Computer Science")
display_info(city="London", country="UK")

def build_query(table, **conditions):
    parts = [f"{k}={v!r}" for k, v in conditions.items()]
    where = " AND ".join(parts)
    return f"SELECT * FROM {table} WHERE {where}" if where else f"SELECT * FROM {table}"

print(build_query("students"))
print(build_query("students", name="Alice", active=True))


print("\n" + "=" * 60)
print("EXAMPLE 5: Mixed *args and **kwargs")
print("=" * 60)

def mixed(a, b, *args, sep=", ", **kwargs):
    """Demonstrate the full parameter ordering rules."""
    print(f"  a={a}, b={b}")
    print(f"  extra positional args: {args}")
    print(f"  sep={sep!r}")
    print(f"  extra keyword args: {kwargs}")

mixed(1, 2)
print()
mixed(1, 2, 3, 4, 5, sep=" | ", x=10, y=20)

# Unpacking into function calls with * and **
coords = (3, 4)
options = {"sep": " — ", "x": 99}
mixed(1, 2, *coords, **options)


print("\n" + "=" * 60)
print("EXAMPLE 6: Lambda Functions")
print("=" * 60)

square = lambda x: x ** 2
add_two = lambda a, b: a + b
clamp = lambda val, lo, hi: max(lo, min(val, hi))

print(square(7))           # 49
print(add_two(3, 4))       # 7
print(clamp(150, 0, 100))  # 100
print(clamp(-5, 0, 100))   # 0

words = ["banana", "apple", "cherry", "date", "elderberry"]
# Sort by length, then alphabetically
sorted_words = sorted(words, key=lambda w: (len(w), w))
print(sorted_words)

numbers = [1, -3, 2, -7, 4, -1]
# Use lambda with sorted to sort by absolute value
by_abs = sorted(numbers, key=lambda n: abs(n))
print(by_abs)   # [1, -1, 2, -3, 4, -7]


print("\n" + "=" * 60)
print("EXAMPLE 7: Decorators")
print("=" * 60)

import functools
import time

def timer(func):
    """Decorator that prints how long a function takes to run."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [{func.__name__}] took {elapsed:.6f}s")
        return result
    return wrapper

def logger(func):
    """Decorator that logs function calls and return values."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__}{args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} returned {result!r}")
        return result
    return wrapper

@timer
def slow_sum(n):
    """Sum integers from 0 to n-1."""
    return sum(range(n))

@logger
def multiply(a, b):
    return a * b

result = slow_sum(1_000_000)
print(f"  Result: {result}")

multiply(6, 7)

# Stacking decorators (applied bottom-up)
@timer
@logger
def compute(x):
    return x ** 3

compute(5)

# functools.wraps preserves metadata
print(f"  compute.__name__ = {compute.__name__}")


print("\n" + "=" * 60)
print("EXAMPLE 8: Recursive Functions")
print("=" * 60)

def factorial(n):
    """Return n! using recursion. Requires n >= 0."""
    if n < 0:
        raise ValueError("factorial undefined for negative numbers")
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case

def fibonacci(n):
    """Return the nth Fibonacci number (0-indexed). Requires n >= 0."""
    if n <= 1:          # base cases: fib(0)=0, fib(1)=1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(f"  factorial({i}) = {factorial(i)}")

print()
fib_sequence = [fibonacci(i) for i in range(10)]
print(f"  First 10 Fibonacci numbers: {fib_sequence}")

# Iterative vs recursive — same result:
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"  factorial(10) recursive  = {factorial(10)}")
print(f"  factorial(10) iterative  = {factorial_iterative(10)}")


print("\n" + "=" * 60)
print("EXAMPLE 9: Functions Returning Multiple Values")
print("=" * 60)

def statistics(numbers):
    """Return (minimum, maximum, mean) of a list of numbers."""
    if not numbers:
        raise ValueError("List must not be empty")
    total = sum(numbers)
    return min(numbers), max(numbers), total / len(numbers)

def divide_with_remainder(dividend, divisor):
    """Return (quotient, remainder) as a named tuple."""
    from collections import namedtuple
    DivResult = namedtuple("DivResult", ["quotient", "remainder"])
    return DivResult(dividend // divisor, dividend % divisor)

data = [4, 7, 2, 9, 1, 5, 8]
minimum, maximum, mean = statistics(data)
print(f"  min={minimum}, max={maximum}, mean={mean:.2f}")

result = divide_with_remainder(17, 5)
print(f"  17 ÷ 5 → quotient={result.quotient}, remainder={result.remainder}")

# Ignoring some return values with _
_, maximum, _ = statistics(data)
print(f"  (only captured max) max={maximum}")


print("\n" + "=" * 60)
print("EXAMPLE 10: Higher-Order Functions")
print("=" * 60)

def apply_twice(func, value):
    """Apply func to value, then apply func to the result."""
    return func(func(value))

def compose(*funcs):
    """Return a new function that applies funcs right-to-left."""
    def composed(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return composed

double   = lambda x: x * 2
add_ten  = lambda x: x + 10
to_str   = lambda x: f"result={x}"

print(apply_twice(double, 3))    # 12  (3*2=6, 6*2=12)
print(apply_twice(add_ten, 5))   # 25  (5+10=15, 15+10=25)

pipeline = compose(to_str, add_ten, double)
print(pipeline(3))               # result=16  (3*2=6, 6+10=16, "result=16")

# Built-in higher-order functions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares     = list(map(lambda x: x ** 2, nums))
evens       = list(filter(lambda x: x % 2 == 0, nums))
print(f"  squares: {squares}")
print(f"  evens:   {evens}")

from functools import reduce
product = reduce(lambda acc, x: acc * x, nums)
print(f"  product of 1..10: {product}")

# Passing named functions as arguments
def is_palindrome(s):
    return s == s[::-1]

words = ["racecar", "hello", "level", "world", "madam"]
palindromes = list(filter(is_palindrome, words))
print(f"  palindromes: {palindromes}")
