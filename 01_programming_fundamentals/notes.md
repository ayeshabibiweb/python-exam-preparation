# Topic 01 — Programming Fundamentals

## Overview

Programming fundamentals form the bedrock of every Python program you will ever write. This topic covers how Python programs are structured, how code is executed, how to store values, and the basic I/O tools you need to interact with a running program. A solid understanding here prevents the majority of beginner and intermediate mistakes.

---

## 1. Python Syntax Overview

### Indentation

Python uses **indentation** (whitespace at the start of a line) to define blocks of code, rather than curly braces `{}` as in C, Java, or JavaScript. This is not just a style preference — it is part of the language grammar.

```python
if True:
    print("This line is inside the if block")
print("This line is outside the if block")
```

The standard indentation is **4 spaces** per level (PEP 8 recommendation). Mixing tabs and spaces causes `TabError` exceptions. Configure your editor to insert spaces when you press Tab.

### Statements

A Python **statement** is a single logical instruction. Most statements occupy one line, but long statements can be continued across multiple lines using:

- A backslash `\` at the end of the line
- An implicit continuation inside brackets `()`, `[]`, or `{}`

```python
# Backslash continuation
result = 1 + 2 + 3 + \
         4 + 5

# Implicit continuation (preferred)
result = (1 + 2 + 3 +
          4 + 5)
```

### Comments

Comments start with `#` and extend to the end of the line. Python ignores them entirely — they exist only for human readers. Write comments that explain *why*, not *what* (the code already shows what).

```python
# Calculate the area of a circle
area = 3.14159 * radius ** 2  # radius squared then multiplied by pi
```

Multi-line comments are written as multiple single-line `#` comments. String literals used as standalone expressions (not assigned to anything) are sometimes used as block comments, but this is an informal convention.

---

## 2. Variables and Naming Conventions

A **variable** is a name that refers to a value stored in memory. In Python, variables are created the moment you assign a value to them — there is no separate declaration step.

```python
age = 21          # creates a variable called 'age' pointing to the integer 21
name = "Alice"    # creates a variable called 'name' pointing to the string "Alice"
```

### Naming Rules (enforced by Python)

- Must start with a letter (`a–z`, `A–Z`) or an underscore `_`
- Can contain letters, digits (`0–9`), and underscores
- Cannot contain spaces or special characters (`@`, `-`, `.`, etc.)
- Cannot be a Python **keyword** (`if`, `for`, `while`, `class`, `def`, etc.)
- Case-sensitive: `age`, `Age`, and `AGE` are three different variables

### Naming Conventions (PEP 8 — followed by the Python community)

| Use Case | Convention | Example |
|----------|-----------|---------|
| Regular variables & functions | `snake_case` | `user_name`, `calculate_area` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_SIZE`, `PI` |
| Classes | `PascalCase` | `BankAccount`, `UserProfile` |
| Private (internal) | Leading underscore | `_internal_value` |
| Very private | Double leading underscore | `__mangled_name` |

### Good Variable Names

Name variables by what they *represent*, not by their type. `user_count` is better than `integer1`. Short names like `i`, `j`, `k` are acceptable for loop counters. Names like `temp` or `data` are vague and should be avoided in non-trivial code.

---

## 3. Basic Data Flow

A Python program executes **top to bottom**, one statement at a time (unless redirected by control structures covered in Topic 04). Data flows through the program via variables:

```
Input → Process → Output
```

- **Input:** Values entered by the user (`input()`), read from a file, or defined as literals
- **Process:** Calculations, transformations, and decisions performed on that data
- **Output:** Results displayed to the user (`print()`) or written to a file

---

## 4. Code Execution Model

### How Python Runs Your Code

1. **Source file** (`.py`) — you write human-readable Python code
2. **Compilation** — CPython compiles source code to **bytecode** (`.pyc` files in `__pycache__/`)
3. **Interpretation** — the Python Virtual Machine (PVM) executes the bytecode instruction by instruction

This is why Python is called an *interpreted* language — you do not manually compile before running. The compilation to bytecode happens automatically and transparently.

### The REPL

The Python **REPL** (Read-Eval-Print Loop) is the interactive shell you get by running `python` or `python3` with no arguments. It reads one expression, evaluates it, prints the result, and loops. Excellent for quick experiments, but not a substitute for writing `.py` files.

---

## 5. The `print()` Function

`print()` is the primary tool for sending output to the terminal. Key parameters:

| Parameter | Default | Effect |
|-----------|---------|--------|
| `sep` | `' '` | Separator between multiple values |
| `end` | `'\n'` | String appended after the last value |
| `file` | `sys.stdout` | Where to write output |

```python
print("Hello", "World")           # Hello World
print("Hello", "World", sep="-")  # Hello-World
print("No newline", end="")       # no newline at end
print("A", "B", "C", sep=", ")   # A, B, C
```

---

## 6. Common Mistakes and How to Avoid Them

**Mistake 1: Inconsistent indentation**
Using 2 spaces in one block and 4 in another causes `IndentationError`. Configure your editor to always use 4 spaces.

**Mistake 2: Using a variable before assigning it**
`print(x)` before `x = 5` raises `NameError: name 'x' is not defined`. Python has no default value for uninitialized variables.

**Mistake 3: Confusing `=` (assignment) with `==` (equality)**
`if x = 5:` is a syntax error in Python (intentionally — this was a common bug source in C/Java).

**Mistake 4: Forgetting that `input()` always returns a string**
`age = input("Enter age: ")` gives you `"21"` (a string), not `21` (an integer). You must cast: `age = int(input("Enter age: "))`.

**Mistake 5: Shadowing built-in names**
Naming a variable `list`, `str`, `input`, or `print` overwrites the built-in and causes confusing errors later. Always use descriptive names.

---

## 7. Key Vocabulary

| Term | Definition |
|------|-----------|
| **Variable** | A name bound to a value in memory |
| **Assignment** | Binding a name to a value using `=` |
| **Literal** | A value written directly in code (`42`, `"hello"`, `True`) |
| **Expression** | Code that evaluates to a value (`2 + 3`, `len("hi")`) |
| **Statement** | A complete instruction (`x = 5`, `print(x)`) |
| **Keyword** | Reserved word with special meaning (`if`, `for`, `def`) |
| **Indentation** | Whitespace used to define code blocks |
| **Bytecode** | Compiled intermediate representation of Python source |
| **REPL** | Interactive Read-Eval-Print Loop |
| **PEP 8** | Python's official style guide |

---

## Summary

Python programs are composed of statements that execute top to bottom. Indentation defines code structure. Variables are untyped names that point to values, and they follow strict naming rules with community conventions layered on top. The execution model compiles source to bytecode before running it through the PVM. The `print()` function and `input()` function handle basic I/O. The most common beginner errors — mixed indentation, undefined variables, type confusion from `input()` — are all preventable with good habits established early.
