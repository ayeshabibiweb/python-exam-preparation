# 07 – Strings & Text Processing

## Overview

Strings are one of Python's most-used data types. They are **immutable** sequences of Unicode characters, packed with methods for searching, transforming, and validating text. Together with the `re` module for regular expressions, Python provides a rich toolkit for any text processing task.

---

## String Immutability

Once created, a string's content cannot be changed. Any operation that appears to modify a string actually creates a new one.

```python
s = "hello"
s[0] = "H"    # TypeError: 'str' object does not support item assignment
s = "H" + s[1:]  # correct: build a new string
```

This means strings are safe to use as dictionary keys and in sets.

---

## String Indexing and Slicing

Strings support integer indexing (0-based) and negative indexing (from the end).

```python
s = "Python"
s[0]    # "P"
s[-1]   # "n"
```

**Slice syntax**: `s[start:stop:step]`

- `start` is inclusive; `stop` is exclusive.
- Defaults: `start=0`, `stop=len(s)`, `step=1`.
- Negative step reverses direction.

```python
s[1:4]    # "yth"
s[:3]     # "Pyt"
s[::2]    # "Pto"   (every other character)
s[::-1]   # "nohtyP" (reverse)
```

---

## Essential String Methods

| Method | Description | Example |
|---|---|---|
| `.upper()` / `.lower()` | Case conversion | `"hi".upper()` → `"HI"` |
| `.strip()` / `.lstrip()` / `.rstrip()` | Remove whitespace (or chars) | `"  hi  ".strip()` → `"hi"` |
| `.split(sep)` | Split into list | `"a,b,c".split(",")` → `["a","b","c"]` |
| `.join(iterable)` | Join list into string | `"-".join(["a","b"])` → `"a-b"` |
| `.replace(old, new)` | Replace substrings | `"abc".replace("b","X")` → `"aXc"` |
| `.find(sub)` | Index of first occurrence (-1 if absent) | `"hello".find("l")` → `2` |
| `.index(sub)` | Like find but raises `ValueError` | `"hello".index("l")` → `2` |
| `.count(sub)` | Count non-overlapping occurrences | `"banana".count("a")` → `3` |
| `.startswith(prefix)` | True if string starts with prefix | `"Hello".startswith("He")` → `True` |
| `.endswith(suffix)` | True if string ends with suffix | `"file.txt".endswith(".txt")` → `True` |
| `.isdigit()` | True if all chars are digits | `"123".isdigit()` → `True` |
| `.isalpha()` | True if all chars are alphabetic | `"abc".isalpha()` → `True` |
| `.isalnum()` | True if all chars are alphanumeric | `"abc3".isalnum()` → `True` |
| `.isspace()` | True if all chars are whitespace | `"   ".isspace()` → `True` |
| `.title()` | Title case | `"hello world".title()` → `"Hello World"` |
| `.capitalize()` | First char upper, rest lower | `"hELLO".capitalize()` → `"Hello"` |
| `.zfill(width)` | Zero-pad on the left | `"42".zfill(5)` → `"00042"` |
| `.center(w, fill)` | Centre in field of width `w` | `"hi".center(10, "-")` → `"----hi----"` |

---

## String Formatting

### f-strings (Python 3.6+) — Preferred

```python
name = "Alice"
score = 95.678
f"Name: {name}, Score: {score:.2f}"
```

### .format() Method

```python
"{} scored {:.1f}".format("Alice", 95.678)
"{name}: {score}".format(name="Alice", score=95)
```

### % Legacy Formatting

```python
"Name: %s, Score: %.2f" % ("Alice", 95.678)
```

---

## Raw Strings

Prefix `r` disables backslash escape processing. Ideal for regex patterns and Windows paths.

```python
path  = r"C:\Users\Alice\Documents"
regex = r"\d{4}-\d{2}-\d{2}"    # no need to escape backslashes
```

---

## Multiline Strings

Triple quotes preserve newlines and are also used for docstrings.

```python
poem = """Roses are red,
Violets are blue,
Python is great,
And so are you."""
```

---

## String Concatenation and Repetition

```python
"Hello" + " " + "World"   # concatenation
"ha" * 3                   # "hahaha"
```

Concatenation in a loop is slow (O(n²)); use `"".join(parts)` instead.

---

## Regular Expressions (re module)

Regular expressions describe patterns in text. Import with `import re`.

### Core Functions

| Function | Returns | When to use |
|---|---|---|
| `re.match(pattern, s)` | match object or `None` | Pattern at the **start** of string |
| `re.search(pattern, s)` | match object or `None` | First match **anywhere** in string |
| `re.findall(pattern, s)` | list of strings | All non-overlapping matches |
| `re.finditer(pattern, s)` | iterator of match objects | All matches with position info |
| `re.sub(pattern, repl, s)` | new string | Replace matches |
| `re.split(pattern, s)` | list of strings | Split on pattern |

### Common Pattern Tokens

| Token | Matches |
|---|---|
| `.` | Any character except newline |
| `\d` | Digit `[0-9]` |
| `\D` | Non-digit |
| `\w` | Word character `[a-zA-Z0-9_]` |
| `\W` | Non-word character |
| `\s` | Whitespace |
| `\S` | Non-whitespace |
| `^` | Start of string |
| `$` | End of string |
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 |
| `{n,m}` | Between n and m occurrences |
| `[abc]` | Any of a, b, c |
| `[^abc]` | Not a, b, or c |
| `(...)` | Capturing group |
| `(?:...)` | Non-capturing group |

### Flags

```python
re.search(pattern, s, re.IGNORECASE)
re.IGNORECASE | re.MULTILINE
```

### Compiled Patterns

For patterns used repeatedly, compile first for efficiency:

```python
pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
pattern.findall("Dates: 2024-01-15 and 2025-03-22")
```

---

## Common Text Processing Patterns

```python
# Check if string is a valid email (simplified)
bool(re.match(r"^[\w.+-]+@[\w-]+\.[a-z]{2,}$", email, re.I))

# Extract all numbers from text
re.findall(r"\d+\.?\d*", "I have 3 cats and 2.5 dogs")

# Remove all HTML tags
re.sub(r"<[^>]+>", "", "<b>Hello</b> <i>World</i>")

# Split on multiple delimiters
re.split(r"[,;|]", "a,b;c|d")
```

---

## Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Trying to mutate a string | `s[0] = "X"` → TypeError | Build a new string |
| Using `find()` without checking -1 | Off-by-one or negative index | Check `if idx != -1:` |
| Forgetting `r""` in regex | `\d` becomes backspace + d | Use raw strings for patterns |
| Using `+` in a loop | O(n²) performance | Use `"".join(list)` |
| Confusing `split()` vs `split(" ")` | `split()` handles any whitespace; `split(" ")` splits on single spaces only | Use `split()` for robust whitespace handling |
| `match` vs `search` | `match` only checks start of string | Use `search` for arbitrary position |

---

## Summary

- Strings are immutable; all methods return new strings.
- Master slicing: `[start:stop:step]` — negative step reverses.
- `split()` / `join()` are your friends for parsing and building text.
- Use f-strings for clean formatting in modern Python.
- The `re` module handles complex pattern matching; prefer raw strings for patterns.
- Compile regex patterns (`re.compile`) when using them repeatedly.
