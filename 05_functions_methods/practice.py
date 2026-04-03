# 05 – Functions & Methods: Practice Problems
# Each problem states the task as a comment, followed by the full solution.
# Run this file: python practice.py

print("=" * 60)
print("PROBLEM 1: Temperature Converter")
print("=" * 60)
# Write a function celsius_to_fahrenheit(c) that converts Celsius to
# Fahrenheit using the formula F = (C * 9/5) + 32.
# Then write fahrenheit_to_celsius(f) for the reverse.
# Finally, write convert(value, unit) where unit is "C" or "F"
# and it dispatches to the correct function.

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def convert(value, unit):
    if unit.upper() == "C":
        return celsius_to_fahrenheit(value)
    elif unit.upper() == "F":
        return fahrenheit_to_celsius(value)
    else:
        raise ValueError(f"Unknown unit: {unit!r}. Use 'C' or 'F'.")

print(celsius_to_fahrenheit(0))     # 32.0
print(celsius_to_fahrenheit(100))   # 212.0
print(fahrenheit_to_celsius(32))    # 0.0
print(fahrenheit_to_celsius(212))   # 100.0
print(f"convert(37, 'C') = {convert(37, 'C'):.2f}°F")
print(f"convert(98.6, 'F') = {convert(98.6, 'F'):.2f}°C")


print("\n" + "=" * 60)
print("PROBLEM 2: Flexible String Joiner with *args")
print("=" * 60)
# Write a function join_strings(*words, separator=", ", prefix="",
# suffix="") that joins all positional string arguments with the
# given separator, and wraps the result in prefix/suffix.
# Example: join_strings("a","b","c", separator="-", prefix="[", suffix="]")
#          should return "[a-b-c]"

def join_strings(*words, separator=", ", prefix="", suffix=""):
    return prefix + separator.join(words) + suffix

print(join_strings("apple", "banana", "cherry"))
print(join_strings("a", "b", "c", separator="-", prefix="[", suffix="]"))
print(join_strings("hello", "world", separator=" "))
print(join_strings("solo", prefix="(", suffix=")"))


print("\n" + "=" * 60)
print("PROBLEM 3: Profile Builder with **kwargs")
print("=" * 60)
# Write a function build_profile(first_name, last_name, **extra)
# that returns a dictionary containing first_name and last_name
# plus any additional keyword arguments.
# Ensure first_name and last_name keys are always present even if
# extra provides conflicting keys (first/last take priority).

def build_profile(first_name, last_name, **extra):
    profile = dict(extra)                 # start with extras
    profile["first_name"] = first_name   # these always win
    profile["last_name"] = last_name
    return profile

p1 = build_profile("Alice", "Smith", age=21, major="CS")
p2 = build_profile("Bob", "Jones", city="London", active=True)
print(p1)
print(p2)


print("\n" + "=" * 60)
print("PROBLEM 4: Memoization Decorator")
print("=" * 60)
# Write a decorator called memoize that caches the results of a
# function call keyed by its arguments.  If the same arguments are
# passed again, return the cached result instead of recomputing.
# Apply it to a slow_fibonacci function and verify that repeated
# calls with the same argument only compute once.

import functools

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache   # expose cache for inspection
    return wrapper

@memoize
def slow_fibonacci(n):
    """Compute nth Fibonacci number (inefficient recursive version)."""
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

for i in range(10):
    print(f"  fib({i}) = {slow_fibonacci(i)}")

print(f"  Cache size after computing fib(0..9): {len(slow_fibonacci.cache)}")


print("\n" + "=" * 60)
print("PROBLEM 5: Recursive Sum of Nested List")
print("=" * 60)
# Write a recursive function flatten_sum(data) that accepts a
# list which may contain integers OR nested lists of integers
# (any depth) and returns the total sum of all integers.
# Example: flatten_sum([1, [2, [3, 4]], 5]) → 15

def flatten_sum(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += flatten_sum(item)   # recurse into sublists
        else:
            total += item
    return total

print(flatten_sum([1, 2, 3]))                        # 6
print(flatten_sum([1, [2, 3], [4, [5, 6]]]))         # 21
print(flatten_sum([1, [2, [3, [4, [5]]]]]))           # 15
print(flatten_sum([]))                                # 0


print("\n" + "=" * 60)
print("PROBLEM 6: Lambda-Powered Sorting and Filtering")
print("=" * 60)
# Given a list of student dictionaries, each with keys "name",
# "grade" (0-100), and "year" (1-4):
# (a) Sort by grade descending.
# (b) Filter to keep only students with grade >= 60.
# (c) Sort passing students by year ascending, then grade descending.
# Use lambdas for all key/filter functions.

students = [
    {"name": "Alice",   "grade": 88, "year": 2},
    {"name": "Bob",     "grade": 45, "year": 1},
    {"name": "Carol",   "grade": 73, "year": 3},
    {"name": "Dave",    "grade": 60, "year": 2},
    {"name": "Eve",     "grade": 91, "year": 1},
    {"name": "Frank",   "grade": 55, "year": 4},
]

# (a) Sort by grade descending
by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print("By grade (desc):", [s["name"] for s in by_grade])

# (b) Filter passing students
passing = list(filter(lambda s: s["grade"] >= 60, students))
print("Passing:", [s["name"] for s in passing])

# (c) Sort passing by year asc, then grade desc
sorted_passing = sorted(passing, key=lambda s: (s["year"], -s["grade"]))
print("Sorted passing:", [(s["name"], s["year"], s["grade"]) for s in sorted_passing])


print("\n" + "=" * 60)
print("PROBLEM 7: Closure — Counter Factory")
print("=" * 60)
# Write a function make_counter(start=0, step=1) that returns a
# closure. Each time the returned function is called, it increments
# an internal counter by step and returns the new value.
# The closure should also support a reset() method that sets the
# counter back to start.

def make_counter(start=0, step=1):
    count = [start]   # list so nonlocal-style mutation works easily

    def counter():
        count[0] += step
        return count[0]

    def reset():
        count[0] = start

    counter.reset = reset   # attach reset as attribute
    return counter

c = make_counter()
print(c(), c(), c())      # 1 2 3
c.reset()
print(c())                # 1

c2 = make_counter(start=10, step=5)
print(c2(), c2(), c2())   # 15 20 25


print("\n" + "=" * 60)
print("PROBLEM 8: Function that Validates Input")
print("=" * 60)
# Write a decorator validate_positive that raises a ValueError
# if any positional argument passed to the decorated function
# is not a positive number (> 0).
# Apply it to a compute_area(width, height) function.

def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i, arg in enumerate(args):
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(
                    f"Argument {i} ({arg!r}) must be a positive number."
                )
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def compute_area(width, height):
    return width * height

print(compute_area(5, 3))    # 15
print(compute_area(2.5, 4))  # 10.0

try:
    compute_area(-1, 5)
except ValueError as e:
    print(f"Caught: {e}")

try:
    compute_area(0, 5)
except ValueError as e:
    print(f"Caught: {e}")


print("\n" + "=" * 60)
print("PROBLEM 9: Recursive Power Without ** Operator")
print("=" * 60)
# Write a recursive function recursive_power(base, exp) that
# computes base^exp for non-negative integer exponents without
# using the ** operator or math.pow.
# Optimise using fast exponentiation (also called exponentiation
# by squaring): if exp is even, power(base, exp) = power(base*base, exp//2).

def recursive_power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = recursive_power(base, exp // 2)
        return half * half
    return base * recursive_power(base, exp - 1)

test_cases = [(2, 10), (3, 5), (5, 0), (7, 1), (2, 16)]
for b, e in test_cases:
    computed = recursive_power(b, e)
    expected = b ** e
    status = "✓" if computed == expected else "✗"
    print(f"  {status} recursive_power({b}, {e}) = {computed}  (expected {expected})")


print("\n" + "=" * 60)
print("PROBLEM 10: Higher-Order — Pipeline Builder")
print("=" * 60)
# Write a function pipeline(*funcs) that returns a new function.
# When the returned function is called with a value, it applies
# each function in funcs left-to-right (like a unix pipe).
# Example: pipeline(double, add_one, square)(3)
#          → square(add_one(double(3))) = square(add_one(6)) = square(7) = 49

def pipeline(*funcs):
    def run(value):
        result = value
        for f in funcs:
            result = f(result)
        return result
    return run

double   = lambda x: x * 2
add_one  = lambda x: x + 1
square   = lambda x: x ** 2
to_str   = lambda x: f"answer={x}"

p1 = pipeline(double, add_one, square)
print(p1(3))   # 49    (3→6→7→49)
print(p1(0))   # 1     (0→0→1→1)

p2 = pipeline(square, double, to_str)
print(p2(4))   # answer=32   (4→16→32→"answer=32")

# Empty pipeline should be identity
identity = pipeline()
print(identity(42))   # 42
