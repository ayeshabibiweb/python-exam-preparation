# Study Guide — Python Exam Preparation

A structured 4-week plan and learning strategies for intermediate university students. Each week builds directly on the last — resist the temptation to skip ahead.

---

## 4-Week Study Plan

### Week 1 — Foundations (Topics 01–04)

**Goal:** Develop rock-solid fundamentals. Every advanced Python concept rests on these four topics.

| Day | Task |
|-----|------|
| Mon | Topic 01 notes.md → examples.py (read, predict, run) |
| Tue | Topic 01 practice.py (attempt before looking) → key_points.md |
| Wed | Topic 02 notes.md → examples.py |
| Thu | Topic 02 practice.py → key_points.md |
| Fri | Topic 03 notes.md → examples.py → practice.py |
| Sat | Topic 04 notes.md → examples.py → practice.py |
| Sun | Review all four key_points.md files; write 5 code snippets from memory |

**Week 1 Checkpoints:**
- [ ] Can explain Python's execution model (source → bytecode → interpreter)
- [ ] Know all basic data types and how to cast between them
- [ ] Can evaluate any operator expression including precedence
- [ ] Can write FizzBuzz and nested loop patterns without reference

---

### Week 2 — Core Programming (Topics 05–08)

**Goal:** Master the building blocks used in virtually every Python program.

| Day | Task |
|-----|------|
| Mon | Topic 05: Functions — def, parameters, return values, default args |
| Tue | Topic 05: *args/**kwargs, lambda, scope (LEGB rule) |
| Wed | Topic 06: Strings — slicing, methods, f-strings, encoding |
| Thu | Topic 07: Lists & Tuples — indexing, slicing, list comprehensions |
| Fri | Topic 08: Dictionaries & Sets — CRUD operations, comprehensions |
| Sat | Cross-topic exercises combining functions + data structures |
| Sun | Review all key_points.md; write solutions to 3 practice problems from memory |

**Week 2 Checkpoints:**
- [ ] Can write functions with default parameters and *args/**kwargs
- [ ] Can slice any string or list given start/stop/step
- [ ] Can build a dict/list comprehension for a given problem
- [ ] Understands the difference between mutable and immutable arguments

---

### Week 3 — OOP, Memory, Exceptions, Modules (Topics 09–12)

**Goal:** Write and reason about object-oriented programs; handle errors robustly.

| Day | Task |
|-----|------|
| Mon | Topic 09: Classes, __init__, instance vs. class attributes |
| Tue | Topic 10: Inheritance, super(), polymorphism, dunder methods |
| Wed | Topic 11: Memory model — references, id(), shallow vs. deep copy, GC |
| Thu | Topic 12: Exceptions — try/except/else/finally, custom exceptions |
| Fri | OOP mini-project: design and implement a small class hierarchy |
| Sat | Exception-safety: refactor week 2 code to handle all edge cases |
| Sun | Review key_points.md for topics 09–12; flashcard drill |

**Week 3 Checkpoints:**
- [ ] Can implement a class with inheritance and overridden methods
- [ ] Understands the difference between shallow and deep copy
- [ ] Can write a try/except/finally block that catches specific exceptions
- [ ] Knows when to use `raise` vs. `raise ... from ...`

---

### Week 4 — Advanced Topics (Topics 13–16)

**Goal:** Round out your knowledge with practical and advanced Python.

| Day | Task |
|-----|------|
| Mon | Topic 13: Modules/packages — import system, __name__, virtual envs |
| Tue | Topic 14: File I/O — open(), modes, context managers, pathlib |
| Wed | Topic 15: Concurrency — threading vs. multiprocessing, asyncio basics |
| Thu | Topic 16: Best practices — PEP 8, type hints, testing with unittest |
| Fri | Full mock exam (use sample_exams/ when available) |
| Sat | Review all weak areas identified during mock exam |
| Sun | Final review: all key_points.md + cheat_sheets/ |

**Week 4 Checkpoints:**
- [ ] Can import from a custom module and explain __name__ == "__main__"
- [ ] Can read/write files safely using context managers
- [ ] Understands the GIL and when to choose threading vs. multiprocessing
- [ ] Code follows PEP 8 and includes type hints

---

## Learning Strategies

### 1. Active Recall (Most Effective)

Close the notes and try to write the concept or code from scratch. This feels harder than re-reading — that difficulty is the learning happening. Use after each study session:

- Cover `key_points.md` and recite each point aloud
- Open a blank file and implement a concept without reference
- Write pseudocode for a problem before writing Python

### 2. Spaced Repetition

Revisit material at increasing intervals: review after 1 day, then 3 days, then 1 week. Each `key_points.md` is designed for this — a 5-minute review before bed is enough to maintain retention.

### 3. The Predict-Run-Explain Loop

For every `examples.py` file:
1. **Predict** — Read each example and write down the expected output
2. **Run** — Execute the file and check your predictions
3. **Explain** — For any mismatch, explain in words why the actual output occurred

This technique catches misconceptions early and builds confidence.

### 4. Rubber Duck Debugging

Explain your code out loud to an imaginary listener (or a rubber duck). If you cannot explain a line, you do not fully understand it. This is especially useful for:
- Scope and variable resolution
- Object references and mutation
- Loop logic and termination conditions

### 5. Write Code by Hand

Many university exams require handwritten code. Practice writing Python on paper at least once per topic:
- No autocomplete forces you to recall exact syntax
- Exposes gaps in knowledge of standard library methods
- Improves exam performance under time pressure

---

## Time Management

### Daily Study Session (90 minutes recommended)
- **0–5 min:** Recall previous session (what did I cover? what was hard?)
- **5–45 min:** New material (notes.md + examples.py)
- **45–75 min:** Practice (practice.py — attempt before reading solutions)
- **75–90 min:** Review (key_points.md + notes on mistakes made)

### Before the Exam (Final 48 Hours)
- Do NOT start new topics in the last 48 hours
- Review `key_points.md` for all completed topics
- Re-do 2–3 practice problems from memory per topic
- Get 8 hours of sleep — sleep consolidates memory more than cramming

### During the Exam
- Read all questions before starting — allocate time proportionally
- Tackle questions you are confident about first to bank points
- For code-writing questions, write pseudocode before Python syntax
- Leave at least 10 minutes at the end to review for syntax errors

---

## Common Exam Topics by Frequency

### Very Frequently Tested
- List/dict/set comprehensions
- Function definitions with default and keyword arguments
- String formatting (f-strings)
- Exception handling (try/except/finally)
- Class definition with __init__ and at least one method

### Frequently Tested
- Scope (LEGB rule, global/nonlocal)
- Operator precedence and expression evaluation
- Loop patterns (while with break, for with enumerate)
- Type casting and implicit conversion pitfalls
- Shallow vs. deep copy

### Occasionally Tested
- Bitwise operators
- Generator expressions
- Decorators (basic)
- File I/O with context managers
- The `__name__ == "__main__"` pattern

---

## Recommended External Resources

- **Official Python Docs:** https://docs.python.org/3/ — authoritative reference
- **PEP 8 Style Guide:** https://peps.python.org/pep-0008/ — read once, follow always
- **Python Tutor (visualizer):** https://pythontutor.com — step through code visually
- **Real Python:** https://realpython.com — practical tutorials for every topic

---

*Consistent daily practice beats marathon cramming sessions every time.*
