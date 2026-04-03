# 07 – Strings & Text Processing: Key Points

## Slicing Syntax

```
s[start : stop : step]
  start  — inclusive (default 0)
  stop   — exclusive (default len(s))
  step   — default 1; negative reverses direction
```

| Pattern | Result |
|---|---|
| `s[1:4]` | Characters at index 1, 2, 3 |
| `s[:3]` | First 3 characters |
| `s[-3:]` | Last 3 characters |
| `s[::2]` | Every other character |
| `s[::-1]` | Reverse the string |

## Most-Used String Methods

```python
s.upper()            s.lower()            s.title()
s.strip()            s.lstrip()           s.rstrip()
s.split(sep)         sep.join(iterable)
s.replace(old, new)
s.startswith(p)      s.endswith(p)
s.find(sub)          s.index(sub)         s.count(sub)
s.isdigit()          s.isalpha()          s.isalnum()
s.isspace()          s.islower()          s.isupper()
s.center(w, fill)    s.ljust(w)           s.rjust(w)    s.zfill(w)
```

## f-string Format Mini-Language

```
{value : fill align width . precision type}

{name:<20}      left-align, width 20
{n:>10.2f}      right-align, width 10, 2 decimal float
{n:08b}         binary, zero-padded width 8
{n:,}           integer with thousands separator
{n:.2%}         percentage with 2 decimal places
{val!r}         call repr() on the value
{val=}          debug: prints "val=<value>" (Python 3.8+)
```

## Regex Patterns Quick Reference

```
.     any char (not \n)    \d  digit       \D  non-digit
\w    word char            \W  non-word    \s  whitespace   \S  non-ws
^     start of string      $   end of string
*     0 or more            +   1 or more   ?   0 or 1
{n}   exactly n            {n,m} n to m
[abc] char class           [^abc] negated class
(...)  capturing group     (?:...) non-capturing group
(?P<name>...)  named group
```

## Core re Functions

```python
import re

re.match(r"pattern", s)           # match at START only
re.search(r"pattern", s)          # first match anywhere
re.findall(r"pattern", s)         # list of all matches
re.finditer(r"pattern", s)        # iterator of match objects
re.sub(r"pattern", replacement, s)  # replace matches
re.split(r"pattern", s)           # split on pattern

m = re.search(r"(\d+)-(\d+)", s)
m.group(0)    # entire match
m.group(1)    # first capture group
m.groups()    # tuple of all groups
m.start()     # start index of match
m.end()       # end index of match
```

## Quick Reminders

- Strings are **immutable** — all methods return new strings.
- `"".join(list)` is O(n); concatenation in a loop is O(n²).
- `split()` (no arg) handles any whitespace; `split(" ")` splits on single space.
- `find()` returns -1 if not found; `index()` raises `ValueError`.
- Always use raw strings (`r"..."`) for regex patterns.
- Compile patterns (`re.compile`) for reuse in loops.
