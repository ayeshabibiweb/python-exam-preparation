# Topic 03 — Operators and Expressions

## Overview

Operators are the symbols and keywords Python uses to perform computations and comparisons. An **expression** is any combination of values, variables, and operators that Python can evaluate to produce a result. Understanding how operators work — and especially the order in which they are evaluated — is critical for predicting program behaviour and avoiding subtle bugs.

---

## 1. Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | True division | `7 / 2` | `3.5` (always float) |
| `//` | Floor division | `7 // 2` | `3` (integer, rounds toward -∞) |
| `%` | Modulo (remainder) | `7 % 2` | `1` |
| `**` | Exponentiation | `2 ** 8` | `256` |

**Key distinctions:**
- `/` always produces a `float`, even with two integers: `4 / 2` → `2.0`
- `//` rounds *toward negative infinity*: `-7 // 2` → `-4` (not `-3`)
- `%` follows the sign of the **divisor**: `-7 % 3` → `2`
- `**` has higher precedence than unary `-`: `-2 ** 2` → `-4` (not `4`)

---

## 2. Comparison Operators

Comparison operators return a `bool` (`True` or `False`):

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `5 == 5` → `True` |
| `!=` | Not equal to | `5 != 3` → `True` |
| `<` | Less than | `3 < 5` → `True` |
| `>` | Greater than | `5 > 3` → `True` |
| `<=` | Less than or equal | `5 <= 5` → `True` |
| `>=` | Greater than or equal | `6 >= 5` → `True` |

Python supports **chained comparisons**: `0 < x < 10` is valid and equivalent to `0 < x and x < 10`. This is more readable and evaluated correctly — never write `0 < x and x < 10` when you can chain.

---

## 3. Logical Operators

| Operator | Meaning | Short-circuits? |
|----------|---------|-----------------|
| `and` | True if both operands are true | Yes — returns first falsy value |
| `or` | True if at least one operand is true | Yes — returns first truthy value |
| `not` | Negates the boolean value | N/A |

### Short-Circuit Evaluation

Python stops evaluating as soon as the result is determined:
- `False and expensive_func()` — `expensive_func()` is **never called**
- `True or expensive_func()` — `expensive_func()` is **never called**

Importantly, `and` and `or` do not necessarily return `True`/`False` — they return one of their **operands**:

```python
"" or "default"     # "default" (first truthy value)
"hello" or "other"  # "hello"   (first truthy value)
None and 5          # None      (first falsy value)
10 and 20           # 20        (both truthy — returns last value)
```

This behaviour is commonly used for default values: `name = user_input or "Anonymous"`.

---

## 4. Bitwise Operators

Bitwise operators work on the binary representations of integers:

| Operator | Name | Example (decimal) | Binary |
|----------|------|-----------|--------|
| `&` | AND | `12 & 10` → `8` | `1100 & 1010 = 1000` |
| `\|` | OR | `12 \| 10` → `14` | `1100 \| 1010 = 1110` |
| `^` | XOR | `12 ^ 10` → `6` | `1100 ^ 1010 = 0110` |
| `~` | NOT (complement) | `~5` → `-6` | inverts all bits |
| `<<` | Left shift | `3 << 2` → `12` | `011 → 1100` |
| `>>` | Right shift | `12 >> 2` → `3` | `1100 → 0011` |

`~n` is always equal to `-(n + 1)` due to two's complement representation.

Left shift by `n` is equivalent to multiplying by `2^n`. Right shift by `n` is equivalent to floor-dividing by `2^n`.

---

## 5. Membership Operators

| Operator | Meaning | Works With |
|----------|---------|-----------|
| `in` | True if value is in the sequence | str, list, tuple, set, dict (keys) |
| `not in` | True if value is not in the sequence | same |

```python
"a" in "apple"          # True
3 in [1, 2, 3, 4]       # True
"key" in {"key": 1}     # True (checks dict keys)
10 not in range(5)      # True
```

---

## 6. Identity Operators

| Operator | Meaning |
|----------|---------|
| `is` | True if both names refer to the *same object* in memory |
| `is not` | True if both names refer to *different objects* |

Use `is`/`is not` **only** for `None` checks and object identity. Never for value comparison (see Small Integer Interning in Topic 02).

---

## 7. Augmented Assignment Operators

Augmented assignment combines an arithmetic operation with assignment:

```python
x += 5    # x = x + 5
x -= 3    # x = x - 3
x *= 2    # x = x * 2
x /= 4    # x = x / 4  (result is always float)
x //= 3   # x = x // 3
x %= 7    # x = x % 7
x **= 2   # x = x ** 2
x &= 0xFF # x = x & 0xFF
x |= 1    # x = x | 1
x ^= mask # x = x ^ mask
x <<= 1   # x = x << 1
x >>= 1   # x = x >> 1
```

**For mutable objects**, `+=` calls `__iadd__` (in-place add) rather than creating a new object — this is why `list1 += list2` modifies `list1` in place, while `list1 = list1 + list2` creates a new list.

---

## 8. Operator Precedence (High to Low)

| Priority | Operators | Notes |
|----------|-----------|-------|
| 1 (highest) | `()` | Parentheses override everything |
| 2 | `**` | Right-associative: `2**3**2` = `2**9` = 512 |
| 3 | `+x`, `-x`, `~x` | Unary operators |
| 4 | `*`, `/`, `//`, `%` | Multiplicative |
| 5 | `+`, `-` | Additive |
| 6 | `<<`, `>>` | Bit shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in` | Comparisons |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 (lowest) | `or` | Logical OR |

**Mnemonic:** PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction) covers the arithmetic portion. After that come bit operations, then comparisons, then logical operators.

---

## 9. Common Mistakes

**Mistake 1:** Confusing `/` with `//`
`5 / 2` → `2.5` (float); `5 // 2` → `2` (int). Use `//` when you need integer division.

**Mistake 2:** Assuming `-2 ** 2` is `4`
Python evaluates this as `-(2 ** 2)` = `-4`. Write `(-2) ** 2` for `4`.

**Mistake 3:** Using `==` to check for `None`
Always use `is None` / `is not None`.

**Mistake 4:** Trusting `and`/`or` to always return a bool
They return operands: `0 or []` returns `[]`, not `False`.

**Mistake 5:** Not accounting for floor division with negatives
`-7 // 2` → `-4` (rounds toward -∞), not `-3`.

---

## 10. Key Vocabulary

| Term | Definition |
|------|-----------|
| **Operator** | Symbol or keyword that performs an operation |
| **Operand** | Value the operator acts upon |
| **Expression** | Code that evaluates to a value |
| **Precedence** | The order in which operators are evaluated |
| **Associativity** | Left-to-right (most) or right-to-left (`**`, unary) |
| **Short-circuit** | Skipping evaluation when result is already determined |
| **Floor division** | Division that rounds toward negative infinity |
| **Modulo** | Remainder after division |
| **Bitwise** | Operating on individual bits of an integer |
