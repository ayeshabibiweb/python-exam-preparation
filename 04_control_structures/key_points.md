# Key Points — Topic 04: Control Structures

Quick-reference cheat sheet. Review this before your exam.

---

## if / elif / else

```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

- Conditions evaluated **top to bottom**; only the **first** truthy block runs
- `elif` and `else` are optional
- No `switch` in Python < 3.10 — use `if`/`elif` chain or a dict of callables

---

## Ternary Expression

```python
value = x if condition else y

# Example
label = "even" if n % 2 == 0 else "odd"
```

Do not nest ternaries more than one level — use `if`/`elif` instead.

---

## for Loop

```python
for item in iterable:
    ...
```

### range() patterns

```python
range(n)              # 0, 1, …, n-1
range(a, b)           # a, a+1, …, b-1
range(a, b, step)     # a, a+step, … (up to but not including b)
range(10, 0, -1)      # 10, 9, …, 1  (countdown)
```

### Useful loop helpers

```python
for i, v in enumerate(lst):          # index + value
for i, v in enumerate(lst, start=1): # index starts at 1
for a, b in zip(lst1, lst2):         # pair up two iterables
for v in reversed(lst):              # iterate backwards
for v in sorted(lst):                # iterate in sorted order
```

---

## while Loop

```python
while condition:
    ...
```

| Pattern | Template |
|---------|----------|
| Counter | `i = 0; while i < n: i += 1` |
| Sentinel | `while val != STOP:` |
| Infinite + break | `while True: if cond: break` |

---

## break, continue, pass

| Keyword | Effect | Scope |
|---------|--------|-------|
| `break` | Exit the loop immediately | Innermost loop only |
| `continue` | Skip rest of current iteration | Innermost loop only |
| `pass` | Do nothing (placeholder) | Any empty block |

```python
# break example — stop at first negative
for x in data:
    if x < 0:
        break
    process(x)

# continue example — skip even numbers
for n in range(10):
    if n % 2 == 0:
        continue
    print(n)          # 1 3 5 7 9
```

---

## Loop else Clause

```python
for item in collection:
    if found(item):
        break
else:
    # Runs ONLY if loop completed without break
    print("Not found")
```

```python
while condition:
    if done():
        break
else:
    # Runs ONLY if condition became False (no break)
    print("Exhausted")
```

---

## Nested Loops

```python
for i in range(rows):
    for j in range(cols):
        ...
```

- `break`/`continue` affect only the **innermost** enclosing loop
- To break multiple levels: use a flag variable or `return` from a function

---

## match Statement (Python 3.10+)

```python
match value:
    case 1:
        ...
    case 2 | 3:        # multiple patterns with |
        ...
    case str(s):       # capture into variable s
        ...
    case int(n) if n > 0:   # guard condition
        ...
    case _:            # wildcard — matches everything
        ...
```

---

## Common Patterns

```python
# Count items meeting a condition
count = sum(1 for x in data if predicate(x))

# Find first match (or None)
result = next((x for x in data if predicate(x)), None)

# Remove items while iterating (SAFE way)
data = [x for x in data if not predicate(x)]

# Flatten a 2D list
flat = [item for row in matrix for item in row]
```

---

## Common Mistakes

```python
# 1. Putting the wrong condition first in FizzBuzz
if n % 3 == 0:         # prints "Fizz" for n=15 instead of "FizzBuzz"
...
# FIX: check n % 15 == 0 (or n % 3 == 0 and n % 5 == 0) FIRST

# 2. off-by-one with range
range(1, n)    # 1 … n-1  (n is excluded)
range(1, n+1)  # 1 … n    (inclusive)

# 3. Mutating a list inside the loop you're iterating over
for item in lst:
    if bad(item):
        lst.remove(item)   # BUG — skips elements
# FIX: lst = [x for x in lst if not bad(x)]

# 4. Forgetting that break exits only the INNER loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break    # breaks inner loop only; outer keeps going

# 5. Infinite while loop
while n > 0:
    print(n)         # forgot n -= 1 → runs forever
```

---

## Tips

- `for` is preferred over `while` whenever you know the number of iterations
- Use `enumerate()` instead of `range(len(lst))`
- The loop `else` clause is underused but very elegant for "search and not found" logic
- Use `any()` / `all()` with generator expressions instead of explicit loops where possible:
  ```python
  any(x > 0 for x in data)   # True if at least one positive
  all(x > 0 for x in data)   # True if all positive
  ```
