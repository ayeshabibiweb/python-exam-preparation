# Key Points — Topic 03: Operators and Expressions

Quick-reference cheat sheet. Review this before your exam.

---

## Arithmetic Operators

| Op | Name | Example | Result | Note |
|----|------|---------|--------|------|
| `+` | Add | `3 + 2` | `5` | |
| `-` | Subtract | `3 - 2` | `1` | |
| `*` | Multiply | `3 * 4` | `12` | |
| `/` | True divide | `7 / 2` | `3.5` | **always float** |
| `//` | Floor divide | `7 // 2` | `3` | rounds toward -∞ |
| `%` | Modulo | `7 % 3` | `1` | sign follows divisor |
| `**` | Power | `2 ** 8` | `256` | right-associative |

---

## Dangerous Arithmetic Gotchas

```python
-2 ** 2       # -4  (unary - applied AFTER **)
(-2) ** 2     # 4   (use parens!)

-7 // 2       # -4  (floor toward -infinity, not -3)
-7 % 2        # 1   (sign of result follows the divisor 2)

7 / 2         # 3.5 (always float — even 4/2 gives 2.0)
7 // 2        # 3   (integer result)

2 ** 3 ** 2   # 512 = 2**(3**2), right-to-left associativity
```

---

## Comparison Operators

```python
==  !=  <  >  <=  >=
```

**Chaining** (Python only):
```python
0 < x < 10        # equivalent to: 0 < x and x < 10
1 <= y <= 100     # valid, readable
```

---

## Logical Operators

| Op | Truth table | Short-circuits | Returns |
|----|------------|----------------|---------|
| `and` | True iff both true | on first `False` | **first falsy** or last value |
| `or` | True if any true | on first `True` | **first truthy** or last value |
| `not` | Negates bool | N/A | `True` or `False` |

```python
"" or "default"      # "default"  — common default-value pattern
0 or 42              # 42
None and "value"     # None
42 and "yes"         # "yes"
```

---

## Bitwise Operators

| Op | Name | Example | Binary |
|----|------|---------|--------|
| `&` | AND | `12 & 10 = 8` | `1100 & 1010 = 1000` |
| `\|` | OR | `12 \| 10 = 14` | `1100 \| 1010 = 1110` |
| `^` | XOR | `12 ^ 10 = 6` | `1100 ^ 1010 = 0110` |
| `~` | NOT | `~5 = -6` | -(n+1) |
| `<<` | Left shift | `3 << 2 = 12` | multiply by 2ⁿ |
| `>>` | Right shift | `12 >> 2 = 3` | floor-divide by 2ⁿ |

**Common patterns:**
```python
n & 1 == 0       # even check
n & (1 << k)     # check bit k
n | (1 << k)     # set bit k
n & ~(1 << k)    # clear bit k
n ^ (1 << k)     # toggle bit k
```

---

## Membership and Identity

```python
x in collection         # True if x is a member
x not in collection     # True if x is not a member

x is None               # identity check (same object)
x is not None           # preferred None check
```

---

## Augmented Assignment

```python
x += n    x -= n    x *= n    x /= n
x //= n   x %= n    x **= n
x &= n    x |= n    x ^= n    x <<= n    x >>= n
```

**List note:** `lst += [x]` is in-place (modifies `lst`); `lst = lst + [x]` creates a new list.

---

## Operator Precedence Table (High → Low)

```
()               ← parentheses
**               ← exponent (RIGHT-associative)
+x  -x  ~x      ← unary
*  /  //  %      ← multiplicative
+  -             ← additive
<<  >>           ← bit shifts
&                ← bitwise AND
^                ← bitwise XOR
|                ← bitwise OR
==  !=  <  >  <=  >=  is  is not  in  not in  ← comparisons
not              ← logical NOT
and              ← logical AND
or               ← logical OR (LOWEST)
```

**When in doubt, add parentheses!**

---

## Common Mistakes

```python
# 1. Division always returns float
10 / 5          # 2.0, not 2

# 2. ** precedence vs unary minus
-2 ** 2         # -4, not 4 → write (-2) ** 2

# 3. and/or return operands, not bool
x = 0 or []     # x is [], not False

# 4. Chaining comparisons — be careful with mixed operators
1 < 5 > 3       # True (1<5 AND 5>3) — valid but potentially confusing

# 5. Short-circuit skips function calls
False and some_function()   # some_function() NEVER called
```

---

## Tips

- `bool(expr)` converts any expression to a definitive `True`/`False`
- Use `math.isclose(a, b)` instead of `a == b` for floats
- The modulo operator is great for: wrapping indices (`i % len(lst)`), checking divisibility (`n % k == 0`), cycling through values
- Prefer `x is None` over `x == None` — it's faster and idiomatic
- Add parentheses liberally in complex expressions — readability matters more than brevity
