"""
Topic 02 — Data Types and Variables: Practice Problems
======================================================
Attempt each problem yourself before reading the solution.
    python 02_data_types_variables/practice.py
"""

print("=" * 60)
print("Topic 02 — Practice Problems")
print("=" * 60)

# ===========================================================================
# Problem 1: Type Identification
# ---------------------------------
# Without running code, predict the type of each expression:
#   10 / 2, 10 // 2, 10 % 3, True + 3, None, "42", int("42"), 0.0
# Then print each value and its type to verify.
# ===========================================================================
print("\n--- Problem 1: Type Identification ---")

# SOLUTION
expressions = [
    ("10 / 2",    10 / 2),
    ("10 // 2",   10 // 2),
    ("10 % 3",    10 % 3),
    ("True + 3",  True + 3),
    ("None",      None),
    ('"42"',      "42"),
    ('int("42")', int("42")),
    ("0.0",       0.0),
]
for label, val in expressions:
    print(f"  {label:<14} → {str(val):<10} type: {type(val).__name__}")


# ===========================================================================
# Problem 2: Safe Type Conversion
# ---------------------------------
# Write a function safe_int(value) that attempts to convert value to int.
# If the conversion fails (ValueError), return 0 instead.
# Test with: "123", "abc", 3.7, True, None
# ===========================================================================
print("\n--- Problem 2: Safe Type Conversion ---")

# SOLUTION
def safe_int(value):
    """Convert value to int; return 0 if conversion fails."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0

test_values = ["123", "abc", 3.7, True, None]
for v in test_values:
    print(f"  safe_int({v!r:<8}) = {safe_int(v)}")


# ===========================================================================
# Problem 3: Truthiness Table
# -----------------------------
# Print a truthiness table for:
#   0, 1, -1, 0.0, 0.1, "", "0", "False", [], [0], {}, None, True, False
# Show the value and its boolean equivalent.
# ===========================================================================
print("\n--- Problem 3: Truthiness Table ---")

# SOLUTION
candidates = [0, 1, -1, 0.0, 0.1, "", "0", "False", [], [0], {}, None, True, False]
print(f"  {'Value':<12} {'bool()'}")
print(f"  {'-'*12} {'-'*6}")
for val in candidates:
    print(f"  {val!r:<12} {bool(val)}")


# ===========================================================================
# Problem 4: Scope Puzzle
# -----------------------
# Predict the output of this code before running it:
#
#   x = "global"
#
#   def outer():
#       x = "outer"
#       def inner():
#           print(x)    # which x?
#       inner()
#       print(x)
#
#   outer()
#   print(x)
#
# Then implement it and verify.
# ===========================================================================
print("\n--- Problem 4: Scope Puzzle ---")

# SOLUTION
# inner() has no local x, so it looks in the enclosing scope (outer's x = "outer")
# outer() prints its own local x = "outer"
# The global print sees the global x = "global"

x = "global"

def outer():
    x = "outer"
    def inner():
        print(f"  inner sees:  {x}")   # "outer" (enclosing scope)
    inner()
    print(f"  outer sees:  {x}")       # "outer" (local)

outer()
print(f"  global sees: {x}")           # "global"


# ===========================================================================
# Problem 5: Global Keyword
# --------------------------
# Write a function reset_counter() that sets a global variable `counter`
# to 0, and increment_counter() that adds 1 to it.
# Start counter at 5, call increment three times, reset, increment once.
# Print the counter value after each operation.
# ===========================================================================
print("\n--- Problem 5: Global Keyword ---")

# SOLUTION
counter = 5

def reset_counter():
    global counter
    counter = 0

def increment_counter():
    global counter
    counter += 1

print(f"  Start:       counter = {counter}")
increment_counter(); print(f"  After +1:    counter = {counter}")
increment_counter(); print(f"  After +1:    counter = {counter}")
increment_counter(); print(f"  After +1:    counter = {counter}")
reset_counter();     print(f"  After reset: counter = {counter}")
increment_counter(); print(f"  After +1:    counter = {counter}")


# ===========================================================================
# Problem 6: Nonlocal Accumulator
# --------------------------------
# Create a function make_accumulator() that returns a function add(n).
# Each call to add(n) adds n to a running total stored in the enclosing scope
# and returns the new total.
# Test: add(10), add(5), add(-3) should return 10, 15, 12.
# ===========================================================================
print("\n--- Problem 6: Nonlocal Accumulator ---")

# SOLUTION
def make_accumulator():
    total = 0
    def add(n):
        nonlocal total
        total += n
        return total
    return add

add = make_accumulator()
print(f"  add(10) = {add(10)}")   # 10
print(f"  add(5)  = {add(5)}")    # 15
print(f"  add(-3) = {add(-3)}")   # 12


# ===========================================================================
# Problem 7: Float Comparison Fix
# --------------------------------
# The following comparison is broken due to float precision:
#   (0.1 + 0.2 + 0.3) == 0.6  →  False
# Fix it using math.isclose(), then write your own comparison using a
# tolerance of 1e-9.
# ===========================================================================
print("\n--- Problem 7: Float Comparison Fix ---")

# SOLUTION
import math

a = 0.1 + 0.2 + 0.3
b = 0.6

print(f"  Raw: {a}")
print(f"  a == b:             {a == b}")                      # False
print(f"  math.isclose():     {math.isclose(a, b)}")          # True
print(f"  Manual tolerance:   {abs(a - b) < 1e-9}")           # True


# ===========================================================================
# Problem 8: Mutable Default Argument Bug
# ----------------------------------------
# The following function has a classic Python bug. Identify it, explain it,
# and fix it.
#
#   def add_item(item, container=[]):
#       container.append(item)
#       return container
#
# Expected: each call with no container gives a fresh list.
# Actual:   the list persists across calls.
# ===========================================================================
print("\n--- Problem 8: Mutable Default Argument Bug ---")

# BUGGY version (demonstrating the problem)
def add_item_buggy(item, container=[]):
    container.append(item)
    return container

print("  Buggy version:")
print(f"    {add_item_buggy('a')}")   # ['a']
print(f"    {add_item_buggy('b')}")   # ['a', 'b']  ← BUG: shares the list!
print(f"    {add_item_buggy('c')}")   # ['a', 'b', 'c']

# FIXED version — use None as sentinel, create fresh list inside
def add_item_fixed(item, container=None):
    if container is None:
        container = []
    container.append(item)
    return container

print("  Fixed version:")
print(f"    {add_item_fixed('a')}")   # ['a']
print(f"    {add_item_fixed('b')}")   # ['b']  ← fresh list each time
print(f"    {add_item_fixed('c')}")   # ['c']


# ===========================================================================
# Problem 9: Type Hierarchy Explorer
# -------------------------------------
# Python's bool is a subclass of int.
# Write code that demonstrates this using isinstance() and type().
# Also show that None is the only instance of NoneType.
# ===========================================================================
print("\n--- Problem 9: Type Hierarchy ---")

# SOLUTION
print(f"  type(True)             = {type(True)}")
print(f"  isinstance(True, int)  = {isinstance(True, int)}")    # True
print(f"  isinstance(True, bool) = {isinstance(True, bool)}")   # True
print(f"  type(True) is bool     = {type(True) is bool}")        # True
print(f"  type(True) is int      = {type(True) is int}")         # False (exact type)

print()
print(f"  type(None)             = {type(None)}")
x = None
y = None
print(f"  x is y (both None):    {x is y}")   # True — None is a singleton


# ===========================================================================
# Problem 10: Variable Rebinding vs Mutation
# -------------------------------------------
# Predict whether b is affected in each scenario, then verify:
#
# Scenario A (immutable — int):
#   a = 5; b = a; a = 10  →  b = ?
#
# Scenario B (mutable — list):
#   a = [1,2,3]; b = a; a.append(4)  →  b = ?
#
# Scenario C (mutable, but rebind instead of mutate):
#   a = [1,2,3]; b = a; a = [1,2,3,4]  →  b = ?
# ===========================================================================
print("\n--- Problem 10: Rebinding vs Mutation ---")

# SOLUTION — Scenario A: immutable
a = 5
b = a
a = 10
print(f"  Scenario A — immutable int:")
print(f"    a={a}, b={b}  ← b unaffected (ints are immutable)")

# SOLUTION — Scenario B: mutate mutable object
a = [1, 2, 3]
b = a
a.append(4)
print(f"  Scenario B — mutable list, .append():")
print(f"    a={a}, b={b}  ← b IS affected (same object)")

# SOLUTION — Scenario C: rebind name to new object
a = [1, 2, 3]
b = a
a = [1, 2, 3, 4]   # a now points to a NEW list
print(f"  Scenario C — mutable list, reassigned:")
print(f"    a={a}, b={b}  ← b unaffected (a points to new object)")

print("\nAll practice problems complete.")
