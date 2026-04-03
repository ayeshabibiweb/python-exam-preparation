# 06 – Input / Output Handling

## Overview

Handling input and output is fundamental to every real-world program. Python provides powerful, consistent tools for reading from users, formatting data as text, and working with files. This section covers console I/O, string formatting, file operations, context managers, and structured data formats.

---

## print() Function

`print()` accepts any number of positional arguments and several keyword arguments:

```python
print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)
```

| Parameter | Default | Purpose |
|---|---|---|
| `sep` | `" "` | Separator between objects |
| `end` | `"\n"` | String printed after all objects |
| `file` | `sys.stdout` | File-like object to write to |
| `flush` | `False` | Force flushing the stream buffer |

```python
print("a", "b", "c", sep="-")      # a-b-c
print("Loading", end="")
print(" ... done")                  # Loading ... done  (same line)
```

---

## input() Function

`input(prompt)` displays `prompt`, waits for the user to type something and press Enter, then returns the text as a **string**.

```python
name = input("Enter your name: ")
age  = int(input("Enter your age: "))   # always returns str; cast as needed
```

> **Important**: `input()` always returns a string. You must explicitly convert to `int`, `float`, etc.

---

## String Formatting

### f-strings (Python 3.6+) — Preferred

```python
name  = "Alice"
score = 95.678
f"Name: {name}, Score: {score:.2f}"   # "Name: Alice, Score: 95.68"
```

Format specifiers after `:` follow mini-language rules: `{value:width.precisiontype}`.

| Specifier | Meaning |
|---|---|
| `:.2f` | Float with 2 decimal places |
| `:>10` | Right-align in a field of width 10 |
| `:<10` | Left-align in a field of width 10 |
| `:^10` | Centre-align in a field of width 10 |
| `:,` | Thousand separator |
| `:05d` | Integer zero-padded to width 5 |

### .format() Method

```python
"{name} scored {score:.1f}".format(name="Bob", score=82.3)
"{0} and {1}".format("first", "second")
```

### % Formatting (Legacy)

```python
"Hello, %s! You are %d years old." % ("Alice", 21)
"Pi ≈ %.4f" % 3.14159
```

Still common in older codebases; prefer f-strings for new code.

---

## File Operations

### Opening Files

```python
open(file, mode="r", encoding="utf-8")
```

| Mode | Meaning |
|---|---|
| `"r"` | Read (default) — file must exist |
| `"w"` | Write — creates or truncates |
| `"a"` | Append — creates or appends |
| `"x"` | Exclusive create — fails if file exists |
| `"rb"` / `"wb"` | Binary read / write |
| `"r+"` | Read and write |

Always specify `encoding="utf-8"` for text files to avoid platform-dependent defaults.

### Reading Files

```python
f.read()            # read entire file as one string
f.readline()        # read one line (including \n)
f.readlines()       # read all lines into a list

for line in f:      # most memory-efficient way to iterate
    process(line)
```

### Writing Files

```python
f.write("some text\n")          # write a string; returns number of chars written
f.writelines(["line1\n", "line2\n"])  # write a sequence of strings
```

---

## Context Managers (with statement)

The `with` statement ensures the file is **always closed**, even if an exception occurs:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# f is automatically closed here
```

You can open multiple files in one `with` block:

```python
with open("input.txt") as src, open("output.txt", "w") as dst:
    dst.write(src.read())
```

---

## Exception Handling with Files

```python
try:
    with open("missing.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except OSError as e:
    print(f"OS error: {e}")
```

Common file-related exceptions: `FileNotFoundError`, `PermissionError`, `IsADirectoryError`, `OSError`.

---

## os.path for File Paths

```python
import os

os.path.join("folder", "file.txt")   # "folder/file.txt" (OS-aware)
os.path.exists("file.txt")           # True / False
os.path.isfile("file.txt")           # True if it exists and is a file
os.path.isdir("folder")              # True if it exists and is a directory
os.path.basename("/a/b/c.txt")       # "c.txt"
os.path.dirname("/a/b/c.txt")        # "/a/b"
os.path.splitext("report.csv")       # ("report", ".csv")
```

For modern code, prefer `pathlib.Path` over `os.path`.

---

## CSV Basics

```python
import csv

# Reading
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# Writing
with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 21})
```

Always pass `newline=""` when opening CSV files to let the `csv` module handle line endings.

---

## JSON Basics

```python
import json

# Serialise Python → JSON string
json_str = json.dumps({"name": "Alice", "scores": [90, 85]}, indent=2)

# Parse JSON string → Python object
data = json.loads(json_str)

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read from file
with open("data.json") as f:
    data = json.load(f)
```

JSON supports: `str`, `int`, `float`, `bool`, `None`, `list`, `dict`. Python's `tuple` becomes a JSON array.

---

## Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Not closing files | Resource leak | Use `with` statement |
| Forgetting to cast `input()` | `"5" + 3` raises `TypeError` | `int(input(...))` |
| Opening in `"w"` instead of `"a"` | Overwrites existing content | Use `"a"` to append |
| Missing `newline=""` in CSV | Extra blank lines on Windows | Always pass `newline=""` |
| Not specifying `encoding` | Works on dev, breaks on other OS | `encoding="utf-8"` |
| Catching all exceptions | Hides real bugs | Catch specific exceptions |

---

## Summary

- `print()` and `input()` are your primary console I/O tools.
- Use f-strings for clean, readable string formatting.
- Always open files with `with` to guarantee they are closed.
- Specify `encoding="utf-8"` for portable text files.
- `csv` and `json` modules handle structured data cleanly.
