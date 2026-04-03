"""
Topic 03 — Operators and Expressions: Examples
===============================================
Run this file to see all examples execute in sequence.
    python 03_operators_expressions/examples.py
"""

# ===========================================================================
# Example 1: Arithmetic Operators
# +  -  *  /  //  %  **
# ===========================================================================
print("=" * 50)
print("Example 1: Arithmetic Operators")
print("=" * 50)

a, b = 17, 5

print(f"{a} + {b}  = {a + b}")    # 22
print(f"{a} - {b}  = {a - b}")    # 12
print(f"{a} * {b}  = {a * b}")    # 85
print(f"{a} / {b}  = {a / b}")    # 3.4   (always float)
print(f"{a} // {b} = {a // b}")   # 3     (floor division)
print(f"{a} % {b}  = {a % b}")    # 2     (remainder)
print(f"{a} ** 2   = {a ** 2}")   # 289   (exponent)

# Floor division with negatives — rounds toward -infinity
print(f"\n-17 // 5  = {-17 // 5}")   # -4  (NOT -3!)
print(f"17 // -5  = {17 // -5}")     # -4
print(f"-17 % 5   = {-17 % 5}")      # 3   (sign follows divisor)

# Exponent precedence gotcha
print(f"\n-2 ** 2  = {-2 ** 2}")        # -4  (unary minus applied AFTER **)
print(f"(-2) ** 2 = {(-2) ** 2}")       # 4   (parentheses force order)

# Right-associativity of **
print(f"2 ** 3 ** 2 = {2 ** 3 ** 2}")   # 512 = 2**(3**2) = 2**9, not (2**3)**2=64


# ===========================================================================
# Example 2: Comparison Operators
# Return True or False. Support chaining.
# ===========================================================================
print("\nExample 2: Comparison Operators")
print("-" * 40)

x = 7

print(f"x = {x}")
print(f"x == 7:  {x == 7}")    # True
print(f"x != 7:  {x != 7}")    # False
print(f"x > 5:   {x > 5}")     # True
print(f"x < 5:   {x < 5}")     # False
print(f"x >= 7:  {x >= 7}")    # True
print(f"x <= 6:  {x <= 6}")    # False

# Chained comparisons — Python-specific feature
print(f"\n0 < x < 10:   {0 < x < 10}")    # True
print(f"5 <= x <= 10: {5 <= x <= 10}")    # True
print(f"1 < x < 5:    {1 < x < 5}")       # False (7 is not < 5)

# Comparing strings (lexicographic order)
print(f"\n'apple' < 'banana': {'apple' < 'banana'}")  # True ('a' < 'b')
print(f"'z' > 'a':          {'z' > 'a'}")             # True


# ===========================================================================
# Example 3: Logical Operators — and, or, not
# These return operands, not necessarily True/False.
# ===========================================================================
print("\nExample 3: Logical Operators")
print("-" * 40)

p, q = True, False

print(f"True  and False = {p and q}")    # False
print(f"True  or  False = {p or q}")     # True
print(f"not True        = {not p}")      # False
print(f"not False       = {not q}")      # True

# Returning operands (not just bool)
print(f"\n'' or 'default'     = {'' or 'default'!r}")        # 'default'
print(f"'hello' or 'other'  = {'hello' or 'other'!r}")       # 'hello'
print(f"None and 'value'    = {None and 'value'!r}")          # None
print(f"42 and 'yes'        = {42 and 'yes'!r}")              # 'yes'
print(f"0 or [] or 'found'  = {0 or [] or 'found'!r}")        # 'found'

# Practical: default value pattern
user_name = ""
display_name = user_name or "Anonymous"
print(f"\ndisplay_name = {display_name!r}")   # 'Anonymous'


# ===========================================================================
# Example 4: Short-Circuit Evaluation
# Python stops as soon as result is determined.
# ===========================================================================
print("\nExample 4: Short-Circuit Evaluation")
print("-" * 40)

def expensive(label):
    """Simulates an expensive function — prints if called."""
    print(f"  [called: {label}]")
    return True

# 'and' short-circuits on False
print("False and expensive():")
result = False and expensive("should not run")
print(f"  result = {result}")

# 'or' short-circuits on True
print("True or expensive():")
result = True or expensive("should not run")
print(f"  result = {result}")

# Both sides evaluated when necessary
print("True and expensive():")
result = True and expensive("DOES run")
print(f"  result = {result}")


# ===========================================================================
# Example 5: Bitwise Operators
# Work on the binary representation of integers.
# ===========================================================================
print("\nExample 5: Bitwise Operators")
print("-" * 40)

a = 0b1100  # 12
b = 0b1010  # 10

print(f"a = {a:4d}  ({a:08b})")
print(f"b = {b:4d}  ({b:08b})")
print(f"a & b  = {a & b:4d}  ({(a & b):08b})  (AND)")
print(f"a | b  = {a | b:4d}  ({(a | b):08b})  (OR)")
print(f"a ^ b  = {a ^ b:4d}  ({(a ^ b):08b})  (XOR)")
print(f"~a     = {~a:4d}  (NOT — -(a+1))")

# Shift operators — equivalent to multiply/divide by powers of 2
n = 3
print(f"\n{n} << 2 = {n << 2}  (same as {n} * 4)")
print(f"12 >> 2 = {12 >> 2}  (same as 12 // 4)")

# Common use: check if a number is even/odd using bit masking
for num in [0, 1, 7, 8, 15, 16]:
    parity = "even" if (num & 1) == 0 else "odd"
    print(f"  {num:2d} & 1 = {num & 1}  → {parity}")


# ===========================================================================
# Example 6: Membership Operators — in, not in
# ===========================================================================
print("\nExample 6: Membership Operators")
print("-" * 40)

fruits = ["apple", "banana", "cherry"]
text = "Hello, Python!"
scores = {90: "A", 80: "B", 70: "C"}  # dict

print(f"'banana' in {fruits}: {'banana' in fruits}")       # True
print(f"'mango' not in {fruits}: {'mango' not in fruits}") # True
print(f"'Python' in text: {'Python' in text}")             # True
print(f"90 in scores (dict keys): {90 in scores}")         # True
print(f"3 in range(5): {3 in range(5)}")                   # True


# ===========================================================================
# Example 7: Identity Operators — is, is not
# Tests whether two names point to the exact same object.
# ===========================================================================
print("\nExample 7: Identity Operators")
print("-" * 40)

x = [1, 2, 3]
y = [1, 2, 3]   # same value, different object
z = x           # same object

print(f"x == y:    {x == y}")    # True  (same value)
print(f"x is y:    {x is y}")    # False (different objects)
print(f"x is z:    {x is z}")    # True  (same object)

# None identity check
val = None
print(f"\nval is None:     {val is None}")     # True  ← correct
print(f"val is not None: {val is not None}")   # False


# ===========================================================================
# Example 8: Augmented Assignment Operators
# +=  -=  *=  /=  //=  %=  **=  &=  |=  ^=  <<=  >>=
# ===========================================================================
print("\nExample 8: Augmented Assignment Operators")
print("-" * 40)

n = 10
print(f"Start: n = {n}")
n += 5;   print(f"n += 5  → {n}")    # 15
n -= 3;   print(f"n -= 3  → {n}")    # 12
n *= 2;   print(f"n *= 2  → {n}")    # 24
n /= 4;   print(f"n /= 4  → {n}")    # 6.0 (always float)
n //= 2;  print(f"n //= 2 → {n}")    # 3.0
n **= 3;  print(f"n **= 3 → {n}")    # 27.0
n %= 5;   print(f"n %= 5  → {n}")    # 2.0

# += on a list modifies in-place (different from = list + list)
nums = [1, 2]
ref = nums              # ref and nums point to same list
nums += [3, 4]          # modifies in-place via __iadd__
print(f"\nlist += : {nums}")
print(f"ref is nums: {ref is nums}")  # True — still the same object


# ===========================================================================
# Example 9: Operator Precedence
# Parentheses > ** > unary > * / // % > + - > comparisons > not > and > or
# ===========================================================================
print("\nExample 9: Operator Precedence")
print("-" * 40)

# Evaluate without parentheses first, then verify with parens
expr1 = 2 + 3 * 4         # 14  (* before +)
expr2 = (2 + 3) * 4       # 20  (parens override)
expr3 = 2 ** 3 ** 2       # 512 (** is right-associative: 2**(3**2)=2**9)
expr4 = (2 ** 3) ** 2     # 64  (parens force left-first)
expr5 = not 5 > 3         # False (> before not)
expr6 = not (5 > 3)       # False (same result here)
expr7 = not 5 < 3         # True  (< before not, so not False = True)

print(f"2 + 3 * 4         = {expr1}")
print(f"(2 + 3) * 4       = {expr2}")
print(f"2 ** 3 ** 2       = {expr3}")
print(f"(2 ** 3) ** 2     = {expr4}")
print(f"not 5 > 3         = {expr5}")
print(f"not 5 < 3         = {expr7}")


# ===========================================================================
# Example 10: Combining Operators — Real-World Expressions
# ===========================================================================
print("\nExample 10: Real-World Expressions")
print("-" * 40)

# Determine if a year is a leap year
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is leap year: {is_leap}")

# Clamp a value to [0, 100]
raw_score = 115
clamped = max(0, min(100, raw_score))
print(f"Clamped {raw_score} to [0,100]: {clamped}")

# Extract RGB components from a hex colour using bitwise operators
colour = 0xFF8C00  # dark orange
red   = (colour >> 16) & 0xFF
green = (colour >> 8) & 0xFF
blue  = colour & 0xFF
print(f"\nHex colour: 0x{colour:06X}")
print(f"  R={red}, G={green}, B={blue}")

print("\nAll examples complete.")
