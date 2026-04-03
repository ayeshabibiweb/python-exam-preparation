"""
Topic 13: Advanced Python Concepts – Practice Problems
Each problem is stated as a comment followed by its full solution.
Run this file to verify all solutions produce the expected output.
"""

# ═══════════════════════════════════════════════════════════════
# Problem 1: Even Number Generator
# Write a generator function `evens_up_to(n)` that yields all
# even numbers from 0 up to (and including) n.
# Example: list(evens_up_to(10)) → [0, 2, 4, 6, 8, 10]
# ═══════════════════════════════════════════════════════════════
print("Problem 1: Even Number Generator")

def evens_up_to(n):
    for i in range(0, n + 1, 2):
        yield i

print(list(evens_up_to(10)))    # [0, 2, 4, 6, 8, 10]
print(list(evens_up_to(7)))     # [0, 2, 4, 6]


# ═══════════════════════════════════════════════════════════════
# Problem 2: Running Total Generator
# Write a generator `running_total(iterable)` that yields a
# cumulative sum as it processes each element.
# Example: list(running_total([1, 2, 3, 4])) → [1, 3, 6, 10]
# ═══════════════════════════════════════════════════════════════
print("\nProblem 2: Running Total Generator")

def running_total(iterable):
    total = 0
    for value in iterable:
        total += value
        yield total

print(list(running_total([1, 2, 3, 4])))      # [1, 3, 6, 10]
print(list(running_total([10, 5, 3, 2])))     # [10, 15, 18, 20]


# ═══════════════════════════════════════════════════════════════
# Problem 3: Infinite Geometric Sequence Generator
# Write a generator `geometric(first, ratio)` that yields
# an infinite geometric sequence: first, first*ratio, first*ratio^2, ...
# Use islice to print the first 6 terms of geometric(2, 3).
# Expected output: [2, 6, 18, 54, 162, 486]
# ═══════════════════════════════════════════════════════════════
print("\nProblem 3: Infinite Geometric Sequence Generator")

from itertools import islice

def geometric(first, ratio):
    value = first
    while True:
        yield value
        value *= ratio

terms = list(islice(geometric(2, 3), 6))
print(terms)   # [2, 6, 18, 54, 162, 486]


# ═══════════════════════════════════════════════════════════════
# Problem 4: Custom Reversed Iterator
# Implement a class `Reversed` that acts as an iterator yielding
# elements of a sequence in reverse order.
# Example: list(Reversed([1, 2, 3, 4])) → [4, 3, 2, 1]
# ═══════════════════════════════════════════════════════════════
print("\nProblem 4: Custom Reversed Iterator")

class Reversed:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.sequence[self.index]
        self.index -= 1
        return value

print(list(Reversed([1, 2, 3, 4])))        # [4, 3, 2, 1]
print(list(Reversed("hello")))             # ['o', 'l', 'l', 'e', 'h']


# ═══════════════════════════════════════════════════════════════
# Problem 5: Context Manager for Indented Printing
# Implement a context manager class `Indent` that increases
# the indentation level for any print statements within the block.
# Use a class with __enter__ and __exit__.
# ═══════════════════════════════════════════════════════════════
print("\nProblem 5: Context Manager for Indented Printing")

class Indent:
    _level = 0
    _indent = "  "

    def __enter__(self):
        Indent._level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        Indent._level -= 1
        return False

    @staticmethod
    def print(msg):
        print(Indent._indent * Indent._level + msg)

Indent.print("Top level")
with Indent():
    Indent.print("Level 1")
    with Indent():
        Indent.print("Level 2")
    Indent.print("Back to level 1")
Indent.print("Top level again")


# ═══════════════════════════════════════════════════════════════
# Problem 6: Memoization Closure
# Write a function `make_memoized(func)` that returns a new
# function with a cache. Repeated calls with the same argument
# return the cached value instead of recomputing.
# ═══════════════════════════════════════════════════════════════
print("\nProblem 6: Memoization Closure")

def make_memoized(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
            print(f"  [cache miss] computing {func.__name__}{args}")
        else:
            print(f"  [cache hit ] returning cached value for {args}")
        return cache[args]

    return wrapper

def slow_square(n):
    return n * n

memo_square = make_memoized(slow_square)
print(memo_square(4))   # cache miss → 16
print(memo_square(4))   # cache hit  → 16
print(memo_square(7))   # cache miss → 49


# ═══════════════════════════════════════════════════════════════
# Problem 7: Functional Pipeline with map, filter, reduce
# Given a list of product dictionaries with 'name' and 'price',
# compute the total price of products that cost more than $20,
# after applying a 10% discount to each.
# Use map, filter, and reduce — no loops.
# ═══════════════════════════════════════════════════════════════
print("\nProblem 7: Functional Pipeline with map/filter/reduce")

from functools import reduce

products = [
    {"name": "apple",  "price": 1.5},
    {"name": "laptop", "price": 999.99},
    {"name": "pen",    "price": 2.0},
    {"name": "phone",  "price": 499.99},
    {"name": "book",   "price": 25.0},
]

DISCOUNT = 0.10
THRESHOLD = 20.0

total = reduce(
    lambda acc, p: acc + p,
    map(
        lambda p: p["price"] * (1 - DISCOUNT),
        filter(lambda p: p["price"] > THRESHOLD, products)
    )
)

print(f"  Total after 10% discount (items > $20): ${total:.2f}")
# Expected: laptop(899.99) + phone(449.99) + book(22.50) = $1372.48


# ═══════════════════════════════════════════════════════════════
# Problem 8: Using partial to Create Specialised Functions
# Use functools.partial to create:
#   - `is_divisible_by_3`: returns True if n is divisible by 3
#   - `format_usd`: formats a number as "$X.XX"
# Then filter numbers 1-30 using is_divisible_by_3 and format them.
# ═══════════════════════════════════════════════════════════════
print("\nProblem 8: Partial Functions")

from functools import partial

def divisible_by(divisor, n):
    return n % divisor == 0

def format_currency(symbol, decimals, value):
    return f"{symbol}{value:.{decimals}f}"

is_divisible_by_3 = partial(divisible_by, 3)
format_usd = partial(format_currency, "$", 2)

multiples_of_3 = list(filter(is_divisible_by_3, range(1, 31)))
print(f"  Multiples of 3 (1-30): {multiples_of_3}")

prices = [9.5, 14.0, 3.99, 100.0]
formatted = list(map(format_usd, prices))
print(f"  Formatted prices: {formatted}")


# ═══════════════════════════════════════════════════════════════
# Problem 9: Generator-Based File Line Reader
# Write a generator `read_lines(text)` that takes a multi-line
# string and yields each non-empty line stripped of whitespace.
# ═══════════════════════════════════════════════════════════════
print("\nProblem 9: Generator-Based Line Reader")

def read_lines(text):
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            yield stripped

sample_text = """
    Hello World
    
    Python is great
    
    Generator example
"""

for line in read_lines(sample_text):
    print(f"  → {line}")


# ═══════════════════════════════════════════════════════════════
# Problem 10: Zip-Based Data Merging
# Given two lists — `names` (strings) and `scores` (lists of ints),
# use zip to pair them, then use a generator expression to produce
# a list of dicts: {"name": ..., "average": ...} sorted by average
# descending.
# ═══════════════════════════════════════════════════════════════
print("\nProblem 10: Zip-Based Data Merging")

names  = ["Alice", "Bob", "Charlie", "Diana"]
scores = [[88, 92, 95], [70, 65, 80], [91, 89, 94], [60, 75, 70]]

records = [
    {"name": name, "average": sum(s) / len(s)}
    for name, s in zip(names, scores)
]

ranked = sorted(records, key=lambda r: r["average"], reverse=True)

print("  Ranking:")
for i, student in enumerate(ranked, 1):
    print(f"    {i}. {student['name']}: {student['average']:.1f}")
