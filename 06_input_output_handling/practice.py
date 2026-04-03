# 06 – Input / Output Handling: Practice Problems
# Each problem states the task as a comment, followed by the full solution.
# Run this file: python practice.py
# File I/O uses the module's own directory for temporary files.

import os
import json
import csv

DEMO_DIR = os.path.dirname(os.path.abspath(__file__))

def demo_path(filename):
    return os.path.join(DEMO_DIR, filename)

created_files = []  # track files to clean up at end


print("=" * 60)
print("PROBLEM 1: Formatted Receipt Printer")
print("=" * 60)
# Write a function print_receipt(items, tax_rate=0.08) where
# items is a list of (name, price) tuples.
# Print a formatted receipt with:
#   - A header line
#   - Each item left-aligned (name 20 chars) with price right-aligned (8 chars, 2 dp)
#   - A separator line
#   - Subtotal, tax, and total lines
# Use f-strings throughout.

def print_receipt(items, tax_rate=0.08):
    width = 30
    print("=" * width)
    print(f"{'RECEIPT':^{width}}")
    print("=" * width)
    subtotal = 0.0
    for name, price in items:
        print(f"  {name:<18} {price:>7.2f}")
        subtotal += price
    tax = subtotal * tax_rate
    total = subtotal + tax
    print("-" * width)
    print(f"  {'Subtotal':<18} {subtotal:>7.2f}")
    print(f"  {'Tax ({:.0%})':<18} {tax:>7.2f}".format(tax_rate).replace(
        "Tax ({:.0%})".format(tax_rate),
        f"Tax ({tax_rate:.0%})"
    ))
    print(f"  {'TOTAL':<18} {total:>7.2f}")
    print("=" * width)

basket = [("Coffee", 3.50), ("Sandwich", 5.99), ("Juice", 2.75), ("Muffin", 1.80)]
print_receipt(basket)


print("\n" + "=" * 60)
print("PROBLEM 2: Safe Integer Input Reader")
print("=" * 60)
# Write a function read_positive_int(prompt, values) that simulates
# reading integers from a list of strings (to stay runnable without
# interactive input). It should:
# - Skip values that are not valid integers (print a warning)
# - Skip values that are <= 0 (print a warning)
# - Return the first valid positive integer found

def read_positive_int(prompt, values):
    """
    Simulate reading a positive integer interactively.
    values: list of strings to try in order.
    """
    for raw in values:
        print(f"  {prompt}{raw}")
        try:
            n = int(raw)
        except ValueError:
            print(f"  Warning: {raw!r} is not an integer. Try again.")
            continue
        if n <= 0:
            print(f"  Warning: {n} is not positive. Try again.")
            continue
        return n
    raise ValueError("No valid input found in provided values.")

result = read_positive_int("Enter a positive integer: ", ["abc", "-3", "0", "7"])
print(f"  Got valid input: {result}")


print("\n" + "=" * 60)
print("PROBLEM 3: Log File Writer")
print("=" * 60)
# Write a function log_event(filepath, level, message) that
# appends a line to a log file in the format:
#   [YYYY-MM-DD HH:MM:SS] LEVEL: message
# Use the datetime module for the timestamp.
# Then write read_log(filepath) that reads and returns all log lines.

from datetime import datetime

def log_event(filepath, level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {level.upper()}: {message}\n"
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(line)

def read_log(filepath):
    if not os.path.isfile(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.rstrip() for line in f]

log_file = demo_path("practice_log.txt")
created_files.append(log_file)

log_event(log_file, "INFO",    "Application started")
log_event(log_file, "warning", "Disk usage above 80%")
log_event(log_file, "ERROR",   "Failed to connect to database")

entries = read_log(log_file)
print(f"  {len(entries)} log entries:")
for entry in entries:
    print(f"  {entry}")


print("\n" + "=" * 60)
print("PROBLEM 4: CSV Student Report")
print("=" * 60)
# Given a list of student dictionaries, write them to a CSV file
# with columns: name, grade, passed (True/False based on grade >= 50).
# Then read the CSV back and print a summary: total students,
# number passed, class average grade.

students = [
    {"name": "Alice",  "grade": 88},
    {"name": "Bob",    "grade": 42},
    {"name": "Carol",  "grade": 75},
    {"name": "Dave",   "grade": 50},
    {"name": "Eve",    "grade": 95},
    {"name": "Frank",  "grade": 38},
]

csv_file = demo_path("practice_students.csv")
created_files.append(csv_file)

# Write
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "grade", "passed"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for s in students:
        writer.writerow({
            "name":   s["name"],
            "grade":  s["grade"],
            "passed": s["grade"] >= 50
        })
print(f"  Wrote {len(students)} students to {csv_file}")

# Read back and summarise
with open(csv_file, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

total   = len(rows)
passed  = sum(1 for r in rows if r["passed"] == "True")
average = sum(float(r["grade"]) for r in rows) / total

print(f"  Total students : {total}")
print(f"  Passed (≥50)   : {passed}")
print(f"  Class average  : {average:.1f}")


print("\n" + "=" * 60)
print("PROBLEM 5: JSON Config Manager")
print("=" * 60)
# Write two functions:
# - save_config(filepath, config_dict): saves a dict as formatted JSON
# - load_config(filepath, defaults=None): loads JSON; if file missing,
#   returns the defaults dict (or {} if no defaults given)
# Demonstrate round-trip with a config dict that includes nested values.

def save_config(filepath, config_dict):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(config_dict, f, indent=2)

def load_config(filepath, defaults=None):
    if defaults is None:
        defaults = {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return defaults

config_file = demo_path("practice_config.json")
created_files.append(config_file)

config = {
    "app": {"name": "MyApp", "version": "1.0.0", "debug": False},
    "database": {"host": "localhost", "port": 5432, "name": "mydb"},
    "features": ["auth", "logging", "cache"],
}

save_config(config_file, config)
loaded = load_config(config_file)
print(f"  App name    : {loaded['app']['name']}")
print(f"  DB port     : {loaded['database']['port']}")
print(f"  Features    : {loaded['features']}")

# Missing file returns defaults
missing = load_config(demo_path("no_such.json"), defaults={"theme": "dark"})
print(f"  Missing file defaults: {missing}")


print("\n" + "=" * 60)
print("PROBLEM 6: Word Frequency Counter from File")
print("=" * 60)
# Write write_text_file(filepath, text) to create a text file.
# Write word_frequency(filepath) that reads the file, splits into
# words (lowercased, stripping punctuation), and returns a dict
# mapping each word to its count, sorted by count descending.

import string

def write_text_file(filepath, text):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

def word_frequency(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    # Remove punctuation and split
    translator = str.maketrans("", "", string.punctuation)
    words = text.lower().translate(translator).split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items(), key=lambda kv: kv[1], reverse=True))

text_file = demo_path("practice_text.txt")
created_files.append(text_file)

sample = (
    "To be or not to be, that is the question. "
    "Whether 'tis nobler in the mind to suffer the "
    "slings and arrows of outrageous fortune, or to take "
    "arms against a sea of troubles."
)
write_text_file(text_file, sample)
freq = word_frequency(text_file)

print("  Top 8 words:")
for word, count in list(freq.items())[:8]:
    print(f"    {word!r:12} → {count}")


print("\n" + "=" * 60)
print("PROBLEM 7: Multi-File Copy with Error Handling")
print("=" * 60)
# Write a function copy_file(src, dst) that copies src to dst
# using file I/O (not shutil). Handle:
# - FileNotFoundError for missing source
# - Any OSError for other I/O problems
# Return True on success, False on failure.
# Demonstrate with both a valid and invalid source.

def copy_file(src, dst):
    try:
        with open(src, "r", encoding="utf-8") as fsrc:
            content = fsrc.read()
        with open(dst, "w", encoding="utf-8") as fdst:
            fdst.write(content)
        return True
    except FileNotFoundError as e:
        print(f"  [copy_file] Source not found: {e.filename}")
        return False
    except OSError as e:
        print(f"  [copy_file] OS error: {e}")
        return False

src_file = demo_path("practice_copy_src.txt")
dst_file = demo_path("practice_copy_dst.txt")
created_files.extend([src_file, dst_file])

write_text_file(src_file, "This is the source file content.\nLine 2.\n")

ok = copy_file(src_file, dst_file)
print(f"  copy valid file   → success={ok}")

with open(dst_file, "r", encoding="utf-8") as f:
    print(f"  Destination content: {f.read().strip()!r}")

ok = copy_file(demo_path("missing_src.txt"), dst_file)
print(f"  copy missing file → success={ok}")


print("\n" + "=" * 60)
print("PROBLEM 8: Print Table Formatter")
print("=" * 60)
# Write a function print_table(headers, rows, col_width=12) that
# prints a nicely aligned table to the console using f-strings.
# Each cell should be left-aligned and truncated to col_width chars.
# Include header separator lines.

def print_table(headers, rows, col_width=12):
    def cell(value, width):
        s = str(value)
        return s[:width].ljust(width)

    sep = "+" + "+".join("-" * (col_width + 2) for _ in headers) + "+"
    header_row = "| " + " | ".join(cell(h, col_width) for h in headers) + " |"
    print(sep)
    print(header_row)
    print(sep)
    for row in rows:
        data_row = "| " + " | ".join(cell(v, col_width) for v in row) + " |"
        print(data_row)
    print(sep)

headers = ["Name", "Score", "Grade", "Year"]
data = [
    ["Alice",       92,  "A",  2],
    ["Bob",         65,  "C",  1],
    ["Carol",       88,  "B",  3],
    ["Dave",        71,  "B-", 2],
    ["Eve (Honours)", 97, "A+", 4],
]
print_table(headers, data)

# Cleanup all created files
print("\n--- Cleaning up practice files ---")
for path in created_files:
    if os.path.exists(path):
        os.remove(path)
        print(f"  Removed: {os.path.basename(path)}")
