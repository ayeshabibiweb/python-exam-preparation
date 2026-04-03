# Topic 04 — Control Structures

## Overview

Control structures determine the order in which statements execute. Without them, Python would run every line exactly once, top to bottom. With them, you can make decisions (`if`/`elif`/`else`), repeat actions (`for`, `while`), and manage iteration flow (`break`, `continue`, `pass`). Mastery of control structures is the foundation of algorithm design.

---

## 1. The `if` / `elif` / `else` Statement

The `if` statement conditionally executes a block based on a boolean expression:

```python
if condition:
    # executes if condition is truthy
elif another_condition:
    # executes if the elif condition is truthy (and the if was False)
else:
    # executes if none of the above conditions were True
```

Key rules:
- `elif` and `else` are optional. You can have any number of `elif` clauses.
- Python evaluates conditions **top to bottom** and executes the **first** matching block only.
- Once a branch executes, all remaining `elif`/`else` branches are skipped.
- The condition can be any expression — Python evaluates its truthiness.

---

## 2. Ternary (Conditional) Expression

Python's one-line conditional expression evaluates to one of two values:

```python
value = expression_if_true if condition else expression_if_false
```

Example:
```python
label = "even" if n % 2 == 0 else "odd"
```

Use sparingly — nested ternary expressions become hard to read. Stick to simple cases.

---

## 3. `for` Loops

`for` iterates over any **iterable** (list, string, range, tuple, dict, file, etc.):

```python
for variable in iterable:
    # body — variable takes each value in turn
```

The loop variable takes each item from the iterable one at a time. After the last item, execution continues after the loop body.

### `range()`

`range(stop)`, `range(start, stop)`, `range(start, stop, step)` generate sequences of integers:

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 8)       # 2, 3, 4, 5, 6, 7
range(0, 10, 2)   # 0, 2, 4, 6, 8
range(10, 0, -1)  # 10, 9, 8, ... 1  (countdown)
```

`range()` is lazy — it does not create a list in memory, making it efficient for large sequences.

### `enumerate()`

When you need both the index and the value, use `enumerate()`:

```python
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)
```

---

## 4. `while` Loops

`while` repeats as long as its condition is truthy:

```python
while condition:
    # body
```

**Infinite loops:** If the condition never becomes `False`, the loop runs forever. Always ensure the loop has a termination path (a variable that changes, or a `break`).

Common patterns:
- **Counter-controlled:** `while count < limit: count += 1`
- **Sentinel-controlled:** `while user_input != "quit":`
- **Event-controlled:** `while not found:`

---

## 5. `break`, `continue`, and `pass`

### `break`

Immediately exits the **innermost** enclosing loop. Execution continues with the next statement after the loop.

```python
for n in range(100):
    if n == 5:
        break       # stops the loop when n reaches 5
```

### `continue`

Skips the **rest of the current iteration** and jumps back to the loop condition check (for `while`) or the next item (for `for`).

```python
for n in range(10):
    if n % 2 == 0:
        continue    # skip even numbers
    print(n)        # prints 1, 3, 5, 7, 9
```

### `pass`

Does nothing — a syntactic placeholder for an empty block. Required when a block is syntactically needed but you have nothing to put in it yet.

```python
if some_condition:
    pass    # TODO: implement this branch
```

---

## 6. The Loop `else` Clause

Python's `for` and `while` loops can have an `else` clause. The `else` block executes **when the loop completes normally** (i.e., it was *not* terminated by `break`):

```python
for item in collection:
    if condition(item):
        break
else:
    # runs only if no break occurred — item was not found
    print("Not found")
```

This is particularly useful for search patterns — the `else` fires if the target was not found.

---

## 7. Nested Loops

Loops can be nested inside other loops. The inner loop completes all its iterations for each single iteration of the outer loop:

```python
for i in range(3):      # outer: 3 iterations
    for j in range(3):  # inner: 3 iterations per outer iteration = 9 total
        print(i, j)
```

**`break` in nested loops only exits the innermost loop.** To break out of multiple levels, use a flag variable or refactor into a function and use `return`.

---

## 8. The `match` Statement (Python 3.10+)

Python 3.10 introduced structural pattern matching as an alternative to chains of `if`/`elif`:

```python
match command:
    case "quit":
        quit()
    case "help":
        show_help()
    case str(msg) if msg.startswith("say "):
        print(msg[4:])
    case _:
        print(f"Unknown command: {command}")
```

`match` supports matching on values, types, sequences, mappings, and complex patterns with guards (`if`). The `_` case is the wildcard (catch-all).

---

## 9. Common Patterns and Anti-Patterns

### Pattern: Counting Items That Meet a Condition

```python
count = sum(1 for x in data if condition(x))
```

### Pattern: Finding the First Match

```python
result = next((x for x in data if condition(x)), None)
```

### Anti-Pattern: Modifying a List While Iterating Over It

```python
# WRONG — skips elements
for item in my_list:
    if condition(item):
        my_list.remove(item)   # changes the list mid-iteration!

# CORRECT — iterate over a copy, or use list comprehension
my_list = [x for x in my_list if not condition(x)]
```

### Anti-Pattern: Using `range(len(lst))` When You Need Values

```python
# CLUNKY
for i in range(len(items)):
    print(items[i])

# PYTHONIC
for item in items:
    print(item)

# When you need index AND value
for i, item in enumerate(items):
    print(i, item)
```

---

## 10. Key Vocabulary

| Term | Definition |
|------|-----------|
| **Conditional** | A statement that chooses between execution paths |
| **Branch** | One of the paths in a conditional statement |
| **Iteration** | Repeating a block of code |
| **Iterable** | Any object that can produce values one at a time |
| **Iterator** | An object that remembers its position in a sequence |
| **Sentinel value** | A special value used to signal a condition (e.g., end of input) |
| **Loop else** | `else` on a loop: executes if loop was not broken |
| **Ternary expression** | Single-line `value_if_true if cond else value_if_false` |
| **Pattern matching** | Structural `match`/`case` (Python 3.10+) |
| **Guard** | A condition in a `match` case: `case x if x > 0:` |
