"""
Topic 03 — Operators and Expressions: Practice Problems
=======================================================
Attempt each problem yourself before reading the solution.
    python 03_operators_expressions/practice.py
"""

print("=" * 60)
print("Topic 03 — Practice Problems")
print("=" * 60)

# ===========================================================================
# Problem 1: Expression Evaluation — Predict the Output
# -------------------------------------------------------
# Before running, write down what you think each expression evaluates to.
# Then verify by running the code.
#
# Expressions:
#   a) 3 + 4 * 2
#   b) (3 + 4) * 2
#   c) 10 / 3
#   d) 10 // 3
#   e) 10 % 3
#   f) 2 ** 3 ** 2
#   g) not 5 == 5
#   h) 5 != 3 and 2 > 1
# ===========================================================================
print("\n--- Problem 1: Expression Evaluation ---")

# SOLUTION
print(f"  a) 3 + 4 * 2      = {3 + 4 * 2}")       # 11
print(f"  b) (3 + 4) * 2    = {(3 + 4) * 2}")     # 14
print(f"  c) 10 / 3         = {10 / 3:.6f}")       # 3.333...
print(f"  d) 10 // 3        = {10 // 3}")           # 3
print(f"  e) 10 % 3         = {10 % 3}")            # 1
print(f"  f) 2 ** 3 ** 2    = {2 ** 3 ** 2}")       # 512 (right-associative)
print(f"  g) not 5 == 5     = {not 5 == 5}")        # False
print(f"  h) 5!=3 and 2>1   = {5 != 3 and 2 > 1}") # True


# ===========================================================================
# Problem 2: Divisibility Checker
# ---------------------------------
# Write an expression (one line) that evaluates to True if a number n
# is divisible by both 3 and 5, and False otherwise.
# Test with n = 15, 9, 10, 7.
# ===========================================================================
print("\n--- Problem 2: Divisibility Checker ---")

# SOLUTION
def divisible_by_3_and_5(n):
    return n % 3 == 0 and n % 5 == 0

for n in [15, 9, 10, 7]:
    print(f"  divisible_by_3_and_5({n:2d}) = {divisible_by_3_and_5(n)}")


# ===========================================================================
# Problem 3: Without Using if, Return a Default
# -----------------------------------------------
# Use Python's short-circuit behaviour of `or` to write a one-liner:
# Given a value v, return v if it is truthy, otherwise return "N/A".
# Test with: "Alice", "", 0, 42, None, [], "0"
# ===========================================================================
print("\n--- Problem 3: Short-Circuit Default ---")

# SOLUTION
def default_value(v):
    return v or "N/A"

test_cases = ["Alice", "", 0, 42, None, [], "0"]
for v in test_cases:
    print(f"  default_value({v!r:<8}) = {default_value(v)!r}")


# ===========================================================================
# Problem 4: Bitwise Masking
# ---------------------------
# Given flags = 0b10110101 (8-bit flag register):
#   a) Check if bit 4 (0-indexed from right) is set → True/False
#   b) Set bit 3 (turn it on)
#   c) Clear bit 7 (turn it off)
#   d) Toggle bit 2 (flip it)
# Print flags in binary after each operation.
# ===========================================================================
print("\n--- Problem 4: Bitwise Masking ---")

# SOLUTION
flags = 0b10110101
print(f"  Original flags: {flags:08b} ({flags})")

# a) Check bit 4
bit4_set = bool(flags & (1 << 4))
print(f"  a) Bit 4 set:   {bit4_set}   ({flags:08b} & {(1<<4):08b} = {flags & (1<<4):08b})")

# b) Set bit 3
flags_b = flags | (1 << 3)
print(f"  b) Set bit 3:   {flags_b:08b} (was {flags:08b})")

# c) Clear bit 7 (using & with inverted mask)
flags_c = flags & ~(1 << 7)
print(f"  c) Clear bit 7: {flags_c:08b} (was {flags:08b})")

# d) Toggle bit 2
flags_d = flags ^ (1 << 2)
print(f"  d) Toggle bit 2:{flags_d:08b} (was {flags:08b})")


# ===========================================================================
# Problem 5: Leap Year Detector
# ------------------------------
# A year is a leap year if:
#   - Divisible by 4, AND not divisible by 100
#   OR
#   - Divisible by 400
# Write a single boolean expression (no if/else).
# Test: 2000 (True), 1900 (False), 2024 (True), 2023 (False)
# ===========================================================================
print("\n--- Problem 5: Leap Year Detector ---")

# SOLUTION
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

for year in [2000, 1900, 2024, 2023, 1600, 2100]:
    print(f"  is_leap_year({year}) = {is_leap_year(year)}")


# ===========================================================================
# Problem 6: Chained Comparison Validator
# ----------------------------------------
# Write a function is_valid_grade(score) that returns True if score is
# between 0 and 100 inclusive, using a chained comparison.
# Test with: -1, 0, 55, 100, 101
# ===========================================================================
print("\n--- Problem 6: Chained Comparison ---")

# SOLUTION
def is_valid_grade(score):
    return 0 <= score <= 100

for score in [-1, 0, 55, 100, 101]:
    print(f"  is_valid_grade({score:4d}) = {is_valid_grade(score)}")


# ===========================================================================
# Problem 7: Operator Precedence Puzzle
# ----------------------------------------
# Add parentheses to make each statement True (do NOT change the values).
#   a) 2 + 3 * 4 == 20    → False without parens; True with parens
#   b) -2 ** 2 == 4        → False without parens; True with parens
#   c) not True == False   → True without parens; False with parens (not (True == False))
# Verify each corrected expression evaluates to True.
# ===========================================================================
print("\n--- Problem 7: Precedence Puzzle ---")

# SOLUTION
a_fixed = (2 + 3) * 4 == 20          # True
b_fixed = (-2) ** 2 == 4              # True
c_fixed = not (True == False)         # True (== first, then not)
c_orig  = not True == False           # True (not True is False; False == False is True)

print(f"  a) (2 + 3) * 4 == 20      = {a_fixed}")
print(f"  b) (-2) ** 2 == 4         = {b_fixed}")
print(f"  c) not (True == False)    = {c_fixed}")
print(f"     not True == False      = {c_orig}  (same result, different reason)")


# ===========================================================================
# Problem 8: Augmented Assignment Chain
# ----------------------------------------
# Starting with x = 100, apply the following augmented assignments in order:
#   x //= 7
#   x += 15
#   x **= 2
#   x %= 50
#   x -= 3
# Print x after each step and the final value.
# ===========================================================================
print("\n--- Problem 8: Augmented Assignment Chain ---")

# SOLUTION
x = 100
print(f"  Start:    x = {x}")
x //= 7;  print(f"  //= 7  → x = {x}")    # 14
x += 15;  print(f"  += 15  → x = {x}")    # 29
x **= 2;  print(f"  **= 2  → x = {x}")    # 841
x %= 50;  print(f"  %= 50  → x = {x}")    # 41
x -= 3;   print(f"  -= 3   → x = {x}")    # 38


# ===========================================================================
# Problem 9: Password Validator
# ------------------------------
# A password is valid if ALL of:
#   - Length >= 8
#   - Contains at least one digit (hint: use any() + a generator)
#   - Does not start or end with a space
# Write a one-line boolean expression (or short function).
# Test: "abc", "password1", "  hello1", "StrongP4ss"
# ===========================================================================
print("\n--- Problem 9: Password Validator ---")

# SOLUTION
def is_valid_password(pwd):
    return (
        len(pwd) >= 8
        and any(c.isdigit() for c in pwd)
        and not pwd.startswith(" ")
        and not pwd.endswith(" ")
    )

test_inputs = ["abc", "password1", "  hello1", "StrongP4ss", "nodigits", "12345678"]
for sample in test_inputs:
    print(f"  {sample!r:<15} → valid: {is_valid_password(sample)}")


# ===========================================================================
# Problem 10: Packing and Unpacking Bits
# ----------------------------------------
# Pack the RGB values R=200, G=128, B=45 into a single 24-bit integer
# using bitwise left-shift and OR operators.
# Then unpack the components back from the integer and verify they match.
# ===========================================================================
print("\n--- Problem 10: Bit Packing (RGB) ---")

# SOLUTION
R, G, B = 200, 128, 45

# Pack: R occupies bits 16-23, G bits 8-15, B bits 0-7
packed = (R << 16) | (G << 8) | B
print(f"  Packed: R={R}, G={G}, B={B} → 0x{packed:06X} ({packed})")

# Unpack
r_out = (packed >> 16) & 0xFF
g_out = (packed >> 8)  & 0xFF
b_out =  packed        & 0xFF
print(f"  Unpacked: R={r_out}, G={g_out}, B={b_out}")
print(f"  Match: {(R, G, B) == (r_out, g_out, b_out)}")

print("\nAll practice problems complete.")
