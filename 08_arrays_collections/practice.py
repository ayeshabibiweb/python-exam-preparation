# 08 – Arrays & Collections: Practice Problems
# Each problem states the task as a comment, followed by the full solution.
# Run this file: python practice.py

from collections import namedtuple, defaultdict, Counter

print("=" * 60)
print("PROBLEM 1: List Rotation")
print("=" * 60)
# Write a function rotate(lst, k) that rotates a list to the right
# by k positions without using collections.deque.
# rotate([1,2,3,4,5], 2) → [4, 5, 1, 2, 3]
# Handle k larger than len(lst) and negative k (left rotation).

def rotate(lst, k):
    if not lst:
        return lst[:]
    n = len(lst)
    k = k % n           # normalise: handle k > n and k < 0
    return lst[-k:] + lst[:-k] if k else lst[:]

tests = [
    ([1, 2, 3, 4, 5], 2,   [4, 5, 1, 2, 3]),
    ([1, 2, 3, 4, 5], 0,   [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 7,   [4, 5, 1, 2, 3]),  # k > len
    ([1, 2, 3, 4, 5], -1,  [2, 3, 4, 5, 1]),  # left rotate
    ([1],             3,   [1]),
]
for lst, k, expected in tests:
    result = rotate(lst, k)
    ok = "✓" if result == expected else "✗"
    print(f"  {ok} rotate({lst}, {k:+d}) = {result}")


print("\n" + "=" * 60)
print("PROBLEM 2: Frequency Counter with defaultdict")
print("=" * 60)
# Write a function count_frequencies(items) that returns a dict
# mapping each item to how many times it appears, using defaultdict.
# Then write top_n(freq_dict, n) that returns the n most common
# items as a list of (item, count) tuples, sorted by count descending.

def count_frequencies(items):
    freq = defaultdict(int)
    for item in items:
        freq[item] += 1
    return dict(freq)

def top_n(freq_dict, n):
    return sorted(freq_dict.items(), key=lambda kv: kv[1], reverse=True)[:n]

votes = ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice", "Dave", "Bob", "Alice"]
freq  = count_frequencies(votes)
print(f"  Frequencies: {freq}")
print(f"  Top 3:")
for name, count in top_n(freq, 3):
    print(f"    {name}: {count} vote(s)")


print("\n" + "=" * 60)
print("PROBLEM 3: Set Operations — Common and Unique")
print("=" * 60)
# Given three sets of student IDs enrolled in three courses,
# find:
# (a) Students in ALL three courses
# (b) Students in EXACTLY one course
# (c) Students in course A but NOT in B or C
# (d) Students in any course (union)

cs101 = {101, 102, 103, 104, 105, 106}
cs201 = {103, 104, 107, 108, 109}
cs301 = {104, 106, 109, 110, 111}

in_all    = cs101 & cs201 & cs301
in_any    = cs101 | cs201 | cs301
only_one  = set()
for sid in in_any:
    courses = sum([sid in cs101, sid in cs201, sid in cs301])
    if courses == 1:
        only_one.add(sid)
a_not_bc  = cs101 - cs201 - cs301

print(f"  In all three courses     : {sorted(in_all)}")
print(f"  In exactly one course    : {sorted(only_one)}")
print(f"  In CS101 only (not B/C)  : {sorted(a_not_bc)}")
print(f"  In any course (union)    : {sorted(in_any)}")


print("\n" + "=" * 60)
print("PROBLEM 4: Dictionary Merging and Updating")
print("=" * 60)
# Write a function deep_merge(base, overrides) that merges two dicts.
# If a key exists in both and both values are dicts, merge recursively.
# Otherwise, override's value wins.
# Demonstrate with a config merging use case.

def deep_merge(base, overrides):
    result = dict(base)
    for key, value in overrides.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

defaults = {
    "debug": False,
    "database": {"host": "localhost", "port": 5432, "name": "app"},
    "cache": {"ttl": 300, "max_size": 1000},
}
user_config = {
    "debug": True,
    "database": {"name": "myapp_prod", "db_pass": "secret"},
    "logging": {"level": "INFO"},
}

merged = deep_merge(defaults, user_config)
print(f"  debug              : {merged['debug']}")
print(f"  database.host      : {merged['database']['host']}")    # kept from defaults
print(f"  database.name      : {merged['database']['name']}")    # overridden
print(f"  database.db_pass    : {merged['database']['db_pass']}")  # new from user
print(f"  cache.ttl          : {merged['cache']['ttl']}")        # kept from defaults
print(f"  logging.level      : {merged['logging']['level']}")    # new section


print("\n" + "=" * 60)
print("PROBLEM 5: List Comprehension Challenges")
print("=" * 60)
# Solve the following using list comprehensions (no explicit loops):
# (a) Generate all Pythagorean triples (a, b, c) where a < b < c <= 30
# (b) Create a multiplication table as a list of lists (1-5 x 1-5)
# (c) Given a list of sentences, extract all words longer than 4 chars,
#     lowercased and deduplicated, sorted alphabetically.

# (a) Pythagorean triples
triples = [
    (a, b, c)
    for c in range(1, 31)
    for b in range(1, c)
    for a in range(1, b)
    if a**2 + b**2 == c**2
]
print(f"  Pythagorean triples (c≤30): {triples}")

# (b) Multiplication table
mul_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(f"  Multiplication table 5×5:")
for row in mul_table:
    print(f"    {row}")

# (c) Long unique words
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and flexible programming language.",
    "Learning programming requires practice and patience.",
]
long_words = sorted({
    word.strip(".,!?").lower()
    for sentence in sentences
    for word in sentence.split()
    if len(word.strip(".,!?")) > 4
})
print(f"  Long unique words: {long_words}")


print("\n" + "=" * 60)
print("PROBLEM 6: Dict Comprehension — Inventory Management")
print("=" * 60)
# Given a list of transaction tuples (item, quantity_change),
# build a running inventory dict.  Positive quantities are
# stock additions; negative are sales.  Filter out items with
# zero or negative stock at the end.
# Use a dict comprehension (or combination with grouping) to build
# the final inventory.

transactions = [
    ("apples",  100), ("bananas",  80),  ("apples",  -30),
    ("cherries", 50), ("bananas",  -90), ("dates",    40),
    ("apples",   20), ("cherries", -50), ("dates",    -5),
    ("elderberry", 10),
]

# Step 1: accumulate with a plain dict (comprehensions alone can't accumulate)
stock = {}
for item, qty in transactions:
    stock[item] = stock.get(item, 0) + qty

# Step 2: dict comprehension to filter and format
final_inventory = {item: qty for item, qty in stock.items() if qty > 0}
print(f"  Raw stock   : {stock}")
print(f"  Final stock (positive only): {final_inventory}")

# Bonus: sorted by quantity descending
ranked = dict(sorted(final_inventory.items(), key=lambda kv: kv[1], reverse=True))
print(f"  Ranked      : {ranked}")


print("\n" + "=" * 60)
print("PROBLEM 7: Named Tuple — Student Records")
print("=" * 60)
# Define a named tuple Student with fields: name, year, gpa, courses.
# Create several student records.
# Write a function honour_roll(students, min_gpa=3.7) that returns
# a sorted list (by gpa descending) of students on the honour roll.
# Write class_summary(students) that returns a dict with
# average gpa and total unique courses across all students.

Student = namedtuple("Student", ["name", "year", "gpa", "courses"])

roster = [
    Student("Alice",  3, 3.92, ["CS301", "CS401", "MATH301"]),
    Student("Bob",    1, 2.85, ["CS101", "MATH101"]),
    Student("Carol",  2, 3.75, ["CS201", "CS202", "PHYS201"]),
    Student("Dave",   4, 3.68, ["CS401", "CS410", "CS420"]),
    Student("Eve",    2, 3.50, ["CS201", "CS202"]),
    Student("Frank",  3, 3.88, ["CS301", "CS302", "CS401"]),
]

def honour_roll(students, min_gpa=3.7):
    eligible = [s for s in students if s.gpa >= min_gpa]
    return sorted(eligible, key=lambda s: s.gpa, reverse=True)

def class_summary(students):
    avg_gpa = sum(s.gpa for s in students) / len(students)
    all_courses = {c for s in students for c in s.courses}
    return {
        "average_gpa":    round(avg_gpa, 3),
        "unique_courses": len(all_courses),
        "courses":        sorted(all_courses),
    }

print("  Honour Roll (GPA ≥ 3.7):")
for s in honour_roll(roster):
    print(f"    {s.name:<8} Year {s.year}  GPA {s.gpa:.2f}")

summary = class_summary(roster)
print(f"\n  Average GPA   : {summary['average_gpa']}")
print(f"  Unique courses: {summary['unique_courses']}")
print(f"  Courses       : {summary['courses']}")


print("\n" + "=" * 60)
print("PROBLEM 8: Choosing the Right Collection")
print("=" * 60)
# Demonstrate appropriate collection choices for three scenarios:
#
# (a) WORD COUNTER: Count how many times each word appears in text.
#     → dict (or Counter) — key/value store with O(1) lookup
#
# (b) UNIQUE VISITORS: Track whether a user has visited before.
#     Given a stream of user_ids, find unique visitors and
#     duplicates efficiently.
#     → set — O(1) membership, automatic deduplication
#
# (c) ORDERED HISTORY: Keep the last 5 commands a user ran,
#     preserving order and allowing duplicates.
#     → list — ordered, supports duplicates, easy slicing

# (a) Word counter using Counter
from collections import Counter

text = ("the cat sat on the mat the cat in the hat "
        "the cat sat the mat sat")
word_count = Counter(text.split())
print("  (a) Word counts (top 5):")
for word, count in word_count.most_common(5):
    print(f"      {word!r:8}: {count}")

# (b) Unique visitors
visitor_stream = [101, 202, 101, 303, 202, 404, 101, 505, 303, 606]
seen       = set()
duplicates = set()
for uid in visitor_stream:
    if uid in seen:
        duplicates.add(uid)
    else:
        seen.add(uid)
print(f"\n  (b) Unique visitors : {len(seen)}  → {sorted(seen)}")
print(f"      Repeat visitors : {sorted(duplicates)}")

# (c) Command history — keep last N
MAX_HISTORY = 5
history = []
commands = ["ls", "cd ~", "pwd", "ls -la", "cat file.txt", "grep hello file.txt", "exit"]
for cmd in commands:
    history.append(cmd)
    history = history[-MAX_HISTORY:]   # keep last 5
print(f"\n  (c) Command history (last {MAX_HISTORY}):")
for i, cmd in enumerate(history, 1):
    print(f"      {i}. {cmd}")
