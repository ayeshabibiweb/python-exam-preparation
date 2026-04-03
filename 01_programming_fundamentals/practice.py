"""
Topic 01 — Programming Fundamentals: Practice Problems
=======================================================
Attempt each problem yourself before reading the solution.
Cover the solution with your hand or a piece of paper.
Run this file to verify all solutions produce correct output.
    python 01_programming_fundamentals/practice.py
"""

print("=" * 60)
print("Topic 01 — Practice Problems")
print("=" * 60)

# ===========================================================================
# Problem 1: Temperature Converter
# ---------------------------------
# Write a program that converts a temperature from Celsius to Fahrenheit
# and from Celsius to Kelvin.
# Formula: F = (C × 9/5) + 32
# Formula: K = C + 273.15
# Given: celsius = 100
# Expected output:
#   100°C = 212.00°F
#   100°C = 373.15K
# ===========================================================================
print("\n--- Problem 1: Temperature Converter ---")

# SOLUTION
celsius = 100
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C = {fahrenheit:.2f}°F")
print(f"{celsius}°C = {kelvin:.2f}K")


# ===========================================================================
# Problem 2: Circle Calculator
# --------------------------------
# Given a radius of 7, calculate and print:
#   - The circumference (2πr)
#   - The area (πr²)
# Use PI = 3.141592653589793
# Round outputs to 4 decimal places.
# ===========================================================================
print("\n--- Problem 2: Circle Calculator ---")

# SOLUTION
PI = 3.141592653589793
radius = 7

circumference = 2 * PI * radius
area = PI * radius ** 2

print(f"Radius:        {radius}")
print(f"Circumference: {circumference:.4f}")
print(f"Area:          {area:.4f}")


# ===========================================================================
# Problem 3: Variable Swap Without a Temporary Variable
# -------------------------------------------------------
# Given x = 42 and y = 99, swap their values using Python's
# tuple unpacking. Print both before and after.
# ===========================================================================
print("\n--- Problem 3: Variable Swap ---")

# SOLUTION
x = 42
y = 99

print(f"Before: x={x}, y={y}")
x, y = y, x
print(f"After:  x={x}, y={y}")


# ===========================================================================
# Problem 4: Greeting Generator
# --------------------------------
# Given a first name, last name, and age, print a formatted greeting:
#   "Hello, my name is Alice Smith and I am 21 years old."
# Use an f-string.
# ===========================================================================
print("\n--- Problem 4: Greeting Generator ---")

# SOLUTION
first_name = "Alice"
last_name = "Smith"
age = 21

greeting = f"Hello, my name is {first_name} {last_name} and I am {age} years old."
print(greeting)


# ===========================================================================
# Problem 5: Simple Receipt
# --------------------------
# You bought 3 items:
#   - Coffee: £2.50
#   - Sandwich: £4.75
#   - Water: £1.20
# Print a receipt showing each item and price, then the total.
# Use print() with sep and format specifiers to align the output.
# ===========================================================================
print("\n--- Problem 5: Simple Receipt ---")

# SOLUTION
coffee = 2.50
sandwich = 4.75
water = 1.20
total = coffee + sandwich + water

print(f"{'Item':<12} {'Price':>8}")
print("-" * 22)
print(f"{'Coffee':<12} £{coffee:>6.2f}")
print(f"{'Sandwich':<12} £{sandwich:>6.2f}")
print(f"{'Water':<12} £{water:>6.2f}")
print("-" * 22)
print(f"{'TOTAL':<12} £{total:>6.2f}")


# ===========================================================================
# Problem 6: Seconds Converter
# -----------------------------
# Given total_seconds = 3725, compute and print how many
# hours, minutes, and remaining seconds that represents.
# Expected output: 3725 seconds = 1 hour(s), 2 minute(s), 5 second(s)
# ===========================================================================
print("\n--- Problem 6: Seconds Converter ---")

# SOLUTION
total_seconds = 3725

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")


# ===========================================================================
# Problem 7: BMI Calculator
# --------------------------
# Given weight_kg = 70 and height_m = 1.75, calculate BMI.
# Formula: BMI = weight / (height ** 2)
# Print the result rounded to 1 decimal place and the category:
#   < 18.5 → Underweight
#   18.5–24.9 → Normal weight
#   25–29.9 → Overweight
#   >= 30 → Obese
# Note: use only what you have learned so far (no if/else needed — just calculate
# and print; we cover conditionals in Topic 04).
# ===========================================================================
print("\n--- Problem 7: BMI Calculator ---")

# SOLUTION
weight_kg = 70
height_m = 1.75

bmi = weight_kg / (height_m ** 2)
print(f"Weight: {weight_kg} kg")
print(f"Height: {height_m} m")
print(f"BMI:    {bmi:.1f}")
# Category determination (previewing Topic 04 logic)
category = (
    "Underweight" if bmi < 18.5
    else "Normal weight" if bmi < 25
    else "Overweight" if bmi < 30
    else "Obese"
)
print(f"Category: {category}")


# ===========================================================================
# Problem 8: Naming Convention Audit
# ------------------------------------
# The following variable names contain errors or violate conventions.
# Identify what is wrong with each, then rewrite them correctly.
#
#   2fast = 120         # invalid
#   my-score = 95       # invalid
#   UserAge = 30        # wrong convention for a variable
#   ITEMS = []          # wrong convention for a mutable variable
#   list = [1, 2, 3]    # shadows built-in
#
# Print the corrected assignments and their values.
# ===========================================================================
print("\n--- Problem 8: Naming Convention Audit ---")

# SOLUTION
# 2fast  → cannot start with a digit → use: speed_kmh or fast_speed
# my-score → hyphens not allowed   → use: my_score
# UserAge  → PascalCase for classes only → use: user_age
# ITEMS    → ALL_CAPS for constants; a mutable list is not a constant → use: items
# list     → shadows the built-in list type → use: numbers or item_list

speed_kmh = 120
my_score = 95
user_age = 30
items = []
numbers = [1, 2, 3]

print(f"speed_kmh = {speed_kmh}")
print(f"my_score  = {my_score}")
print(f"user_age  = {user_age}")
print(f"items     = {items}")
print(f"numbers   = {numbers}")


# ===========================================================================
# Problem 9: Multi-Line Output with Alignment
# ---------------------------------------------
# Print the following multiplication table row for 7
# (from 7×1 to 7×10), with aligned columns:
#   7 x  1 =  7
#   7 x  2 = 14
#   ...
#   7 x 10 = 70
# (No loops needed — just print() calls with format specifiers.
#  Loops are covered in Topic 04.)
# ===========================================================================
print("\n--- Problem 9: Multiplication Table Row ---")

# SOLUTION — using a loop here as a preview (Topic 04 covers this fully)
n = 7
for i in range(1, 11):
    print(f"{n} x {i:2d} = {n * i:3d}")


# ===========================================================================
# Problem 10: Extracting Parts of a Value
# ----------------------------------------
# Given a floating-point number value = 47.836:
#   - Extract the integer part (47)
#   - Extract the decimal part (0.836), rounded to 3 decimal places
#   - Print both
# Hint: int() truncates, and you can subtract to get the decimal portion.
# ===========================================================================
print("\n--- Problem 10: Extracting Parts of a Value ---")

# SOLUTION
value = 47.836

integer_part = int(value)               # truncates toward zero
decimal_part = round(value - integer_part, 3)

print(f"Original:     {value}")
print(f"Integer part: {integer_part}")
print(f"Decimal part: {decimal_part}")

print("\nAll practice problems complete.")
