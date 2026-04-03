# Key Points — Topic 01: Programming Fundamentals

Quick-reference cheat sheet. Review this before your exam.

---

## Python Syntax Rules

| Rule | Detail |
|------|--------|
| Indentation | 4 spaces per level (not tabs) |
| Block delimiter | Colon `:` opens a block |
| Statement terminator | Newline (no semicolons needed) |
| Line continuation | `\` or implicit inside `()`, `[]`, `{}` |
| Comments | `#` to end of line |
| Case sensitivity | `Name` ≠ `name` ≠ `NAME` |

---

## Variable Naming Rules

**Must:**
- Start with a letter or `_`
- Contain only letters, digits, `_`
- Not be a keyword (`if`, `for`, `while`, `class`, `def`, `return`, `True`, `False`, `None`, …)

**Conventions (PEP 8):**

```
variables / functions  →  snake_case         e.g. user_age
constants              →  UPPER_SNAKE_CASE   e.g. MAX_SIZE
classes                →  PascalCase         e.g. BankAccount
"private" internal     →  _single_leading    e.g. _helper
```

---

## Assignment Forms

```python
x = 10                      # basic assignment
x = y = z = 0               # chained assignment
a, b = 1, 2                 # tuple unpacking
a, b = b, a                 # swap (no temp variable)
head, *rest = [1, 2, 3, 4]  # extended unpacking
```

---

## print() Quick Reference

```python
print(value)                         # basic
print(v1, v2, v3)                    # multiple values, space-separated
print(v1, v2, sep=", ")              # custom separator
print("done", end="")                # suppress newline
print(f"x = {x:.2f}")               # f-string with format spec
print("{:.2f}".format(x))           # str.format()
```

### Common Format Specifiers

| Spec | Meaning | Example |
|------|---------|---------|
| `:.2f` | 2 decimal places | `3.14` |
| `:d` | Integer | `42` |
| `:>10` | Right-align in 10 chars | `        42` |
| `:<10` | Left-align in 10 chars | `42        ` |
| `:^10` | Centre in 10 chars | `    42    ` |
| `:,` | Thousands separator | `1,000,000` |

---

## Common Built-in Functions

```python
print(x)          # display output
input("prompt")   # read string from user (always str)
type(x)           # return type of x
isinstance(x, T)  # True if x is an instance of T
int(x)            # convert to int
float(x)          # convert to float
str(x)            # convert to str
len(x)            # length of str/list/etc.
abs(x)            # absolute value
round(x, n)       # round to n decimal places
id(x)             # memory address of object
```

---

## Arithmetic Operators

| Op | Name | Example | Result |
|----|------|---------|--------|
| `+` | Add | `3 + 2` | `5` |
| `-` | Subtract | `3 - 2` | `1` |
| `*` | Multiply | `3 * 2` | `6` |
| `/` | True divide | `7 / 2` | `3.5` |
| `//` | Floor divide | `7 // 2` | `3` |
| `%` | Modulo | `7 % 2` | `1` |
| `**` | Power | `2 ** 8` | `256` |

---

## Execution Model Summary

```
.py source file
      ↓  (CPython compiles)
bytecode (.pyc in __pycache__/)
      ↓  (Python Virtual Machine runs)
      output
```

---

## Common Pitfalls

```python
# input() always returns str — cast when needed
age = int(input("Age: "))        # correct
age = input("Age: ")             # age is a str, not int

# = is assignment, == is comparison
if x == 5:  ...   # correct
if x = 5:   ...   # SyntaxError

# Don't shadow built-ins
list = [1, 2]     # BAD — overwrites list type
numbers = [1, 2]  # GOOD

# Indentation must be consistent
if True:
    x = 1
   y = 2   # IndentationError — inconsistent
```

---

## Tips and Tricks

- `type(x).__name__` gives just the type name as a string: `'int'`, `'str'`, etc.
- `print(*my_list)` unpacks a list as separate arguments to print
- `f"{value!r}"` uses `repr()` representation inside an f-string (shows quotes for strings)
- `_` is a valid variable name, conventionally used to discard a value: `_, useful = some_pair`
- Long variable names are fine — clarity beats brevity in most cases
