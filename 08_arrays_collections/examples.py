# 08 – Arrays & Collections: Examples
# Run this file: python examples.py

from collections import namedtuple

print("=" * 60)
print("EXAMPLE 1: List Operations and Methods")
print("=" * 60)

fruits = ["cherry", "apple", "banana"]
print(f"  Initial list   : {fruits}")

fruits.append("date")
print(f"  After append   : {fruits}")

fruits.insert(1, "apricot")
print(f"  After insert(1): {fruits}")

fruits.extend(["elderberry", "fig"])
print(f"  After extend   : {fruits}")

fruits.remove("banana")
print(f"  After remove   : {fruits}")

popped = fruits.pop()
print(f"  pop() returned : {popped!r}, list = {fruits}")

popped2 = fruits.pop(1)
print(f"  pop(1) returned: {popped2!r}, list = {fruits}")

print(f"  count('apple') : {fruits.count('apple')}")
print(f"  index('apple') : {fruits.index('apple')}")

fruits.sort()
print(f"  After sort()   : {fruits}")

fruits.reverse()
print(f"  After reverse(): {fruits}")

copy = fruits.copy()
copy.clear()
print(f"  Original intact: {fruits}")
print(f"  Cleared copy   : {copy}")

# sorted() returns new list; sort() modifies in place
numbers = [5, 2, 8, 1, 9, 3]
print(f"  sorted(nums)   : {sorted(numbers)}")
print(f"  Original intact: {numbers}")
print(f"  sorted(reverse): {sorted(numbers, reverse=True)}")


print("\n" + "=" * 60)
print("EXAMPLE 2: List Slicing")
print("=" * 60)

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"  lst            : {lst}")
print(f"  lst[2:6]       : {lst[2:6]}")       # [2,3,4,5]
print(f"  lst[:4]        : {lst[:4]}")         # first 4
print(f"  lst[6:]        : {lst[6:]}")         # from index 6 to end
print(f"  lst[-3:]       : {lst[-3:]}")        # last 3
print(f"  lst[1:-1]      : {lst[1:-1]}")       # all but first and last
print(f"  lst[::2]       : {lst[::2]}")        # every 2nd
print(f"  lst[1::2]      : {lst[1::2]}")       # odd-index items
print(f"  lst[::-1]      : {lst[::-1]}")       # reverse

# Slice assignment
lst2 = [0, 1, 2, 3, 4]
lst2[1:3] = [10, 20, 30]    # replace 2 elements with 3
print(f"  slice assign   : {lst2}")

lst3 = [0, 1, 2, 3, 4]
lst3[::2] = [100, 200, 300] # replace every other element
print(f"  step assign    : {lst3}")


print("\n" + "=" * 60)
print("EXAMPLE 3: Tuple Creation and Use")
print("=" * 60)

# Basic tuple
point = (3, 4)
print(f"  point          : {point}")
print(f"  point[0]       : {point[0]}")
print(f"  len(point)     : {len(point)}")

# Single-element tuple requires trailing comma
single = (42,)
not_a_tuple = (42)   # just an int in parens
print(f"  single         : {single}, type={type(single).__name__}")
print(f"  not_a_tuple    : {not_a_tuple}, type={type(not_a_tuple).__name__}")

# Tuple unpacking
x, y = point
print(f"  unpacked x={x}, y={y}")

a, *middle, z = (1, 2, 3, 4, 5)
print(f"  a={a}, middle={middle}, z={z}")

# Named tuple
Color = namedtuple("Color", ["red", "green", "blue"])
white = Color(255, 255, 255)
navy  = Color(red=0, green=0, blue=128)
print(f"  white          : {white}")
print(f"  navy.blue      : {navy.blue}")
print(f"  navy[0]        : {navy[0]}")   # index access still works

# Tuple as dict key (hashable)
grid = {(0, 0): "start", (5, 5): "end"}
print(f"  grid[(0,0)]    : {grid[(0,0)]}")

# Tuple is faster than list for iteration
import timeit
list_time  = timeit.timeit("sum([1,2,3,4,5])", number=1_000_000)
tuple_time = timeit.timeit("sum((1,2,3,4,5))", number=1_000_000)
print(f"  sum list  (1M times): {list_time:.3f}s")
print(f"  sum tuple (1M times): {tuple_time:.3f}s")


print("\n" + "=" * 60)
print("EXAMPLE 4: Set Operations")
print("=" * 60)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(f"  a              : {sorted(a)}")
print(f"  b              : {sorted(b)}")

print(f"  union (|)      : {sorted(a | b)}")
print(f"  intersection(&): {sorted(a & b)}")
print(f"  difference (-)  : {sorted(a - b)}")   # in a but not b
print(f"  sym_diff (^)   : {sorted(a ^ b)}")    # in one but not both

# Membership test — O(1)
print(f"  3 in a         : {3 in a}")
print(f"  9 in a         : {9 in a}")

# Deduplicate a list using set
names = ["Alice", "Bob", "Alice", "Carol", "Bob", "Dave"]
unique = list(set(names))
print(f"  deduped names  : {sorted(unique)}")

# Subset / superset
c = {2, 4}
print(f"  c={c} <= a     : {c <= a}")    # c is subset of a
print(f"  a >= c         : {a >= c}")    # a is superset of c

# Mutable operations
s = {1, 2, 3}
s.add(4)
s.discard(2)    # safe remove (no error if absent)
s.discard(99)   # no error
print(f"  after add/discard: {sorted(s)}")

# frozenset — immutable set (can be used as dict key or set element)
fs = frozenset([1, 2, 3])
d = {fs: "a frozen set key"}
print(f"  frozenset as key: {d[fs]!r}")


print("\n" + "=" * 60)
print("EXAMPLE 5: Dictionary CRUD Operations")
print("=" * 60)

# Create
student = {"name": "Alice", "age": 21, "gpa": 3.8}
print(f"  Initial        : {student}")

# Create / Update
student["major"] = "Computer Science"   # add new key
student["age"] = 22                     # update existing
print(f"  After C/U      : {student}")

# Read
print(f"  name           : {student['name']}")
print(f"  phone (missing): {student.get('phone', 'N/A')}")

# Delete
del student["gpa"]
removed = student.pop("age", None)
print(f"  After deletes  : {student}")
print(f"  Removed age    : {removed}")

# Safe check before access
if "major" in student:
    print(f"  major exists   : {student['major']}")


print("\n" + "=" * 60)
print("EXAMPLE 6: Dictionary Methods")
print("=" * 60)

inventory = {"apples": 50, "bananas": 30, "cherries": 100}

# keys, values, items
print(f"  keys()   : {list(inventory.keys())}")
print(f"  values() : {list(inventory.values())}")
print(f"  items()  : {list(inventory.items())}")

# Iterate items (most common pattern)
print("  Iterating items:")
for fruit, qty in inventory.items():
    print(f"    {fruit:<10}: {qty}")

# update — merge dicts
restock = {"bananas": 60, "dates": 20}
inventory.update(restock)
print(f"  After update   : {inventory}")

# merge with | operator (Python 3.9+)
extra = {"elderberry": 15}
combined = inventory | extra
print(f"  | merge        : {combined}")

# setdefault — only sets if key is absent
inventory.setdefault("apples", 999)    # 'apples' already exists → no change
inventory.setdefault("figs", 10)       # new key added
print(f"  setdefault     : {inventory}")

# dict comprehension to build from two lists
keys   = ["a", "b", "c", "d"]
values = [1,   2,   3,   4  ]
paired = dict(zip(keys, values))
print(f"  zip→dict       : {paired}")


print("\n" + "=" * 60)
print("EXAMPLE 7: List Comprehension")
print("=" * 60)

# Basic: squares
squares = [x**2 for x in range(1, 11)]
print(f"  squares        : {squares}")

# With condition: even squares only
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"  even squares   : {even_squares}")

# Transform strings
words  = ["  hello  ", " WORLD ", "Python ", " Test"]
clean  = [w.strip().capitalize() for w in words]
print(f"  cleaned words  : {clean}")

# Nested comprehension — flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [n for row in matrix for n in row]
print(f"  flattened      : {flat}")

# Nested comprehension — transpose a matrix
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"  transposed     : {transposed}")

# Conditional expression (ternary) in comprehension
labels = ["pass" if x >= 50 else "fail" for x in [90, 45, 72, 30, 55]]
print(f"  pass/fail      : {labels}")


print("\n" + "=" * 60)
print("EXAMPLE 8: Dict Comprehension")
print("=" * 60)

# Word → length mapping
words = ["apple", "banana", "cherry", "date", "elderberry"]
word_len = {w: len(w) for w in words}
print(f"  word lengths   : {word_len}")

# Invert a mapping (assumes values are unique)
code_to_name = {1: "Alice", 2: "Bob", 3: "Carol"}
name_to_code = {v: k for k, v in code_to_name.items()}
print(f"  inverted       : {name_to_code}")

# Filter while transforming
scores = {"Alice": 92, "Bob": 45, "Carol": 78, "Dave": 33, "Eve": 88}
passing = {name: score for name, score in scores.items() if score >= 50}
print(f"  passing scores : {passing}")

# Nested dict comprehension
keys   = ["a", "b", "c"]
nested = {k: {i: i**2 for i in range(1, 4)} for k in keys}
print(f"  nested         : {nested}")


print("\n" + "=" * 60)
print("EXAMPLE 9: Set Comprehension")
print("=" * 60)

words = ["banana", "apple", "banana", "cherry", "apple", "date"]

# Unique word lengths
unique_lengths = {len(w) for w in words}
print(f"  unique lengths : {sorted(unique_lengths)}")

# Unique initial letters
initials = {w[0].upper() for w in words}
print(f"  initials       : {sorted(initials)}")

# Primes up to 30 using set comprehension
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

primes = {n for n in range(2, 31) if is_prime(n)}
print(f"  primes ≤ 30    : {sorted(primes)}")

# Find common characters between two strings (using set comprehension)
s1, s2 = "programming", "algorithm"
common = {c for c in s1 if c in s2}
print(f"  common chars   : {sorted(common)}")


print("\n" + "=" * 60)
print("EXAMPLE 10: Nested Structures Example")
print("=" * 60)

# Represent a university department
department = {
    "name": "Computer Science",
    "courses": [
        {"code": "CS101", "title": "Intro to Programming", "credits": 15, "enrolled": 120},
        {"code": "CS201", "title": "Data Structures",      "credits": 15, "enrolled": 85},
        {"code": "CS301", "title": "Algorithms",           "credits": 20, "enrolled": 60},
        {"code": "CS401", "title": "Machine Learning",     "credits": 20, "enrolled": 45},
    ],
    "staff": {"Alice Smith": "Professor", "Bob Jones": "Lecturer"},
}

# Query nested data
print(f"  Department: {department['name']}")
print(f"  Staff:")
for name, role in department["staff"].items():
    print(f"    {name} — {role}")

print(f"  Courses with ≥ 60 enrolled:")
popular = [c for c in department["courses"] if c["enrolled"] >= 60]
for c in popular:
    print(f"    {c['code']}: {c['title']} ({c['enrolled']} students)")

total_enrolled = sum(c["enrolled"] for c in department["courses"])
total_credits  = sum(c["credits"]  for c in department["courses"])
print(f"  Total enrolled  : {total_enrolled}")
print(f"  Total credits   : {total_credits}")

# Build lookup dict from list using dict comprehension
course_lookup = {c["code"]: c for c in department["courses"]}
print(f"  CS201 title     : {course_lookup['CS201']['title']}")
