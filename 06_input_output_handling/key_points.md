# 06 – Input / Output Handling: Key Points

## print() Quick Reference

```python
print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)

print("a", "b", sep="-")    # a-b
print("no newline", end="") # stays on same line
```

## input() Quick Reference

```python
raw   = input("Prompt: ")        # always returns str
num   = int(input("Number: "))   # must cast explicitly
value = float(input("Float: "))
```

## String Formatting Cheat Sheet

| Style | Syntax | Example |
|---|---|---|
| f-string | `f"{var:.2f}"` | `f"{3.14159:.2f}"` → `"3.14"` |
| .format() | `"{:.2f}".format(val)` | `"{:>10}".format("hi")` → `"        hi"` |
| % legacy | `"%.2f" % val` | `"%.2f" % 3.14` → `"3.14"` |

### f-string Format Specifiers

```
{value:fill_char align width .precision type}

{name:<20}    left-align, width 20
{score:>8.2f} right-align, width 8, 2 dp float
{n:05d}       zero-pad integer to width 5
{n:,}         thousands separator
{n:#010x}     hex with 0x prefix, width 10
{n:08b}       binary, zero-padded width 8
```

## File Modes

| Mode | Create? | Truncate? | Read? | Write? | Pointer |
|---|---|---|---|---|---|
| `r` | No | No | ✓ | ✗ | Start |
| `w` | Yes | Yes | ✗ | ✓ | Start |
| `a` | Yes | No | ✗ | ✓ | End |
| `x` | Yes (fail if exists) | — | ✗ | ✓ | Start |
| `r+` | No | No | ✓ | ✓ | Start |
| `rb`/`wb` | — | — | — | — | Binary variants |

## File Reading Methods

```python
f.read()           # entire file as one string
f.readline()       # one line (includes \n)
f.readlines()      # list of all lines
for line in f:     # memory-efficient iteration (preferred)
```

## Context Manager Pattern

```python
with open("file.txt", "r", encoding="utf-8") as f:
    data = f.read()
# file is always closed here, even if an exception occurred
```

## Exception Handling for Files

```python
try:
    with open(path) as f: ...
except FileNotFoundError: ...
except PermissionError:   ...
except OSError as e:      ...
```

## JSON / CSV Quick Reference

```python
# JSON
import json
json.dumps(obj, indent=2)      # Python → JSON string
json.loads(s)                  # JSON string → Python
json.dump(obj, file_obj)       # Python → JSON file
json.load(file_obj)            # JSON file → Python

# CSV
import csv
csv.writer(f).writerow(row)            # write list row
csv.DictWriter(f, fieldnames=[...])    # write dict rows
csv.reader(f)                          # read list rows
csv.DictReader(f)                      # read dict rows (auto headers)
```

## Common Mistakes to Avoid

- Forgetting to cast `input()` result → `TypeError` at runtime
- Using `"w"` mode when you want to append → data loss
- Missing `newline=""` in CSV open → extra blank rows on Windows
- Missing `encoding="utf-8"` → crashes on non-ASCII text on some platforms
- Not using `with` statement → file handle leaked
