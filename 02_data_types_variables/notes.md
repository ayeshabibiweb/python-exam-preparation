# Topic 02 — Data Types and Variables

## Overview

Understanding Python's type system is essential for writing correct programs. This topic covers the five built-in primitive types, how Python stores values in memory, how to convert between types, and how scope determines where a variable is visible. These concepts underpin almost every bug related to "wrong value" or "NameError" you will encounter.

---

## 1. The Five Primitive Types

### `int` — Integer

Integers are whole numbers with no fractional part. Python integers have **unlimited precision** — they grow as large as available memory allows, unlike most other languages which have fixed-size integers (e.g., 32-bit or 64-bit).

```python
x = 42
big = 10 ** 100   # a googol — no overflow in Python
negative = -7
```

Integer literals can be written in different bases:
- Decimal: `255`
- Binary: `0b11111111`
- Octal: `0o377`
- Hexadecimal: `0xFF`

### `float` — Floating-Point Number

Floats represent real numbers using **IEEE 754 double-precision** format (64-bit). This means they have approximately 15–17 significant decimal digits, and they cannot represent every decimal fraction exactly.

```python
pi = 3.14159
tiny = 1.5e-10    # scientific notation: 1.5 × 10⁻¹⁰
large = 2.5e6     # 2,500,000.0
```

**Critical pitfall:** `0.1 + 0.2` does not equal `0.3` exactly in floating-point arithmetic. Always compare floats with a tolerance: `abs(a - b) < 1e-9`, or use the `math.isclose()` function.

### `str` — String

Strings are **immutable** sequences of Unicode characters. They can be defined with single quotes, double quotes, or triple quotes (for multi-line strings).

```python
name = 'Alice'
greeting = "Hello, World!"
long_text = """This spans
multiple lines."""
raw = r"C:\Users\name"   # raw string — backslashes not treated as escapes
```

### `bool` — Boolean

Booleans represent truth values. There are exactly two: `True` and `False`. In Python, `bool` is a subclass of `int`, so `True == 1` and `False == 0` — this occasionally causes surprising behaviour.

```python
flag = True
print(True + True)   # 2 (bool is a subclass of int)
print(True * 5)      # 5
```

**Truthiness:** Every Python object has a boolean value. The following evaluate to `False`:
- `0`, `0.0`, `0j` (numeric zeros)
- `""`, `[]`, `()`, `{}`, `set()` (empty collections)
- `None`
- Any object whose `__bool__` returns `False`

Everything else is truthy.

### `None` — The Absence of a Value

`None` is a singleton representing "no value" or "missing". It is the only instance of `NoneType`. Functions that do not explicitly `return` anything return `None`.

```python
result = None
print(type(result))   # <class 'NoneType'>
```

Always compare with `None` using `is` / `is not`, never `==`:
```python
if result is None:    # correct
if result == None:    # works but not idiomatic
```

---

## 2. Type Casting

**Explicit casting** uses constructor functions to convert between types:

| Conversion | Function | Notes |
|------------|----------|-------|
| Any → int | `int(x)` | Truncates floats; raises `ValueError` for non-numeric strings |
| Any → float | `float(x)` | Accepts `"3.14"` but not `"3,14"` |
| Any → str | `str(x)` | Works on any object |
| Any → bool | `bool(x)` | Returns `False` for falsy values, `True` otherwise |

**Implicit (automatic) casting** happens when Python silently converts types:
- `int + float` → `float` (Python widens to the more precise type)
- `bool` in arithmetic is treated as `0` or `1`

Python does **not** implicitly convert strings to numbers or vice versa — this raises `TypeError`.

---

## 3. Variable Scope

**Scope** determines in which parts of a program a variable name is visible. Python uses the **LEGB rule** for name lookup:

| Letter | Scope | Description |
|--------|-------|-------------|
| **L** | Local | Inside the current function |
| **E** | Enclosing | Inside any enclosing function (for nested functions) |
| **G** | Global | At the top level of the module |
| **B** | Built-in | Python's built-in namespace (`len`, `print`, etc.) |

Python searches L → E → G → B and uses the first match found.

### Local Scope

Variables created inside a function exist only for the duration of that function call:

```python
def greet():
    message = "Hello"   # local variable
    print(message)

greet()
# print(message)  # NameError — message doesn't exist outside
```

### Global Scope

Variables created at the module level are global. A function can **read** a global variable without any declaration. To **modify** a global variable from inside a function, you must declare it with `global`:

```python
count = 0

def increment():
    global count    # without this, count += 1 would raise UnboundLocalError
    count += 1
```

### Nonlocal Scope

For nested functions, `nonlocal` allows the inner function to modify a variable in the enclosing (but not global) scope:

```python
def outer():
    value = 10
    def inner():
        nonlocal value
        value += 5
    inner()
    print(value)  # 15
```

---

## 4. Mutability vs Immutability

| Immutable types | Mutable types |
|----------------|--------------|
| `int`, `float`, `bool`, `str`, `tuple`, `frozenset` | `list`, `dict`, `set` |

**Immutable:** Once created, the object's value cannot change. Assigning a new value to a variable just makes the name point to a different object.

**Mutable:** The object's contents can change in-place. Multiple variables can point to the same object, so modifying it through one name affects all others.

```python
a = [1, 2, 3]
b = a           # b and a point to the SAME list
b.append(4)
print(a)        # [1, 2, 3, 4] — a is affected too!
```

---

## 5. Memory References and `id()`

Every Python object has a unique identity, retrievable with `id()`. For small integers (typically -5 to 256) and short strings, Python **caches** (interns) objects, so `is` comparisons may return `True` unexpectedly. Never use `is` to compare values — use `==` for value equality.

---

## 6. Common Pitfalls

**Pitfall 1:** Comparing `None` with `==` instead of `is`
`if x == None:` works but `if x is None:` is the correct idiom.

**Pitfall 2:** Float precision errors in equality checks
`0.1 + 0.2 == 0.3` is `False`. Use `math.isclose()`.

**Pitfall 3:** Assuming `int()` rounds — it truncates toward zero
`int(3.9)` is `3`, not `4`. Use `round()` for rounding.

**Pitfall 4:** Modifying a global without `global` declaration
This raises `UnboundLocalError` at the point of the augmented assignment.

**Pitfall 5:** Sharing mutable default arguments
`def append_to(item, lst=[]):` — the list `lst` persists across calls. Use `None` as default and create inside the function.

---

## 7. Key Vocabulary

| Term | Definition |
|------|-----------|
| **Type** | Classification of a value that determines what operations are valid |
| **Casting** | Converting a value from one type to another |
| **Truthiness** | Whether a value evaluates to True or False in a boolean context |
| **Scope** | The region of code where a name is visible |
| **LEGB rule** | The order Python searches scopes: Local, Enclosing, Global, Built-in |
| **Mutability** | Whether an object's value can change after creation |
| **Identity** | A unique ID for each object in memory (`id()`) |
| **Interning** | Python's optimization of reusing cached small integers and strings |
