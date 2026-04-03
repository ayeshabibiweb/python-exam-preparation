"""
12 – Modules, Packages, and Libraries: Examples
================================================
Run this file directly:  python examples.py
All examples use only the Python standard library and are self-contained.
"""


# ---------------------------------------------------------------------------
# Example 1 – Import variations
# ---------------------------------------------------------------------------
def example1_import_variations():
    print("=== Example 1: Import Variations ===")

    # 1. import the whole module
    import math
    print(f"math.pi = {math.pi:.6f}")

    # 2. import with alias
    import datetime as dt
    print(f"Today: {dt.date.today()}")

    # 3. import specific names
    from math import sqrt, factorial
    print(f"sqrt(144) = {sqrt(144)}")
    print(f"7! = {factorial(7)}")

    # 4. import with alias
    from math import ceil as round_up
    print(f"round_up(3.2) = {round_up(3.2)}")

    # 5. multiple from one module
    from os.path import join, basename, dirname
    path = join("home", "user", "file.txt")
    print(f"join = {path!r}, base = {basename(path)!r}, dir = {dirname(path)!r}")


# ---------------------------------------------------------------------------
# Example 2 – os module usage
# ---------------------------------------------------------------------------
def example2_os_module():
    print("\n=== Example 2: os Module ===")
    import os

    cwd = os.getcwd()
    print(f"Current directory: {cwd}")

    # os.path utilities
    path = os.path.join("data", "2024", "report.csv")
    print(f"Joined path:  {path!r}")
    print(f"Basename:     {os.path.basename(path)!r}")
    print(f"Dirname:      {os.path.dirname(path)!r}")
    print(f"Splitext:     {os.path.splitext(path)}")

    # Absolute path
    print(f"Absolute cwd: {os.path.abspath('.')!r}")

    # Existence checks
    print(f"cwd exists:  {os.path.exists(cwd)}")
    print(f"cwd is dir:  {os.path.isdir(cwd)}")

    # Environment variable
    home = os.environ.get("HOME", os.environ.get("USERPROFILE", "unknown"))
    print(f"HOME = {home!r}")

    # List directory contents (top-level .py and .md files only)
    files = [f for f in os.listdir(".") if f.endswith((".py", ".md"))]
    print(f"Python/Markdown files in .: {sorted(files)}")


# ---------------------------------------------------------------------------
# Example 3 – sys module usage
# ---------------------------------------------------------------------------
def example3_sys_module():
    print("\n=== Example 3: sys Module ===")
    import sys

    print(f"Python version: {sys.version}")
    print(f"Platform:       {sys.platform}")
    print(f"Script name:    {sys.argv[0]}")
    print(f"Extra args:     {sys.argv[1:]}")   # empty if run without args

    # sys.path – first 3 entries to keep output short
    print(f"sys.path[:3]:   {sys.path[:3]}")

    # sys.getsizeof – inspect object size
    lst = list(range(1000))
    print(f"list(range(1000)) size: {sys.getsizeof(lst)} bytes")

    # sys.maxsize – largest int on this platform
    print(f"sys.maxsize:    {sys.maxsize:,}")


# ---------------------------------------------------------------------------
# Example 4 – json encoding and decoding (using strings, not files)
# ---------------------------------------------------------------------------
def example4_json():
    print("\n=== Example 4: json Module ===")
    import json

    # Python → JSON string
    student = {
        "name":    "Alice",
        "age":     21,
        "courses": ["Python", "Algorithms"],
        "active":  True,
        "gpa":     3.85,
        "advisor": None,
    }

    compact = json.dumps(student)
    pretty  = json.dumps(student, indent=2, sort_keys=True)
    print(f"Compact JSON: {compact}")
    print(f"Pretty JSON:\n{pretty}")

    # JSON string → Python
    parsed = json.loads(compact)
    print(f"\nParsed type: {type(parsed).__name__}")
    print(f"Name:        {parsed['name']}")
    print(f"Courses:     {parsed['courses']}")

    # Demonstrate type mapping
    types_demo = {"int": 1, "float": 1.5, "bool": True,
                  "null": None, "list": [1, 2], "nested": {"key": "val"}}
    roundtrip = json.loads(json.dumps(types_demo))
    print(f"\nRoundtrip equal: {types_demo == roundtrip}")


# ---------------------------------------------------------------------------
# Example 5 – re module usage
# ---------------------------------------------------------------------------
def example5_re_module():
    print("\n=== Example 5: re Module ===")
    import re

    text = "Contact us at support@example.com or sales@company.org for help."

    # search – find first match anywhere
    match = re.search(r"\b\w+@\w+\.\w+\b", text)
    if match:
        print(f"First email found: {match.group(0)}")

    # findall – all matches
    emails = re.findall(r"\b\w+@\w+\.\w+\b", text)
    print(f"All emails: {emails}")

    # sub – replace matches
    masked = re.sub(r"\b\w+@\w+\.\w+\b", "[REDACTED]", text)
    print(f"Masked: {masked}")

    # match – only at string start
    date_str = "2024-06-15 was a great day"
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", date_str)
    if m:
        print(f"Date groups: year={m.group(1)}, month={m.group(2)}, day={m.group(3)}")

    # split
    csv_line = "Alice,30,Engineer,London"
    parts = re.split(r",", csv_line)
    print(f"Split: {parts}")

    # Compiled pattern (efficient for repeated use)
    phone_pattern = re.compile(r"\d{3}-\d{4}")
    numbers = phone_pattern.findall("Call 555-1234 or 555-5678 for info")
    print(f"Phone numbers: {numbers}")


# ---------------------------------------------------------------------------
# Example 6 – datetime operations
# ---------------------------------------------------------------------------
def example6_datetime():
    print("\n=== Example 6: datetime Module ===")
    from datetime import date, datetime, timedelta

    # Current date and datetime
    today = date.today()
    now   = datetime.now()
    print(f"Today:   {today}")
    print(f"Now:     {now}")

    # Constructing specific dates
    birthday  = date(1990, 7, 4)
    christmas = datetime(2024, 12, 25, 9, 0, 0)
    print(f"Birthday:   {birthday}")
    print(f"Christmas:  {christmas}")

    # Date arithmetic
    one_week  = today + timedelta(weeks=1)
    yesterday = today - timedelta(days=1)
    print(f"Next week:  {one_week}")
    print(f"Yesterday:  {yesterday}")

    # Time until Christmas
    days_left = (christmas.date() - today).days
    print(f"Days until Christmas 2024: {days_left}")

    # Formatting
    formatted = now.strftime("%A, %B %d %Y at %H:%M")
    print(f"Formatted:  {formatted}")

    # Parsing
    parsed = datetime.strptime("2024-06-15 14:30", "%Y-%m-%d %H:%M")
    print(f"Parsed:     {parsed}")

    # Accessing components
    print(f"Year={now.year}, Month={now.month}, Day={now.day}, "
          f"Hour={now.hour}, Minute={now.minute}")


# ---------------------------------------------------------------------------
# Example 7 – math module
# ---------------------------------------------------------------------------
def example7_math():
    print("\n=== Example 7: math Module ===")
    import math

    print(f"pi = {math.pi}")
    print(f"e  = {math.e}")
    print(f"sqrt(2)     = {math.sqrt(2):.6f}")
    print(f"floor(3.7)  = {math.floor(3.7)}")
    print(f"ceil(3.2)   = {math.ceil(3.2)}")
    print(f"factorial(10) = {math.factorial(10):,}")
    print(f"log(1000, 10) = {math.log(1000, 10):.1f}")
    print(f"sin(pi/2)   = {math.sin(math.pi/2):.1f}")
    print(f"cos(0)      = {math.cos(0):.1f}")
    print(f"gcd(48, 18) = {math.gcd(48, 18)}")
    print(f"comb(10,3)  = {math.comb(10, 3)}")   # 10-choose-3
    print(f"inf         = {math.inf}")
    print(f"isfinite(1) = {math.isfinite(1)}")
    print(f"isnan(nan)  = {math.isnan(float('nan'))}")

    # Practical: Euclidean distance
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print(f"Distance (0,0)→(3,4) = {distance(0,0,3,4)}")  # 5.0


# ---------------------------------------------------------------------------
# Example 8 – random module
# ---------------------------------------------------------------------------
def example8_random():
    print("\n=== Example 8: random Module ===")
    import random

    # Seed for reproducibility in examples
    random.seed(42)

    print(f"random.random():        {random.random():.4f}")
    print(f"random.randint(1, 100): {random.randint(1, 100)}")
    print(f"random.uniform(0, 10):  {random.uniform(0, 10):.4f}")

    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"random.choice:    {random.choice(fruits)}")
    print(f"random.sample(3): {random.sample(fruits, 3)}")

    deck = list(range(1, 14))    # ace to king
    random.shuffle(deck)
    print(f"Shuffled deck (first 5): {deck[:5]}")

    # Simulate rolling two dice 5 times
    rolls = [(random.randint(1, 6), random.randint(1, 6)) for _ in range(5)]
    print(f"Dice rolls: {rolls}")
    print(f"Sums:       {[a+b for a,b in rolls]}")


# ---------------------------------------------------------------------------
# Example 9 – __name__ == "__main__" pattern
# ---------------------------------------------------------------------------
# When you import this file, the individual functions at the top level are
# defined but not called. When you run the file directly, the code inside
# the if __name__ == "__main__" block executes.

def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def example9_name_main_pattern():
    print("\n=== Example 9: __name__ == '__main__' Pattern ===")
    print(f"This module's __name__: {__name__!r}")
    # When run directly: __name__ == '__main__'
    # When imported:     __name__ == '12_modules_packages_libraries.examples'
    #                    (or just 'examples')

    # Demonstrate that greet() and add() are importable utilities
    print(greet("Student"))   # Hello, Student!
    print(f"add(2, 3) = {add(2, 3)}")


# ---------------------------------------------------------------------------
# Example 10 – Creating a simple module-like structure in-file
# ---------------------------------------------------------------------------
def example10_module_like_structure():
    print("\n=== Example 10: Module-like Structure ===")

    # Demonstrate how a package's __init__.py might organise exports
    # Here we simulate it within a single file using a class namespace

    class mathutils:
        """Simulates a small math utility module."""

        @staticmethod
        def clamp(value: float, lo: float, hi: float) -> float:
            """Clamp value to [lo, hi]."""
            return max(lo, min(value, hi))

        @staticmethod
        def lerp(a: float, b: float, t: float) -> float:
            """Linear interpolation between a and b by factor t in [0,1]."""
            return a + (b - a) * t

        @staticmethod
        def sign(x: float) -> int:
            """Return -1, 0, or 1."""
            return 0 if x == 0 else (1 if x > 0 else -1)

    class stringutils:
        """Simulates a small string utility module."""

        @staticmethod
        def palindrome(s: str) -> bool:
            clean = s.lower().replace(" ", "")
            return clean == clean[::-1]

        @staticmethod
        def word_count(text: str) -> dict:
            import re
            words = re.findall(r"\w+", text.lower())
            counts = {}
            for w in words:
                counts[w] = counts.get(w, 0) + 1
            return counts

    # Use the "modules"
    print(f"clamp(15, 0, 10) = {mathutils.clamp(15, 0, 10)}")
    print(f"lerp(0, 100, 0.3) = {mathutils.lerp(0, 100, 0.3)}")
    print(f"sign(-5) = {mathutils.sign(-5)}")

    print(f"palindrome('racecar') = {stringutils.palindrome('racecar')}")
    print(f"palindrome('hello')   = {stringutils.palindrome('hello')}")

    wc = stringutils.word_count("the cat sat on the mat and the cat")
    print(f"Word counts: {dict(sorted(wc.items(), key=lambda x: -x[1])[:4])}")


# ---------------------------------------------------------------------------
# Run all examples
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    example1_import_variations()
    example2_os_module()
    example3_sys_module()
    example4_json()
    example5_re_module()
    example6_datetime()
    example7_math()
    example8_random()
    example9_name_main_pattern()
    example10_module_like_structure()
