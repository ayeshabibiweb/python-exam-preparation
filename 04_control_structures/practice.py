"""
Topic 04 — Control Structures: Practice Problems
=================================================
Attempt each problem yourself before reading the solution.
    python 04_control_structures/practice.py
"""

print("=" * 60)
print("Topic 04 — Practice Problems")
print("=" * 60)

# ===========================================================================
# Problem 1: FizzBuzz
# --------------------
# Print numbers 1 to 30.
# For multiples of 3 print "Fizz" instead of the number.
# For multiples of 5 print "Buzz".
# For multiples of both 3 AND 5 print "FizzBuzz".
# ===========================================================================
print("\n--- Problem 1: FizzBuzz ---")

# SOLUTION
for i in range(1, 31):
    if i % 15 == 0:        # check combined FIRST (before individual checks)
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()


# ===========================================================================
# Problem 2: Number Guessing Logic (Without User Input)
# -------------------------------------------------------
# Simulate a guessing game: secret = 42.
# Iterate through a list of guesses [10, 55, 42, 70] and for each:
#   - Print "Too low" if guess < secret
#   - Print "Too high" if guess > secret
#   - Print "Correct!" and stop if guess == secret
# ===========================================================================
print("\n--- Problem 2: Number Guessing Logic ---")

# SOLUTION
secret = 42
guesses = [10, 55, 42, 70]

for guess in guesses:
    if guess < secret:
        print(f"  {guess} → Too low")
    elif guess > secret:
        print(f"  {guess} → Too high")
    else:
        print(f"  {guess} → Correct!")
        break


# ===========================================================================
# Problem 3: Triangular Star Pattern
# ------------------------------------
# Print a right-aligned triangle of stars for a given height (n=6):
#      *
#     **
#    ***
#   ****
#  *****
# ******
# ===========================================================================
print("\n--- Problem 3: Star Triangle ---")

# SOLUTION
n = 6
for row in range(1, n + 1):
    spaces = " " * (n - row)
    stars  = "*" * row
    print(f"  {spaces}{stars}")


# ===========================================================================
# Problem 4: Sum of Digits
# -------------------------
# Given an integer n (possibly negative), compute the sum of its digits.
# Example: 12345 → 1+2+3+4+5 = 15
#          -987  → 9+8+7 = 24
# ===========================================================================
print("\n--- Problem 4: Sum of Digits ---")

# SOLUTION
def sum_of_digits(n):
    """Return the sum of the absolute digits of an integer."""
    total = 0
    for ch in str(abs(n)):   # convert to string, iterate characters
        total += int(ch)
    return total

for n in [12345, -987, 0, 9999, 1]:
    print(f"  sum_of_digits({n:6d}) = {sum_of_digits(n)}")


# ===========================================================================
# Problem 5: Prime Number Checker
# --------------------------------
# Write a function is_prime(n) that returns True if n is a prime number.
# A number is prime if it is >= 2 and has no divisors other than 1 and itself.
# Optimisation: only check divisors up to √n.
# Test: 2, 3, 4, 17, 18, 97, 100
# ===========================================================================
print("\n--- Problem 5: Prime Number Checker ---")

# SOLUTION
def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True     # no divisors found

for n in [2, 3, 4, 17, 18, 97, 100]:
    print(f"  is_prime({n:3d}) = {is_prime(n)}")


# ===========================================================================
# Problem 6: Collatz Sequence
# ----------------------------
# The Collatz conjecture: starting from any positive integer n,
# apply the rule: if n is even → n //= 2; if n is odd → n = 3n + 1
# The sequence always (supposedly) reaches 1.
# Print the sequence from n=27 and count the steps.
# ===========================================================================
print("\n--- Problem 6: Collatz Sequence ---")

# SOLUTION
def collatz(n):
    """Return the Collatz sequence starting from n."""
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

seq = collatz(27)
print(f"  Collatz(27): {len(seq)} steps")
print(f"  Max value:   {max(seq)}")
# Print just the first and last 5 values for brevity
print(f"  Start: {seq[:5]} ...")
print(f"  End:   ... {seq[-5:]}")


# ===========================================================================
# Problem 7: Nested Loop — Multiplication Table
# ----------------------------------------------
# Print a full multiplication table from 1×1 to 9×9.
# Format each product to take exactly 4 characters so columns align.
# ===========================================================================
print("\n--- Problem 7: Multiplication Table ---")

# SOLUTION
print("  ", end="")
for j in range(1, 10):
    print(f"{j:4d}", end="")
print()
print("  " + "-" * 36)

for i in range(1, 10):
    print(f"{i:2d}|", end="")
    for j in range(1, 10):
        print(f"{i * j:4d}", end="")
    print()


# ===========================================================================
# Problem 8: Loop else — Linear Search
# ----------------------------------------
# Write a function linear_search(lst, target) that uses a for loop to
# search for target in lst.
# Use the loop else clause to print "Not found" only if no break occurred.
# Return the index if found, or -1 if not found.
# ===========================================================================
print("\n--- Problem 8: Linear Search with loop else ---")

# SOLUTION
def linear_search(lst, target):
    """Search for target in lst; return index or -1."""
    for i, value in enumerate(lst):
        if value == target:
            print(f"  Found {target!r} at index {i}")
            return i
    else:
        print(f"  {target!r} not found in list")
        return -1

data = [3, 7, 2, 9, 1, 5, 8]
linear_search(data, 9)
linear_search(data, 4)


# ===========================================================================
# Problem 9: Accumulate Until Threshold
# ----------------------------------------
# Starting from 1 and doubling each step (1, 2, 4, 8, ...),
# print each value while the running sum stays below 100.
# Print the final sum and how many terms were added.
# ===========================================================================
print("\n--- Problem 9: Accumulate Until Threshold ---")

# SOLUTION
value = 1
total = 0
terms = 0
THRESHOLD = 100

print("  Terms added:", end=" ")
while total + value < THRESHOLD:
    print(value, end=" ")
    total += value
    terms += 1
    value *= 2
print()
print(f"  Total: {total}, Terms: {terms}")


# ===========================================================================
# Problem 10: Password Validator with Detailed Feedback
# --------------------------------------------------------
# Write a function validate_password(pwd) that:
# - Checks length >= 8
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter
# - Contains at least one digit
# - Contains at least one special character from: !@#$%^&*
# For each failed check, append a message to a list and return (is_valid, messages).
# ===========================================================================
print("\n--- Problem 10: Password Validator ---")

# SOLUTION
def validate_password(pwd):
    """
    Validate a password against multiple criteria.
    Returns (is_valid: bool, messages: list[str])
    """
    SPECIAL_CHARS = set("!@#$%^&*")
    messages = []

    if len(pwd) < 8:
        messages.append("Must be at least 8 characters")
    if not any(c.isupper() for c in pwd):
        messages.append("Must contain at least one uppercase letter")
    if not any(c.islower() for c in pwd):
        messages.append("Must contain at least one lowercase letter")
    if not any(c.isdigit() for c in pwd):
        messages.append("Must contain at least one digit")
    if not any(c in SPECIAL_CHARS for c in pwd):
        messages.append("Must contain at least one special character (!@#$%^&*)")

    is_valid = len(messages) == 0
    return is_valid, messages

test_passwords = [
    "abc",
    "password",
    "Password1",
    "StrongP4ss!",
    "N0Special",
    "all_lower1!",
]

for sample in test_passwords:
    valid, issues = validate_password(sample)
    status = "✓ Valid" if valid else "✗ Invalid"
    print(f"  {sample!r:<18} → {status}")  # lgtm[py/clear-text-logging-sensitive-data]
    for issue in issues:
        print(f"      - {issue}")  # lgtm[py/clear-text-logging-sensitive-data]

print("\nAll practice problems complete.")
