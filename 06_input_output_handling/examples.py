# 06 – Input / Output Handling: Examples
# Run this file: python examples.py
# File I/O examples write to the current working directory.

import os
import json
import csv

DEMO_DIR = os.path.dirname(os.path.abspath(__file__))

def demo_path(filename):
    """Return an absolute path inside the module's own directory."""
    return os.path.join(DEMO_DIR, filename)


print("=" * 60)
print("EXAMPLE 1: print() with Different Parameters")
print("=" * 60)

# Default behaviour
print("Hello", "World")                     # Hello World  (sep=" ")

# Custom separator
print("2024", "01", "15", sep="-")          # 2024-01-15

# No newline at end
print("Loading", end="")
print("...", end="")
print(" done")                              # Loading... done

# Printing to stderr (useful for error messages)
import sys
print("This is an error message", file=sys.stderr)

# Multiple values with custom sep and end
print("red", "green", "blue", sep=" | ", end=" ← colours\n")

# Printing nothing (just a blank line)
print()

# Printing repr vs str using sep
items = [1, "two", 3.0, True]
print(*items, sep=", ")                     # 1, two, 3.0, True


print("\n" + "=" * 60)
print("EXAMPLE 2: input() and Processing User Input")
print("=" * 60)
# In a script, we simulate input() by using a helper so this file
# remains fully runnable without interactive input.

def simulated_input(prompt, value):
    """Simulate input() for demo purposes."""
    print(f"  {prompt}{value}")
    return value

raw = simulated_input("Enter your age: ", "21")
age = int(raw)
print(f"  Next year you will be {age + 1}")

raw_score = simulated_input("Enter your score (0-100): ", "87.5")
score = float(raw_score)
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"  Score {score} → Grade {grade}")

# Safe integer input with validation
def read_int(prompt, value, lo=None, hi=None):
    while True:
        try:
            n = int(simulated_input(prompt, value))
            if lo is not None and n < lo:
                print(f"  Must be >= {lo}")
                continue
            if hi is not None and n > hi:
                print(f"  Must be <= {hi}")
                continue
            return n
        except ValueError:
            print("  Not a valid integer, try again.")

n = read_int("Enter a number between 1 and 10: ", "7", lo=1, hi=10)
print(f"  You entered: {n}")


print("\n" + "=" * 60)
print("EXAMPLE 3: f-String Formatting")
print("=" * 60)

name = "Alice"
age = 21
score = 95.6789
balance = 1_234_567.89

# Basic interpolation
print(f"Name: {name}, Age: {age}")

# Numeric formatting
print(f"Score: {score:.2f}")              # 2 decimal places
print(f"Score: {score:8.2f}")            # width 8, 2 dp
print(f"Balance: {balance:,.2f}")        # thousands separator
print(f"Hex: {255:#010x}")               # 0x000000ff
print(f"Binary: {42:08b}")              # 00101010

# Alignment
header = f"{'Name':<12} {'Score':>8} {'Grade':^6}"
print(header)
print(f"{'Alice':<12} {95.6:>8.1f} {'A':^6}")
print(f"{'Bob':<12} {72.3:>8.1f} {'C':^6}")

# Expressions inside f-strings
x, y = 3, 4
print(f"sqrt({x}² + {y}²) = {(x**2 + y**2)**0.5:.4f}")

# Debugging with = (Python 3.8+)
value = 42
print(f"{value=}")    # value=42


print("\n" + "=" * 60)
print("EXAMPLE 4: .format() Method")
print("=" * 60)

# Positional placeholders
print("{} scored {} on the exam".format("Alice", 95))

# Named placeholders
template = "{name} lives in {city} and studies {subject}."
print(template.format(name="Bob", city="London", subject="Physics"))

# Reusing arguments by index
print("{0} says: '{0} is the best!'".format("Python"))

# Format spec inside .format()
print("{:.3f}".format(3.14159))
print("{:>20}".format("right-aligned"))
print("{:*^30}".format(" centred "))

# Formatting a table
rows = [("Alice", 90), ("Bob", 75), ("Carol", 88)]
print("\n  {:<10} {:>6}".format("Name", "Score"))
print("  " + "-" * 17)
for name, sc in rows:
    print("  {:<10} {:>6.1f}".format(name, sc))


print("\n" + "=" * 60)
print("EXAMPLE 5: % String Formatting (Legacy Style)")
print("=" * 60)

name = "Alice"
age = 21
gpa = 3.875

print("Name: %s, Age: %d, GPA: %.2f" % (name, age, gpa))
print("%-10s %5d %8.3f" % (name, age, gpa))   # left-align name

# %s for any object (calls str())
items = [1, 2, 3]
print("Items: %s" % items)

# % with a dict
print("%(name)s is %(age)d years old." % {"name": name, "age": age})


print("\n" + "=" * 60)
print("EXAMPLE 6: Writing to a File")
print("=" * 60)

filepath = demo_path("demo_output.txt")

with open(filepath, "w", encoding="utf-8") as f:
    f.write("Line 1: Hello, file!\n")
    f.write("Line 2: Python I/O is easy.\n")
    # writelines does NOT add newlines automatically
    f.writelines(["Line 3: first part — ", "second part\n"])
    print(f"  Wrote {f.tell()} bytes")

print(f"  File created at: {filepath}")
print(f"  File exists: {os.path.exists(filepath)}")


print("\n" + "=" * 60)
print("EXAMPLE 7: Reading from a File")
print("=" * 60)

# Read whole file at once
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()
print("  read() result:")
print(content)

# Read line by line (memory efficient)
with open(filepath, "r", encoding="utf-8") as f:
    print("  Iterating line by line:")
    for i, line in enumerate(f, start=1):
        print(f"    [{i}] {line.rstrip()}")

# readlines() → list of strings
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"  readlines() gave {len(lines)} lines")


print("\n" + "=" * 60)
print("EXAMPLE 8: Appending to a File")
print("=" * 60)

append_path = demo_path("demo_append.txt")

# Create initial content
with open(append_path, "w", encoding="utf-8") as f:
    f.write("Original line 1\n")

# Append more content (file is NOT truncated)
with open(append_path, "a", encoding="utf-8") as f:
    f.write("Appended line 2\n")
    f.write("Appended line 3\n")

with open(append_path, "r", encoding="utf-8") as f:
    print(f.read())


print("\n" + "=" * 60)
print("EXAMPLE 9: Context Manager with Files")
print("=" * 60)

csv_path = demo_path("demo_data.csv")

# Write CSV using context manager
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "score"])
    writer.writerows([
        ["Alice", 21, 92],
        ["Bob",   22, 78],
        ["Carol", 20, 88],
    ])
print(f"  Wrote CSV to {csv_path}")

# Read CSV using context manager + DictReader
with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("  CSV contents:")
    for row in reader:
        print(f"    {row['name']}: age={row['age']}, score={row['score']}")

# JSON round-trip
json_path = demo_path("demo_data.json")
data = {"students": [
    {"name": "Alice", "score": 92},
    {"name": "Bob",   "score": 78},
]}

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open(json_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"  JSON loaded: {loaded['students']}")


print("\n" + "=" * 60)
print("EXAMPLE 10: Exception Handling for File Not Found")
print("=" * 60)

def safe_read(path):
    """Read a file and return its content, or None on error."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"  [ERROR] File not found: {path!r}")
        return None
    except PermissionError:
        print(f"  [ERROR] Permission denied: {path!r}")
        return None
    except OSError as e:
        print(f"  [ERROR] OS error reading {path!r}: {e}")
        return None

content = safe_read(filepath)
print(f"  Read {len(content)} characters from existing file")

content = safe_read(demo_path("nonexistent_file.txt"))
print(f"  Result for missing file: {content}")

# Using os.path.exists as a pre-check
def read_if_exists(path):
    if not os.path.isfile(path):
        return f"(file {path!r} does not exist)"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

print("  " + read_if_exists(demo_path("missing.txt")))

# Cleanup demo files
for fname in ["demo_output.txt", "demo_append.txt", "demo_data.csv", "demo_data.json"]:
    p = demo_path(fname)
    if os.path.exists(p):
        os.remove(p)
print("\n  Demo files cleaned up.")
