# Python Exam Preparation Materials

A comprehensive study resource for intermediate university students preparing for Python programming exams. This repository provides structured notes, runnable code examples, practice problems, and quick-reference cheat sheets across 16 core Python topics.

---

## Features

- **Structured Notes** — 800–1200 word topic notes covering concepts, common mistakes, and vocabulary
- **Runnable Examples** — 8–10 commented, self-contained Python 3.8+ examples per topic
- **Practice Problems** — Problems with full solutions embedded as comments
- **Key Points / Cheat Sheets** — Scannable quick-reference files for exam review
- **Study Guide** — Recommended 4-week plan with learning strategies
- **16 Core Topics** — From fundamentals through advanced concurrency and best practices

---

## Directory Structure

```
python-exam-preparation/
│
├── README.md                        ← This file
├── STUDY_GUIDE.md                   ← 4-week study plan and strategies
├── .gitignore
│
├── 01_programming_fundamentals/
│   ├── notes.md                     ← Syntax, variables, execution model
│   ├── examples.py                  ← 10 runnable examples
│   ├── practice.py                  ← Practice problems with solutions
│   └── key_points.md                ← Cheat sheet
│
├── 02_data_types_variables/
│   ├── notes.md                     ← int, float, str, bool, None, scope
│   ├── examples.py
│   ├── practice.py
│   └── key_points.md
│
├── 03_operators_expressions/
│   ├── notes.md                     ← All operator types, precedence
│   ├── examples.py
│   ├── practice.py
│   └── key_points.md
│
├── 04_control_structures/
│   ├── notes.md                     ← if/elif/else, loops, break/continue
│   ├── examples.py
│   ├── practice.py
│   └── key_points.md
│
├── 05_functions/                    ← (coming soon)
├── 06_strings/                      ← (coming soon)
├── 07_lists_tuples/                 ← (coming soon)
├── 08_dictionaries_sets/            ← (coming soon)
├── 09_oop_basics/                   ← (coming soon)
├── 10_oop_advanced/                 ← (coming soon)
├── 11_memory_management/            ← (coming soon)
├── 12_exceptions/                   ← (coming soon)
├── 13_modules_packages/             ← (coming soon)
├── 14_file_io/                      ← (coming soon)
├── 15_concurrency/                  ← (coming soon)
├── 16_best_practices/               ← (coming soon)
│
├── practice_problems/               ← Cross-topic exercises (coming soon)
├── sample_exams/                    ← Mock exams (coming soon)
└── cheat_sheets/                    ← Condensed topic summaries (coming soon)
```

---

## How to Use These Materials

### Prerequisites

- Python 3.8 or higher installed (`python --version`)
- A text editor or IDE (VS Code, PyCharm, or any editor)
- Basic familiarity with running Python scripts from the terminal

### Running the Examples

Each `examples.py` and `practice.py` file is self-contained and runnable:

```bash
# Run a topic's examples
python 01_programming_fundamentals/examples.py

# Run practice problems
python 01_programming_fundamentals/practice.py
```

### Suggested Workflow Per Topic

1. **Read `notes.md`** — Build your conceptual understanding first
2. **Study `examples.py`** — Read through the code and predict outputs before running
3. **Run `examples.py`** — Verify your predictions, experiment by modifying values
4. **Attempt `practice.py`** — Cover the solutions and write your own code first
5. **Uncover solutions** — Compare your approach, note differences
6. **Review `key_points.md`** — Reinforce key facts for exam memory

---

## Study Recommendations

### Active Learning Over Passive Reading

Do not simply read the notes and move on. Type out the examples manually — muscle memory reinforces syntax. Modify examples to test your understanding ("what happens if I change this value?").

### Use the Practice Problems Seriously

Before looking at any solution, spend at least 10–15 minutes attempting each problem yourself. Struggling before seeing the answer dramatically improves retention.

### Follow the 4-Week Plan

The `STUDY_GUIDE.md` provides a structured plan that builds knowledge progressively. Topics 01–04 form the foundation — skipping them creates gaps that compound in later topics.

### Exam-Day Tips

- Review all `key_points.md` files the night before
- Practice writing code by hand (many exams are written, not typed)
- Know the most common built-in functions by heart
- Understand error messages — they guide debugging under pressure

---

## Topic Overview

| # | Topic | Key Concepts |
|---|-------|-------------|
| 01 | Programming Fundamentals | Syntax, variables, execution model, I/O |
| 02 | Data Types & Variables | int, float, str, bool, None, scope, mutability |
| 03 | Operators & Expressions | Arithmetic, comparison, logical, bitwise, precedence |
| 04 | Control Structures | if/elif/else, for/while loops, break/continue |
| 05 | Functions | def, parameters, return, scope, lambdas |
| 06 | Strings | Slicing, methods, formatting, encoding |
| 07 | Lists & Tuples | Indexing, slicing, methods, comprehensions |
| 08 | Dictionaries & Sets | Key-value pairs, set operations, comprehensions |
| 09 | OOP Basics | Classes, objects, __init__, methods, attributes |
| 10 | OOP Advanced | Inheritance, polymorphism, dunder methods |
| 11 | Memory Management | References, garbage collection, id(), copying |
| 12 | Exceptions | try/except/finally, custom exceptions, raising |
| 13 | Modules & Packages | import, __name__, pip, virtual environments |
| 14 | File I/O | open(), read/write, context managers, pathlib |
| 15 | Concurrency | Threading, multiprocessing, asyncio basics |
| 16 | Best Practices | PEP 8, testing, documentation, code review |

---

## Contributing

Found a bug or want to add content? Open an issue or pull request. All examples must be Python 3.8+ compatible and include comments explaining the key concept demonstrated.

---

*Python 3.8+ | University Exam Preparation | Intermediate Level*