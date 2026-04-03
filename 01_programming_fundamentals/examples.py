"""
Topic 01 — Programming Fundamentals: Examples
==============================================
Run this file to see all examples execute in sequence.
    python 01_programming_fundamentals/examples.py
"""

# ===========================================================================
# Example 1: Hello World
# The simplest Python program — calls the built-in print() function.
# ===========================================================================
print("=" * 50)
print("Example 1: Hello World")
print("=" * 50)

print("Hello, World!")
print("Hello", "Python", "3")  # print() accepts multiple arguments


# ===========================================================================
# Example 2: Variable Assignment and Types
# Python is dynamically typed — the type is determined by the value assigned.
# ===========================================================================
print("\nExample 2: Variable Assignment and Types")
print("-" * 40)

name = "Alice"          # str
age = 21                # int
height = 1.68           # float
is_student = True       # bool
nothing = None          # NoneType

print(name)
print(age)
print(height)
print(is_student)
print(nothing)


# ===========================================================================
# Example 3: Type Checking with type()
# Use type() to inspect what Python thinks a variable is.
# ===========================================================================
print("\nExample 3: Type Checking with type()")
print("-" * 40)

print(type("hello"))        # <class 'str'>
print(type(42))             # <class 'int'>
print(type(3.14))           # <class 'float'>
print(type(True))           # <class 'bool'>
print(type(None))           # <class 'NoneType'>
print(type([1, 2, 3]))      # <class 'list'>

# isinstance() is preferred in production code (handles inheritance)
print(isinstance(42, int))          # True
print(isinstance(42, (int, float))) # True — checks multiple types at once


# ===========================================================================
# Example 4: Multiple Assignment
# Python supports several compact assignment forms.
# ===========================================================================
print("\nExample 4: Multiple Assignment")
print("-" * 40)

# Assign the same value to multiple names
x = y = z = 0
print(x, y, z)  # 0 0 0

# Tuple unpacking — assign multiple values in one statement
first, second, third = 10, 20, 30
print(first, second, third)  # 10 20 30

# Swap variables without a temporary variable (Python idiom)
a, b = 5, 9
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# Extended unpacking with * (Python 3+)
head, *tail = [1, 2, 3, 4, 5]
print(f"head={head}, tail={tail}")  # head=1, tail=[2, 3, 4, 5]


# ===========================================================================
# Example 5: Constants Convention
# Python has no built-in constant type. UPPER_SNAKE_CASE signals "don't change".
# ===========================================================================
print("\nExample 5: Constants Convention")
print("-" * 40)

PI = 3.141592653589793
MAX_RETRIES = 3
GRAVITY_MS2 = 9.81      # m/s² — units in the name improve clarity

print(f"PI = {PI}")
print(f"MAX_RETRIES = {MAX_RETRIES}")
print(f"GRAVITY = {GRAVITY_MS2} m/s²")

# Python does NOT prevent you from changing a "constant" —
# the UPPER_CASE convention is a human signal only.


# ===========================================================================
# Example 6: Print Formatting
# Three main approaches: % formatting (old), str.format(), and f-strings (modern)
# ===========================================================================
print("\nExample 6: Print Formatting")
print("-" * 40)

product = "coffee"
price = 3.5
quantity = 2

# f-strings (Python 3.6+) — most readable, recommended
print(f"{quantity}x {product} = ${quantity * price:.2f}")

# str.format() — still common in older codebases
print("{0}x {1} = ${2:.2f}".format(quantity, product, quantity * price))

# % formatting — oldest style, still seen in legacy code
print("%dx %s = $%.2f" % (quantity, product, quantity * price))

# Controlling print() separators and endings
print("one", "two", "three", sep=" | ")    # one | two | three
print("no newline here", end=" ")
print("← same line")


# ===========================================================================
# Example 7: Comments and Docstrings
# Comments explain intent; docstrings document functions, classes, and modules.
# ===========================================================================
print("\nExample 7: Comments and Docstrings")
print("-" * 40)


def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle. Must be non-negative.

    Returns:
        float: The area in the same units squared.
    """
    PI = 3.141592653589793
    return PI * radius ** 2  # area formula: π × r²


area = calculate_area(5)
print(f"Area of circle with radius 5: {area:.4f}")

# Access the docstring programmatically
print(calculate_area.__doc__)


# ===========================================================================
# Example 8: Basic Input / Output
# input() always returns a string — cast when you need a number.
# ===========================================================================
print("\nExample 8: Basic Input / Output")
print("-" * 40)

# In a real program you would call input() interactively.
# Here we simulate it with predefined values to keep the example runnable.

simulated_input = "25"                  # pretend the user typed "25"
user_age = int(simulated_input)         # cast str → int
print(f"User age: {user_age}")
print(f"Type after cast: {type(user_age)}")  # <class 'int'>

# What happens without the cast
raw = "10"
# print(raw + 5)  # TypeError: can only concatenate str (not "int") to str
print(int(raw) + 5)  # 15 — correct


# ===========================================================================
# Example 9: Code Blocks and Indentation
# Indentation (4 spaces) defines the scope of a block. Inconsistency = error.
# ===========================================================================
print("\nExample 9: Code Blocks and Indentation")
print("-" * 40)

score = 85

# Each elif/else must align with the opening if
if score >= 90:
    grade = "A"
    print("Excellent work!")
elif score >= 80:
    grade = "B"
    print("Good work!")       # both of these lines are inside the elif block
elif score >= 70:
    grade = "C"
else:
    grade = "F"
    print("Needs improvement.")

print(f"Grade: {grade}")      # this line is outside all blocks

# Nested blocks require additional levels of indentation
for i in range(3):            # outer block — 4 spaces
    for j in range(3):        # inner block — 8 spaces
        if i == j:            # innermost block — 12 spaces
            print(f"  diagonal: ({i},{j})")


# ===========================================================================
# Example 10: Simple Calculations
# Python arithmetic operators: + - * / // % **
# ===========================================================================
print("\nExample 10: Simple Calculations")
print("-" * 40)

length = 7
width = 4

area = length * width
perimeter = 2 * (length + width)
diagonal = (length ** 2 + width ** 2) ** 0.5  # Pythagorean theorem

print(f"Rectangle {length}×{width}")
print(f"  Area:      {area}")
print(f"  Perimeter: {perimeter}")
print(f"  Diagonal:  {diagonal:.4f}")

# Integer vs float division
print(f"\n17 / 5  = {17 / 5}")    # 3.4  (true division — always float)
print(f"17 // 5 = {17 // 5}")    # 3    (floor division — integer result)
print(f"17 % 5  = {17 % 5}")     # 2    (modulo — remainder)
print(f"2 ** 10 = {2 ** 10}")    # 1024 (exponentiation)

print("\nAll examples complete.")
