"""
Topic 02 — Data Types and Variables: Examples
==============================================
Run this file to see all examples execute in sequence.
    python 02_data_types_variables/examples.py
"""

import math

# ===========================================================================
# Example 1: Integer Operations
# Python integers have arbitrary precision — no overflow.
# ===========================================================================
print("=" * 50)
print("Example 1: Integer Operations")
print("=" * 50)

a = 100
b = -7
big = 2 ** 64          # larger than 64-bit unsigned max — Python handles it

print(f"a = {a},  type: {type(a).__name__}")
print(f"b = {b},  type: {type(b).__name__}")
print(f"2**64 = {big}")

# Integer literals in different bases (all represent the same value: 255)
dec = 255
bin_val = 0b11111111
oct_val = 0o377
hex_val = 0xFF
print(f"\n255 in different bases:")
print(f"  decimal: {dec}")
print(f"  binary:  {bin_val}")
print(f"  octal:   {oct_val}")
print(f"  hex:     {hex_val}")
print(f"  All equal: {dec == bin_val == oct_val == hex_val}")


# ===========================================================================
# Example 2: Float Precision
# IEEE 754 double precision — some fractions can't be represented exactly.
# ===========================================================================
print("\nExample 2: Float Precision")
print("-" * 40)

x = 0.1 + 0.2
print(f"0.1 + 0.2 = {x}")               # 0.30000000000000004
print(f"0.1 + 0.2 == 0.3: {x == 0.3}")  # False — classic float trap

# Correct way to compare floats
tolerance = 1e-9
print(f"Within tolerance: {abs(x - 0.3) < tolerance}")  # True
print(f"math.isclose():   {math.isclose(x, 0.3)}")       # True

# Scientific notation
avogadro = 6.022e23
planck = 6.626e-34
print(f"\nAvogadro's number: {avogadro:.3e}")
print(f"Planck's constant: {planck:.3e}")


# ===========================================================================
# Example 3: String Basics
# Strings are immutable sequences of Unicode characters.
# ===========================================================================
print("\nExample 3: String Basics")
print("-" * 40)

s1 = 'single quotes'
s2 = "double quotes"
s3 = """triple-quoted
multi-line string"""
raw = r"C:\Users\Alice\Documents"  # raw string — backslash not an escape

print(s1)
print(s2)
print(s3)
print(raw)

# Strings are immutable — you cannot change a character in place
word = "hello"
# word[0] = "H"  # TypeError: 'str' object does not support item assignment
word = "H" + word[1:]  # must create a new string
print(f"\nModified: {word}")

# String length and indexing
print(f"Length of 'Python': {len('Python')}")
print(f"First char: {'Python'[0]}")    # P
print(f"Last char:  {'Python'[-1]}")   # n


# ===========================================================================
# Example 4: Boolean Operations
# bool is a subclass of int — True==1, False==0.
# ===========================================================================
print("\nExample 4: Boolean Operations")
print("-" * 40)

print(f"True  + True  = {True + True}")    # 2
print(f"True  * 5     = {True * 5}")       # 5
print(f"False + 1     = {False + 1}")      # 1
print(f"isinstance(True, int): {isinstance(True, int)}")  # True

# Truthiness of various values
values = [0, 0.0, "", [], {}, None, "hello", 42, [0], " "]
print("\nTruthiness:")
for v in values:
    print(f"  bool({v!r:12}) = {bool(v)}")


# ===========================================================================
# Example 5: None Type
# None is the singleton representing "no value".
# ===========================================================================
print("\nExample 5: None Type")
print("-" * 40)

result = None
print(f"result = {result}")
print(f"type(result) = {type(result)}")
print(f"result is None: {result is None}")    # correct comparison
print(f"result == None: {result == None}")    # works but not idiomatic

# Functions without explicit return give back None
def do_nothing():
    pass  # no return statement

returned = do_nothing()
print(f"\ndo_nothing() returned: {returned!r}")  # None


# ===========================================================================
# Example 6: Type Casting
# Explicit conversion between types using constructor functions.
# ===========================================================================
print("\nExample 6: Type Casting")
print("-" * 40)

# str → int (raises ValueError if string is not a valid integer)
num_str = "42"
num_int = int(num_str)
print(f"int('42')    = {num_int},   type: {type(num_int).__name__}")

# str → float
pi_str = "3.14159"
pi_float = float(pi_str)
print(f"float('3.14159') = {pi_float},  type: {type(pi_float).__name__}")

# float → int (truncates, does NOT round)
print(f"int(3.9)  = {int(3.9)}")    # 3  (not 4!)
print(f"int(-3.9) = {int(-3.9)}")   # -3 (toward zero, not -4)
print(f"round(3.9) = {round(3.9)}") # 4  (use round() for rounding)

# int → str, float → str
print(f"str(100)  = {str(100)!r}")
print(f"str(3.14) = {str(3.14)!r}")

# Invalid conversion
try:
    bad = int("hello")
except ValueError as e:
    print(f"\nValueError: {e}")


# ===========================================================================
# Example 7: Implicit vs Explicit Conversion
# Python widens numeric types automatically; str requires explicit cast.
# ===========================================================================
print("\nExample 7: Implicit vs Explicit Conversion")
print("-" * 40)

i = 5
f = 2.0
result = i + f          # int + float → float (implicit widening)
print(f"int + float = {result},  type: {type(result).__name__}")

# bool in arithmetic (True=1, False=0)
total = True + True + False + True
print(f"True+True+False+True = {total}")  # 3

# Python does NOT implicitly convert str to number
# print(5 + "3")  # TypeError
print(5 + int("3"))   # 8 — explicit cast required


# ===========================================================================
# Example 8: Scope Demonstration — Local vs Global
# Local variables are created inside a function and do not exist outside.
# ===========================================================================
print("\nExample 8: Scope — Local vs Global")
print("-" * 40)

message = "global message"  # global scope

def show_local():
    message = "local message"    # creates a LOCAL variable, shadows global
    print(f"Inside function: {message}")

def modify_global():
    global message               # declares we want to modify the global
    message = "modified global"

show_local()
print(f"After show_local():    {message}")  # still "global message"

modify_global()
print(f"After modify_global(): {message}")  # now "modified global"


# ===========================================================================
# Example 9: Nonlocal Keyword
# Allows an inner function to modify a variable in its enclosing function.
# ===========================================================================
print("\nExample 9: Nonlocal Keyword")
print("-" * 40)

def make_counter():
    count = 0                 # enclosing scope variable

    def increment():
        nonlocal count        # refers to enclosing scope's 'count'
        count += 1
        return count

    return increment          # return the inner function

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
# Each call remembers and modifies 'count' from the enclosing scope


# ===========================================================================
# Example 10: is vs == for None (and identity vs equality)
# is tests object identity (same object in memory).
# == tests value equality (same value, possibly different objects).
# ===========================================================================
print("\nExample 10: is vs == for None and Identity")
print("-" * 40)

x = None
print(f"x is None:  {x is None}")   # True  — correct idiom
print(f"x == None:  {x == None}")   # True  — works but not idiomatic

# For regular objects, is and == can differ
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"\na = {a},  b = {b},  c = a")
print(f"a == b:  {a == b}")    # True  — same value
print(f"a is b:  {a is b}")    # False — different objects in memory
print(f"a is c:  {a is c}")    # True  — same object

# Small integer interning (implementation detail — don't rely on this)
x = 256
y = 256
print(f"\n256 is 256: {x is y}")   # True (CPython caches small ints)

x = 1000
y = 1000
print(f"1000 is 1000: {x is y}")   # May be False (not cached)

print("\nAll examples complete.")
