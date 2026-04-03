"""
Topic 04 — Control Structures: Examples
========================================
Run this file to see all examples execute in sequence.
    python 04_control_structures/examples.py
"""

import sys

# ===========================================================================
# Example 1: if / elif / else
# Python evaluates conditions top-to-bottom and runs the FIRST matching block.
# ===========================================================================
print("=" * 50)
print("Example 1: if / elif / else")
print("=" * 50)

def classify_score(score):
    """Return a letter grade for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for s in [95, 83, 72, 64, 55]:
    print(f"  Score {s}: Grade {classify_score(s)}")


# ===========================================================================
# Example 2: Ternary (Conditional) Expression
# value_if_true if condition else value_if_false
# ===========================================================================
print("\nExample 2: Ternary Expression")
print("-" * 40)

for n in range(-3, 4):
    label = "positive" if n > 0 else "negative" if n < 0 else "zero"
    print(f"  {n:2d} → {label}")


# ===========================================================================
# Example 3: for Loop with range()
# range(start, stop, step) — stop is exclusive.
# ===========================================================================
print("\nExample 3: for Loop with range()")
print("-" * 40)

# Count up
print("  Counting up (0–4):  ", end="")
for i in range(5):
    print(i, end=" ")
print()

# Count down
print("  Counting down (5–1):", end="")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Even numbers
print("  Even 0–18:          ", end="")
for i in range(0, 20, 2):
    print(i, end=" ")
print()

# Sum using range
total = sum(range(1, 101))   # sum of 1..100
print(f"\n  Sum 1 to 100 = {total}")


# ===========================================================================
# Example 4: for Loop with enumerate() and zip()
# enumerate() gives (index, value); zip() pairs up multiple iterables.
# ===========================================================================
print("\nExample 4: enumerate() and zip()")
print("-" * 40)

fruits = ["apple", "banana", "cherry"]
prices = [1.20, 0.50, 2.00]

print("  enumerate():")
for i, fruit in enumerate(fruits, start=1):   # start=1 begins numbering at 1
    print(f"    {i}. {fruit}")

print("  zip():")
for fruit, price in zip(fruits, prices):
    print(f"    {fruit:<10} £{price:.2f}")


# ===========================================================================
# Example 5: while Loop
# Continues as long as the condition is True. Needs a termination path.
# ===========================================================================
print("\nExample 5: while Loop")
print("-" * 40)

# Classic counter-controlled while
n = 1
print("  Powers of 2 under 1000:", end="")
while n < 1000:
    print(n, end=" ")
    n *= 2
print()

# Sentinel-controlled: stop when a condition is met
x = 100
steps = 0
print(f"\n  Collatz from {x}:", end=" ")
while x != 1:
    print(x, end=" ")
    x = x // 2 if x % 2 == 0 else 3 * x + 1
    steps += 1
print(f"1  ({steps} steps)")


# ===========================================================================
# Example 6: break and continue
# break exits the innermost loop; continue skips to the next iteration.
# ===========================================================================
print("\nExample 6: break and continue")
print("-" * 40)

# break: find the first negative number in a list
numbers = [4, 7, 2, -3, 8, -1, 5]
print("  Searching for first negative:")
for num in numbers:
    if num < 0:
        print(f"  Found: {num}")
        break
    print(f"  Checked {num} (positive)")

# continue: print only odd numbers
print("\n  Odd numbers 1-10:", end=" ")
for i in range(1, 11):
    if i % 2 == 0:
        continue    # skip evens
    print(i, end=" ")
print()


# ===========================================================================
# Example 7: Loop else Clause
# else runs when the loop finishes WITHOUT hitting a break.
# ===========================================================================
print("\nExample 7: Loop else Clause")
print("-" * 40)

def find_prime_factor(n):
    """Return the smallest prime factor of n, or None if n is prime."""
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return divisor
    else:
        # No divisor found — n is prime
        return None

for num in [17, 24, 37, 100]:
    factor = find_prime_factor(num)
    if factor is None:
        print(f"  {num:3d} is prime")
    else:
        print(f"  {num:3d} = {factor} × {num // factor}")


# ===========================================================================
# Example 8: Nested Loops
# The inner loop fully completes for each iteration of the outer loop.
# ===========================================================================
print("\nExample 8: Nested Loops")
print("-" * 40)

# Multiplication table (partial)
print("  Multiplication table (3×3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i}×{j}={i*j}", end="  ")
    print()   # newline after each row

# Triangle pattern
print("\n  Triangle pattern (5 rows):")
for row in range(1, 6):
    print("  " + "*" * row)


# ===========================================================================
# Example 9: pass Statement
# A syntactic placeholder — does nothing, allows empty blocks.
# ===========================================================================
print("\nExample 9: pass Statement")
print("-" * 40)

def not_implemented_yet():
    pass   # function body required — pass is the placeholder

class EmptyClass:
    pass   # class body required

for i in range(5):
    if i == 3:
        pass   # TODO: handle case 3
    else:
        print(f"  i = {i}")


# ===========================================================================
# Example 10: match Statement (Python 3.10+)
# Structural pattern matching — like a powerful switch/case.
# ===========================================================================
print("\nExample 10: match Statement (Python 3.10+)")
print("-" * 40)

# Guard against running on older Python
if sys.version_info >= (3, 10):
    def http_status(code):
        match code:
            case 200:
                return "OK"
            case 301 | 302:
                return "Redirect"
            case 404:
                return "Not Found"
            case 500:
                return "Server Error"
            case int(c) if 400 <= c < 500:
                return f"Client Error ({c})"
            case _:
                return "Unknown"

    for code in [200, 301, 404, 418, 500, 503]:
        print(f"  HTTP {code}: {http_status(code)}")
else:
    # Equivalent using if/elif for older Python versions
    def http_status_compat(code):
        if code == 200:
            return "OK"
        elif code in (301, 302):
            return "Redirect"
        elif code == 404:
            return "Not Found"
        elif code == 500:
            return "Server Error"
        elif 400 <= code < 500:
            return f"Client Error ({code})"
        else:
            return "Unknown"

    for code in [200, 301, 404, 418, 500, 503]:
        print(f"  HTTP {code}: {http_status_compat(code)}")
    print("  (match statement requires Python 3.10+)")

print("\nAll examples complete.")
