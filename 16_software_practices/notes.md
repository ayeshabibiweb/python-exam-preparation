# Topic 16: Software Practices
# ==============================

## What This Topic Covers
Good software practices make code readable, maintainable, and collaborative.
This topic covers PEP 8 style, docstrings, type hints, Git basics, and design principles.

---

## 1. PEP 8 – Python Style Guide

PEP 8 is the official Python style guide. Following it makes code readable for every Python developer.

### Naming Conventions
| Category | Style | Example |
|----------|-------|---------|
| Variables & functions | `snake_case` | `total_price`, `get_user()` |
| Classes | `PascalCase` | `ShoppingCart`, `UserAccount` |
| Constants | `UPPER_CASE` | `MAX_SIZE`, `PI` |
| Private attributes | `_single_underscore` | `_cache`, `_validate()` |
| Name-mangled | `__double_underscore` | `__secret` |
| Modules/packages | `lowercase` | `utils`, `data_parser` |

### Indentation & Whitespace
- Use **4 spaces** per indentation level (never tabs).
- Maximum line length: **79 characters** (or 99 in many modern projects).
- Two blank lines between top-level definitions.
- One blank line between methods inside a class.
- Spaces around operators: `x = y + 1`, not `x=y+1`.
- No spaces inside brackets: `func(a, b)`, not `func( a, b )`.

### Imports
- One import per line.
- Order: standard library → third-party → local.
- Use absolute imports where possible.
```python
import os
import sys

import requests

from mypackage import utils
```

### Common PEP 8 Violations to Avoid
- Mixing tabs and spaces.
- Long lines without line continuation.
- Missing whitespace around operators.
- Wildcard imports (`from module import *`).
- Unused imports.
- Multiple statements on one line (`x = 1; y = 2`).

---

## 2. Docstrings (PEP 257)

Docstrings are string literals that document modules, classes, and functions.
They are accessible via `help()` and `.__doc__`.

### Google Style (Recommended)
```python
def calculate_discount(price: float, rate: float) -> float:
    """Calculate the discounted price.

    Args:
        price: Original price in dollars.
        rate: Discount rate between 0.0 and 1.0.

    Returns:
        The price after applying the discount.

    Raises:
        ValueError: If rate is not between 0 and 1.

    Example:
        >>> calculate_discount(100.0, 0.2)
        80.0
    """
    if not 0 <= rate <= 1:
        raise ValueError(f"rate must be 0–1, got {rate}")
    return price * (1 - rate)
```

### Class Docstring
```python
class Rectangle:
    """Represents a 2D rectangle.

    Attributes:
        width: Width in units.
        height: Height in units.
    """

    def __init__(self, width: float, height: float) -> None:
        """Initialise rectangle with given dimensions."""
        self.width = width
        self.height = height
```

---

## 3. Type Hints (PEP 484)

Type hints add static type information without changing runtime behaviour.
They improve IDE support, documentation, and catch bugs early with mypy.

### Basic Types
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def is_even(n: int) -> bool:
    return n % 2 == 0
```

### typing Module
```python
from typing import List, Dict, Tuple, Optional, Union, Any

def get_names() -> List[str]:
    return ["Alice", "Bob"]

def get_scores() -> Dict[str, int]:
    return {"Alice": 95}

def find_user(user_id: int) -> Optional[str]:
    # Returns a string or None
    ...

def process(data: Union[str, bytes]) -> str:
    ...
```

### Python 3.9+ Shorthand (no typing import needed)
```python
def get_names() -> list[str]: ...
def get_scores() -> dict[str, int]: ...
def coordinates() -> tuple[float, float]: ...
```

---

## 4. Git Basics

Git is the standard version control system for software development.

### Core Workflow
```bash
git init                        # initialise a repository
git clone <url>                 # copy a remote repository

git status                      # show changed files
git add file.py                 # stage a specific file
git add .                       # stage all changes

git commit -m "feat: add login" # save staged changes with a message
git push origin main            # upload commits to remote

git pull origin main            # fetch + merge remote changes
git fetch origin                # fetch without merging
```

### Branching
```bash
git branch feature/login        # create a branch
git checkout feature/login      # switch to it
git checkout -b feature/login   # create AND switch

git merge feature/login         # merge into current branch
git branch -d feature/login     # delete branch
```

### Useful Commands
```bash
git log --oneline -10           # last 10 commits
git diff                        # unstaged changes
git diff --staged               # staged changes
git stash                       # temporarily shelve changes
git stash pop                   # restore shelved changes
```

### Commit Message Best Practices
- Use the imperative mood: "Add feature", not "Added feature".
- Keep subject line ≤ 72 characters.
- Optionally add a body explaining *why*.

---

## 5. Design Principles

### DRY – Don't Repeat Yourself
Avoid duplicating logic. Extract repeated code into functions or classes.
```python
# BAD – repeated logic
tax_a = price_a * 0.08
tax_b = price_b * 0.08

# GOOD
TAX_RATE = 0.08
def calculate_tax(price):
    return price * TAX_RATE
```

### KISS – Keep It Simple, Stupid
Prefer simple, clear solutions over clever, complex ones.

### SOLID Principles (brief overview)
| Letter | Principle | Meaning |
|--------|-----------|---------|
| S | Single Responsibility | A class does one thing |
| O | Open/Closed | Open for extension, closed for modification |
| L | Liskov Substitution | Subclasses can replace parent classes |
| I | Interface Segregation | Small focused interfaces over large ones |
| D | Dependency Inversion | Depend on abstractions, not concretions |

---

## 6. Virtual Environments
```bash
python -m venv venv             # create virtual environment
source venv/bin/activate        # activate (Linux/macOS)
venv\Scripts\activate           # activate (Windows)

pip install requests            # install package into venv
pip freeze > requirements.txt   # save dependencies
pip install -r requirements.txt # restore dependencies
deactivate                      # exit virtual environment
```

---

## Common Mistakes
- Mixing naming conventions (camelCase functions alongside snake_case).
- No docstrings on public functions – makes the code hard to use.
- Committing directly to `main` – use feature branches.
- Vague commit messages like "fix" or "update".
- Ignoring type hint errors from mypy.
- Using mutable default arguments: `def f(lst=[])` is a classic Python bug.
