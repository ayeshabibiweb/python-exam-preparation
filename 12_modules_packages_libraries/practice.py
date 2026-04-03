"""
12 – Modules, Packages, and Libraries: Practice Problems
=========================================================
Each problem is stated as a comment block, followed by the full solution.
Run this file directly:  python practice.py
All solutions use only the Python standard library.
"""


# ===========================================================================
# Problem 1 – os module: directory explorer
# ===========================================================================
# Write a function list_python_files(directory) that:
#   - Returns a sorted list of all .py files in the given directory
#   - For each file, returns a tuple (filename, size_in_bytes)
#   - If the directory does not exist, return an empty list
# ===========================================================================

import os


def list_python_files(directory: str) -> list:
    """Return sorted list of (filename, bytes) for .py files in directory."""
    if not os.path.isdir(directory):
        return []
    result = []
    for name in os.listdir(directory):
        if name.endswith(".py"):
            full_path = os.path.join(directory, name)
            if os.path.isfile(full_path):
                result.append((name, os.path.getsize(full_path)))
    return sorted(result)


def test_problem1():
    print("=== Problem 1: Directory Explorer ===")
    files = list_python_files(".")
    print(f"  Python files in '.': {len(files)} found")
    for name, size in files:
        print(f"    {name:30s} {size:,} bytes")

    print(f"  Non-existent dir: {list_python_files('/no/such/path')}")


# ===========================================================================
# Problem 2 – json module: config serialiser
# ===========================================================================
# Write:
#   save_config(data: dict) -> str   – serialise to JSON string (pretty)
#   load_config(text: str) -> dict   – parse JSON string; raise ValueError
#     with descriptive message on malformed JSON
# ===========================================================================

import json


def save_config(data: dict) -> str:
    """Serialise config dict to a pretty-printed JSON string."""
    return json.dumps(data, indent=2, sort_keys=True)


def load_config(text: str) -> dict:
    """
    Parse JSON config text into a dict.

    Raises:
        ValueError: if text is not valid JSON.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid config JSON: {e}") from e


def test_problem2():
    print("\n=== Problem 2: JSON Config ===")
    config = {
        "database": {"host": "localhost", "port": 5432},
        "debug": True,
        "allowed_hosts": ["localhost", "127.0.0.1"],
    }
    serialised = save_config(config)
    print(f"  Saved:\n{serialised}")

    loaded = load_config(serialised)
    print(f"  Loaded host: {loaded['database']['host']}")
    print(f"  Roundtrip equal: {config == loaded}")

    try:
        load_config("{broken json")
    except ValueError as e:
        print(f"  Malformed JSON error: {e}")


# ===========================================================================
# Problem 3 – re module: log parser
# ===========================================================================
# Given lines from a web server log in the format:
#   "2024-06-15 14:30:22 GET /api/users 200 0.032s"
# Write parse_log_line(line) that returns a dict with keys:
#   timestamp, method, path, status, duration
# Return None if the line doesn't match the expected format.
# ===========================================================================

import re


LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
    r"(?P<method>GET|POST|PUT|DELETE|PATCH)\s+"
    r"(?P<path>/\S*)\s+"
    r"(?P<status>\d{3})\s+"
    r"(?P<duration>[\d.]+)s$"
)


def parse_log_line(line: str) -> dict:
    """Parse a log line; return dict or None if not matching."""
    m = LOG_PATTERN.match(line.strip())
    if m is None:
        return None
    d = m.groupdict()
    d["status"]   = int(d["status"])
    d["duration"] = float(d["duration"])
    return d


def test_problem3():
    print("\n=== Problem 3: Log Parser ===")
    lines = [
        "2024-06-15 14:30:22 GET /api/users 200 0.032s",
        "2024-06-15 14:30:25 POST /api/login 201 0.115s",
        "2024-06-15 14:30:26 GET /api/missing 404 0.008s",
        "this line is malformed",
        "2024-06-15 14:30:27 DELETE /api/users/5 204 0.021s",
    ]
    for line in lines:
        parsed = parse_log_line(line)
        if parsed:
            print(f"  {parsed['method']:6s} {parsed['path']:20s} "
                  f"status={parsed['status']} dur={parsed['duration']}s")
        else:
            print(f"  UNRECOGNISED: {line!r}")


# ===========================================================================
# Problem 4 – datetime module: event scheduler
# ===========================================================================
# Write days_until(event_date_str) that:
#   - Parses a date string "YYYY-MM-DD"
#   - Returns the number of days until that date from today
#   - Returns negative number if the date is in the past
#   - Raises ValueError if the format is wrong
# ===========================================================================

from datetime import date, datetime


def days_until(event_date_str: str) -> int:
    """
    Return days between today and event_date_str ("YYYY-MM-DD").

    Raises:
        ValueError: if the string format is invalid.
    """
    try:
        event_date = datetime.strptime(event_date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(
            f"Invalid date format: {event_date_str!r}. Expected YYYY-MM-DD."
        )
    return (event_date - date.today()).days


def test_problem4():
    print("\n=== Problem 4: Event Scheduler ===")
    dates = [
        "2030-01-01",  # future
        "2020-01-01",  # past
        "not-a-date",  # invalid
    ]
    for d in dates:
        try:
            delta = days_until(d)
            direction = "from now" if delta >= 0 else "ago"
            print(f"  {d}: {abs(delta)} days {direction}")
        except ValueError as e:
            print(f"  Error: {e}")


# ===========================================================================
# Problem 5 – math module: statistics helper
# ===========================================================================
# Implement a Statistics class using only the math module (no statistics lib).
# Methods: mean, variance, std_dev, median, mode
# ===========================================================================

import math


class Statistics:
    """Basic descriptive statistics without the statistics module."""

    def __init__(self, data: list):
        if not data:
            raise ValueError("Data must not be empty")
        self._data = list(data)

    def mean(self) -> float:
        return sum(self._data) / len(self._data)

    def variance(self) -> float:
        mu = self.mean()
        return sum((x - mu) ** 2 for x in self._data) / len(self._data)

    def std_dev(self) -> float:
        return math.sqrt(self.variance())

    def median(self) -> float:
        sorted_data = sorted(self._data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return float(sorted_data[mid])

    def mode(self):
        counts = {}
        for x in self._data:
            counts[x] = counts.get(x, 0) + 1
        max_count = max(counts.values())
        modes = [k for k, v in counts.items() if v == max_count]
        return modes[0] if len(modes) == 1 else sorted(modes)


def test_problem5():
    print("\n=== Problem 5: Statistics Helper ===")
    data = [4, 7, 13, 2, 1, 7, 3, 9, 7, 11]
    stats = Statistics(data)
    print(f"  Data:    {sorted(data)}")
    print(f"  Mean:    {stats.mean():.2f}")
    print(f"  Median:  {stats.median():.2f}")
    print(f"  Mode:    {stats.mode()}")
    print(f"  Std Dev: {stats.std_dev():.2f}")


# ===========================================================================
# Problem 6 – random module: password generator
# ===========================================================================
# Write generate_password(length, use_digits, use_symbols) that:
#   - Generates a random password of the given length
#   - Always includes uppercase and lowercase letters
#   - Optionally includes digits and/or symbols
#   - Guarantees at least one character from each selected category
# ===========================================================================

import random
import string


def generate_password(length: int = 12,
                      use_digits: bool = True,
                      use_symbols: bool = True) -> str:
    """Generate a random password satisfying the given constraints."""
    if length < 4:
        raise ValueError("Password length must be at least 4")

    pool = string.ascii_lowercase + string.ascii_uppercase
    mandatory = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
    ]

    if use_digits:
        pool += string.digits
        mandatory.append(random.choice(string.digits))

    if use_symbols:
        symbols = "!@#$%^&*()-_=+"
        pool += symbols
        mandatory.append(random.choice(symbols))

    remaining = [random.choice(pool) for _ in range(length - len(mandatory))]
    password_chars = mandatory + remaining
    random.shuffle(password_chars)
    return "".join(password_chars)


def test_problem6():
    print("\n=== Problem 6: Password Generator ===")
    random.seed(99)  # reproducible for demo
    for _ in range(3):
        pwd = generate_password(16, use_digits=True, use_symbols=True)
        print(f"  {pwd}  (length={len(pwd)})")

    # Without symbols
    pwd_simple = generate_password(12, use_digits=True, use_symbols=False)
    print(f"  No symbols: {pwd_simple}")

    try:
        generate_password(3)
    except ValueError as e:
        print(f"  Too short: {e}")


# ===========================================================================
# Problem 7 – sys module: command-line argument simulator
# ===========================================================================
# Write a parse_args(argv: list) function that:
#   - Accepts a list of strings (simulating sys.argv)
#   - Parses --key=value pairs and positional arguments
#   - Returns (options: dict, positionals: list)
# ===========================================================================

def parse_args(argv: list) -> tuple:
    """
    Minimal argument parser.
    Returns (options_dict, positionals_list).
    """
    options     = {}
    positionals = []

    for arg in argv:
        if arg.startswith("--"):
            if "=" in arg:
                key, value = arg[2:].split("=", maxsplit=1)
                options[key] = value
            else:
                options[arg[2:]] = True     # flag with no value
        else:
            positionals.append(arg)

    return options, positionals


def test_problem7():
    print("\n=== Problem 7: Argument Parser ===")
    test_cases = [
        ["--host=localhost", "--port=5432", "--debug", "run", "server"],
        ["--output=report.txt", "input1.csv", "input2.csv"],
        [],
    ]
    for argv in test_cases:
        opts, pos = parse_args(argv)
        print(f"  argv:        {argv}")
        print(f"  options:     {opts}")
        print(f"  positionals: {pos}")
        print()


# ===========================================================================
# Problem 8 – Combining multiple modules: file size reporter
# ===========================================================================
# Write file_size_report(directory) that:
#   - Lists all files in the directory (non-recursive)
#   - Returns a JSON string with file stats:
#       { filename: {size_bytes, size_kb, extension, modified_date} }
# Uses: os, json, datetime
# ===========================================================================

from datetime import datetime as _datetime


def file_size_report(directory: str) -> str:
    """
    Build a JSON report of files in the directory.

    Raises:
        ValueError: if directory does not exist.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"Not a directory: {directory!r}")

    report = {}
    for name in sorted(os.listdir(directory)):
        path = os.path.join(directory, name)
        if not os.path.isfile(path):
            continue
        stat     = os.stat(path)
        _, ext   = os.path.splitext(name)
        mod_time = _datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
        report[name] = {
            "size_bytes":   stat.st_size,
            "size_kb":      round(stat.st_size / 1024, 2),
            "extension":    ext or "(none)",
            "modified_date": mod_time,
        }
    return json.dumps(report, indent=2)


def test_problem8():
    print("\n=== Problem 8: File Size Report ===")
    try:
        text = file_size_report(".")
        data = json.loads(text)
        print(f"  Files found: {len(data)}")
        for fname, info in list(data.items())[:3]:   # show first 3
            print(f"  {fname:30s} {info['size_kb']:>8.2f} KB  ({info['extension']})")
    except ValueError as e:
        print(f"  Error: {e}")


# ===========================================================================
# Problem 9 – re module: data extractor
# ===========================================================================
# Write extract_urls(text) that returns a sorted deduplicated list of
# all URLs starting with http:// or https:// found in the text.
# ===========================================================================

def extract_urls(text: str) -> list:
    """Extract all http(s) URLs from text. Returns sorted deduplicated list."""
    pattern = r"https?://[^\s\"\'<>]+"
    found   = re.findall(pattern, text)
    # Remove trailing punctuation (commas, periods, closing parens)
    cleaned = [url.rstrip(".,;:)!?") for url in found]
    return sorted(set(cleaned))


def test_problem9():
    print("\n=== Problem 9: URL Extractor ===")
    sample_text = """
    Visit our website at https://www.example.com for more info.
    Documentation: https://docs.example.com/api/v2 (updated daily).
    Also see http://legacy.example.com/old-api.
    Email admin@example.com (not a URL).
    Duplicate: https://www.example.com should appear once.
    """
    urls = extract_urls(sample_text)
    print(f"  Found {len(urls)} unique URLs:")
    for url in urls:
        print(f"    {url}")


# ===========================================================================
# Run all problems
# ===========================================================================
if __name__ == "__main__":
    test_problem1()
    test_problem2()
    test_problem3()
    test_problem4()
    test_problem5()
    test_problem6()
    test_problem7()
    test_problem8()
    test_problem9()
