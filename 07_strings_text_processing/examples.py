# 07 – Strings & Text Processing: Examples
# Run this file: python examples.py

import re

print("=" * 60)
print("EXAMPLE 1: String Indexing and Slicing")
print("=" * 60)

s = "Python 3.8+"

# Indexing
print(f"  s         = {s!r}")
print(f"  s[0]      = {s[0]!r}")      # first character
print(f"  s[-1]     = {s[-1]!r}")     # last character
print(f"  s[-4]     = {s[-4]!r}")     # 4th from end

# Slicing [start:stop:step]  (stop is exclusive)
print(f"  s[0:6]    = {s[0:6]!r}")    # "Python"
print(f"  s[:6]     = {s[:6]!r}")     # same (start defaults to 0)
print(f"  s[7:]     = {s[7:]!r}")     # "3.8+" (to end)
print(f"  s[::2]    = {s[::2]!r}")    # every 2nd character
print(f"  s[::-1]   = {s[::-1]!r}")   # reverse entire string
print(f"  s[1:8:2]  = {s[1:8:2]!r}")  # step 2 within range

# Practical: check if palindrome
def is_palindrome(word):
    return word == word[::-1]

words = ["racecar", "level", "python", "madam", "hello"]
for w in words:
    print(f"  is_palindrome({w!r}) = {is_palindrome(w)}")


print("\n" + "=" * 60)
print("EXAMPLE 2: Common String Methods")
print("=" * 60)

raw = "  Hello, World!  "

print(f"  original          : {raw!r}")
print(f"  .strip()          : {raw.strip()!r}")
print(f"  .lstrip()         : {raw.lstrip()!r}")
print(f"  .rstrip()         : {raw.rstrip()!r}")
print(f"  .upper()          : {raw.strip().upper()!r}")
print(f"  .lower()          : {raw.strip().lower()!r}")
print(f"  .title()          : {raw.strip().title()!r}")
print(f"  .capitalize()     : {raw.strip().capitalize()!r}")
print(f"  .replace(',', ';'): {raw.strip().replace(',', ';')!r}")

s = "banana"
print(f"\n  s = {s!r}")
print(f"  .count('a')       : {s.count('a')}")          # 3
print(f"  .find('na')       : {s.find('na')}")          # 2
print(f"  .find('xyz')      : {s.find('xyz')}")         # -1 (not found)
print(f"  .startswith('ban'): {s.startswith('ban')}")   # True
print(f"  .endswith('ana')  : {s.endswith('ana')}")     # True
print(f"  .zfill(10)        : {'42'.zfill(10)!r}")      # '0000000042'
print(f"  .center(11, '-')  : {'hi'.center(11, '-')!r}")


print("\n" + "=" * 60)
print("EXAMPLE 3: String Formatting Methods")
print("=" * 60)

name  = "Alice"
score = 95.6789
rank  = 1

# f-strings (preferred, Python 3.6+)
print(f"  f-string: {name} scored {score:.2f}, rank #{rank:03d}")

# .format() — positional
print("  format positional: {} scored {:.2f}".format(name, score))

# .format() — named
print("  format named: {n} scored {s:.2f}".format(n=name, s=score))

# % style (legacy)
print("  %%-style: %s scored %.2f, rank #%03d" % (name, score, rank))

# Alignment
headers = ["Name", "Score", "Rank"]
rows    = [("Alice", 95.7, 1), ("Bob", 82.3, 3), ("Carol", 88.1, 2)]
print()
print(f"  {'Name':<10} {'Score':>7} {'Rank':>5}")
print("  " + "-" * 25)
for n, sc, rk in rows:
    print(f"  {n:<10} {sc:>7.1f} {rk:>5}")


print("\n" + "=" * 60)
print("EXAMPLE 4: String Splitting and Joining")
print("=" * 60)

csv_line = "Alice,21,Computer Science,3.8"
parts = csv_line.split(",")
print(f"  split on ','    : {parts}")
print(f"  parts[0]        : {parts[0]!r}")
print(f"  parts[-1]       : {parts[-1]!r}")

# maxsplit parameter
text = "one two three four five"
print(f"  split maxsplit=2: {text.split(' ', maxsplit=2)}")

# split() with no argument splits on any whitespace
messy = "  hello\t world \n  python  "
print(f"  split() on messy: {messy.split()}")

# join — the inverse of split
words = ["Python", "is", "awesome"]
print(f"  ' '.join()   : {' '.join(words)!r}")
print(f"  '-'.join()   : {'-'.join(words)!r}")
print(f"  ''.join()    : {''.join(words)!r}")

# Building CSV line
row = ["Bob", "22", "Physics", "3.5"]
print(f"  CSV re-join  : {','.join(row)!r}")

# Efficient string building
parts = ["Hello"] + [str(i) for i in range(5)]
result = " | ".join(parts)
print(f"  efficient build: {result!r}")


print("\n" + "=" * 60)
print("EXAMPLE 5: String Searching (find, index, in)")
print("=" * 60)

text = "The quick brown fox jumps over the lazy dog"

# Membership test — fastest
print(f"  'fox' in text      : {'fox' in text}")
print(f"  'cat' in text      : {'cat' in text}")

# find() — returns index or -1
idx = text.find("fox")
print(f"  text.find('fox')   : {idx}")
print(f"  text[{idx}:{idx+3}]         : {text[idx:idx+3]!r}")
print(f"  text.find('cat')   : {text.find('cat')}")   # -1

# rfind() — searches from right
sentence = "she sells sea shells by the sea shore"
print(f"  rfind('sea')       : {sentence.rfind('sea')}")   # last occurrence

# index() — raises ValueError if not found
try:
    pos = text.index("lazy")
    print(f"  text.index('lazy') : {pos}")
    text.index("cat")  # will raise
except ValueError as e:
    print(f"  text.index('cat')  : ValueError — {e}")

# count occurrences
print(f"  count('the')       : {text.lower().count('the')}")


print("\n" + "=" * 60)
print("EXAMPLE 6: String Testing Methods")
print("=" * 60)

test_strings = [
    "123",
    "abc",
    "abc123",
    "  ",
    "",
    "Hello World",
    "hello world",
    "HELLO",
    "Hello",
]

print(f"  {'string':<15} {'isdigit':>8} {'isalpha':>8} {'isalnum':>8} {'isspace':>8} {'islower':>8} {'isupper':>8} {'istitle':>8}")
print("  " + "-" * 72)
for s in test_strings:
    print(f"  {s!r:<15} {str(s.isdigit()):>8} {str(s.isalpha()):>8} "
          f"{str(s.isalnum()):>8} {str(s.isspace()):>8} "
          f"{str(s.islower()):>8} {str(s.isupper()):>8} {str(s.istitle()):>8}")


print("\n" + "=" * 60)
print("EXAMPLE 7: Regular Expressions — Basic Matching")
print("=" * 60)

# re.match — only matches at the START of the string
# re.search — finds FIRST match anywhere
email = "user@example.com"
phone = "+44-7911-123456"
date  = "2024-07-04"

email_pattern = r"^[\w.+-]+@[\w-]+\.[a-z]{2,}$"
phone_pattern = r"^\+?\d[\d\-\s]{8,}\d$"
date_pattern  = r"^\d{4}-\d{2}-\d{2}$"

print(f"  email match  : {bool(re.match(email_pattern, email, re.I))}")
print(f"  phone match  : {bool(re.match(phone_pattern, phone))}")
print(f"  date match   : {bool(re.match(date_pattern,  date))}")

# re.search — find first match anywhere
text = "Contact us at support@example.com or info@test.org for help."
m = re.search(r"[\w.+-]+@[\w-]+\.\w{2,}", text)
if m:
    print(f"  First email found : {m.group()!r}")
    print(f"  At position       : {m.start()}–{m.end()}")


print("\n" + "=" * 60)
print("EXAMPLE 8: Regular Expressions — findall and Groups")
print("=" * 60)

text = "Order 1024 placed on 2024-01-15. Order 2048 placed on 2024-02-20."

# findall — returns list of strings (or tuples when groups are used)
order_ids = re.findall(r"\d+", text)
print(f"  All numbers         : {order_ids}")

# With groups — each match is a tuple of group values
# Capture order_id and date separately
pattern = r"Order (\d+) placed on (\d{4}-\d{2}-\d{2})"
matches = re.findall(pattern, text)
print(f"  Order, Date pairs   : {matches}")

# finditer — match objects with position info
for m in re.finditer(pattern, text):
    oid, date = m.groups()
    print(f"  Order #{oid} on {date} (chars {m.start()}-{m.end()})")

# re.sub — replace matches
cleaned = re.sub(r"\d+", "###", "Phone: 07700 123456, PIN: 1234")
print(f"  Redacted numbers    : {cleaned!r}")

# Named groups
ip_pattern = r"(?P<a>\d{1,3})\.(?P<b>\d{1,3})\.(?P<c>\d{1,3})\.(?P<d>\d{1,3})"
m = re.match(ip_pattern, "192.168.1.100")
if m:
    print(f"  IP octets: {m.group('a')}, {m.group('b')}, {m.group('c')}, {m.group('d')}")


print("\n" + "=" * 60)
print("EXAMPLE 9: Text Parsing Example")
print("=" * 60)

# Parse a simple log line format:
# [2024-01-15 10:32:45] ERROR in module_name: message text
log_lines = [
    "[2024-01-15 10:32:45] INFO  in auth: User Alice logged in",
    "[2024-01-15 10:33:01] ERROR in database: Connection timed out",
    "[2024-01-15 10:33:45] WARN  in cache: Cache miss for key user_42",
    "[2024-01-15 10:34:00] INFO  in auth: User Bob logged out",
]

log_pattern = re.compile(
    r"\[(?P<timestamp>[^\]]+)\]\s+"
    r"(?P<level>\w+)\s+"
    r"in (?P<module>\w+):\s+"
    r"(?P<message>.+)"
)

parsed = []
for line in log_lines:
    m = log_pattern.match(line)
    if m:
        parsed.append(m.groupdict())

for entry in parsed:
    print(f"  [{entry['level']:<5}] {entry['module']}: {entry['message']}")

# Filter errors only
errors = [e for e in parsed if e["level"] == "ERROR"]
print(f"\n  Errors found: {len(errors)}")
for e in errors:
    print(f"    {e['timestamp']} — {e['message']}")


print("\n" + "=" * 60)
print("EXAMPLE 10: String Formatting with Numbers and Dates")
print("=" * 60)

from datetime import date, datetime

# Numbers
pi = 3.14159265358979
population = 8_000_000_000
ratio = 0.0382

print(f"  pi             : {pi:.6f}")
print(f"  pi (sci)       : {pi:e}")
print(f"  pi (sci 3dp)   : {pi:.3e}")
print(f"  population     : {population:,}")
print(f"  ratio          : {ratio:.2%}")    # as percentage
print(f"  padded int     : {42:010d}")
print(f"  hex            : {255:08x}")
print(f"  binary         : {42:08b}")

# Dates
today = date.today()
now   = datetime.now()
print(f"\n  date (ISO)     : {today.isoformat()}")
print(f"  date (custom)  : {today.strftime('%d %B %Y')}")
print(f"  datetime       : {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Aligning a summary table
metrics = [
    ("Accuracy", 0.9823),
    ("Precision", 0.9741),
    ("Recall", 0.9907),
    ("F1-Score", 0.9823),
]
print(f"\n  {'Metric':<12} {'Value':>8}")
print("  " + "-" * 22)
for metric, value in metrics:
    print(f"  {metric:<12} {value:>8.4f}")
