# 12 – Modules, Packages, and Libraries

## 1. Module Definition

A **module** is any `.py` file. When you import it, Python executes the file once and
caches it in `sys.modules`. Subsequent imports return the cached version.

```
my_project/
├── utils.py          ← a module
├── models.py         ← another module
└── main.py
```

---

## 2. `import` Statement Variations

```python
import math                        # import the whole module
import math as m                   # alias to shorten name
from math import sqrt, pi          # import specific names into current namespace
from math import sqrt as sq        # import with alias
from math import *                 # import everything (avoid – pollutes namespace)
```

Import resolution order:
1. `sys.modules` cache
2. Built-in modules
3. Directories in `sys.path` (current directory, `PYTHONPATH`, standard library, site-packages)

---

## 3. `__name__ == "__main__"` Pattern

Every module has a `__name__` attribute:
- When run directly: `__name__ == "__main__"`
- When imported: `__name__ == "module_filename"`

```python
# utils.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    # This block runs ONLY when utils.py is executed directly
    print(add(2, 3))
```

This pattern lets a file serve as both a reusable library and a runnable script.

---

## 4. Standard Library Overview

Python ships with "batteries included" – over 200 built-in modules. Key modules:

| Module       | Purpose                                          |
|--------------|--------------------------------------------------|
| `os`         | OS interaction (paths, files, environment)       |
| `sys`        | Interpreter internals (argv, path, exit)         |
| `json`       | JSON encoding / decoding                         |
| `re`         | Regular expressions                              |
| `datetime`   | Date and time manipulation                       |
| `math`       | Mathematical functions                           |
| `random`     | Random number generation                         |
| `collections`| Specialised container types                      |
| `itertools`  | Iterators and combinatorics                      |
| `functools`  | Higher-order functions (lru_cache, reduce, …)    |
| `pathlib`    | Object-oriented file paths                       |
| `copy`       | Shallow and deep copy                            |
| `io`         | I/O streams                                      |
| `time`       | Time-related utilities                           |
| `logging`    | Flexible event logging                           |
| `unittest`   | Unit testing framework                           |
| `csv`        | CSV file reading / writing                       |
| `hashlib`    | Cryptographic hashing                            |
| `typing`     | Type hints                                       |

---

## 5. `os` Module

```python
import os

os.getcwd()                       # current working directory (string)
os.chdir("/some/path")            # change directory
os.listdir(".")                   # list directory contents
os.path.join("dir", "file.txt")   # cross-platform path join
os.path.exists("path")            # True/False
os.path.isfile("path")            # True if regular file
os.path.isdir("path")             # True if directory
os.path.abspath("relative/path")  # absolute path
os.path.basename("/a/b/c.txt")    # "c.txt"
os.path.dirname("/a/b/c.txt")     # "/a/b"
os.path.splitext("file.py")       # ("file", ".py")
os.makedirs("a/b/c", exist_ok=True)  # create nested dirs
os.environ.get("HOME", "/home")   # environment variable
```

---

## 6. `sys` Module

```python
import sys

sys.argv                   # list of command-line arguments (argv[0] = script name)
sys.path                   # list of directories Python searches for modules
sys.path.insert(0, "/my/lib")  # add a directory to the front of the search path
sys.exit(0)                # exit with code 0 (raise SystemExit)
sys.version                # Python version string
sys.platform               # "linux", "darwin", "win32"
sys.stdin / stdout / stderr # standard streams
sys.getrefcount(obj)       # reference count (see memory management)
sys.getsizeof(obj)         # memory size in bytes
```

---

## 7. `json` Module

```python
import json

# Python → JSON string
data   = {"name": "Alice", "scores": [95, 87], "active": True}
text   = json.dumps(data)                      # compact string
pretty = json.dumps(data, indent=2)            # human-readable

# JSON string → Python
parsed = json.loads(text)                      # dict

# To/from file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    loaded = json.load(f)
```

Type mapping: `dict ↔ object`, `list ↔ array`, `str ↔ string`,
`int/float ↔ number`, `True/False ↔ true/false`, `None ↔ null`.

---

## 8. `re` Module (Regular Expressions)

```python
import re

re.match(pattern, string)      # match at the START of string
re.search(pattern, string)     # first match ANYWHERE
re.findall(pattern, string)    # list of all non-overlapping matches
re.sub(pattern, repl, string)  # replace matches
re.split(pattern, string)      # split by pattern
re.compile(pattern)            # pre-compile for repeated use
```

Common pattern elements:

| Pattern  | Meaning                            |
|----------|------------------------------------|
| `.`      | Any character except newline       |
| `\d`     | Digit                              |
| `\w`     | Word character `[a-zA-Z0-9_]`      |
| `\s`     | Whitespace                         |
| `^`      | Start of string                    |
| `$`      | End of string                      |
| `*`      | 0 or more                          |
| `+`      | 1 or more                          |
| `?`      | 0 or 1                             |
| `{n,m}`  | Between n and m repetitions        |
| `[abc]`  | Character class                    |
| `()`     | Capture group                      |
| `\|`     | Alternation (OR)                   |

---

## 9. `datetime` Module

```python
from datetime import date, time, datetime, timedelta

today    = date.today()
now      = datetime.now()
specific = datetime(2024, 12, 25, 9, 0, 0)

# Arithmetic
tomorrow = today + timedelta(days=1)
diff     = datetime(2025, 1, 1) - datetime.now()   # timedelta object

# Formatting / parsing
s   = now.strftime("%Y-%m-%d %H:%M:%S")    # → "2024-06-15 14:30:00"
dt  = datetime.strptime("2024-06-15", "%Y-%m-%d")
```

---

## 10. `math` Module

```python
import math

math.sqrt(16)       # 4.0
math.floor(3.7)     # 3
math.ceil(3.2)      # 4
math.pi             # 3.141592653589793
math.e              # 2.718281828459045
math.factorial(5)   # 120
math.log(100, 10)   # 2.0  (log base 10)
math.sin / cos / tan
math.inf            # float infinity
math.isnan(x)       # True if x is NaN
math.isfinite(x)    # True if x is not inf/nan
math.gcd(12, 8)     # 4
math.comb(10, 3)    # 120 (binomial coefficient)
```

---

## 11. `random` Module

```python
import random

random.random()              # float in [0.0, 1.0)
random.randint(1, 6)         # int in [1, 6] inclusive
random.choice([1, 2, 3])     # random element
random.sample([1,2,3,4], 2)  # 2 unique elements without replacement
random.shuffle(lst)           # shuffle list in place (returns None)
random.uniform(0.0, 1.0)     # float in [a, b]
random.seed(42)              # reproducible results
```

---

## 12. Package Structure

A **package** is a directory containing an `__init__.py` file:

```
mypackage/
├── __init__.py          ← marks directory as a package; may export symbols
├── utils.py
├── models.py
└── sub/
    ├── __init__.py
    └── helpers.py
```

```python
# mypackage/__init__.py can re-export selected names:
from .utils import helper_func
from .models import User
```

Import from a package:
```python
from mypackage import helper_func
from mypackage.models import User
from mypackage.sub.helpers import util
```

---

## 13. `pip` and Virtual Environments

```bash
# Install a package
pip install requests

# Install specific version
pip install "requests==2.31.0"

# Show installed packages
pip list
pip show requests

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Create virtual environment (isolates project dependencies)
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate.bat     # Windows
deactivate
```

---

## 14. Common Mistakes

1. **Circular imports** – `a.py` imports `b.py` which imports `a.py`. Refactor: move
   shared code to a third module.

2. **`from module import *`** – pollutes namespace; hard to know where a name came from.
   Acceptable only in REPL or `__init__.py` re-exports.

3. **Modifying `sys.path` permanently** – only do so inside `if __name__ == "__main__"`
   blocks; never in library code.

4. **Forgetting `__init__.py`** – required to make a directory a regular package in
   Python < 3.3 (namespace packages work without it, but regular packages need it).

5. **Re-using names of standard library modules** – never name a file `random.py`,
   `json.py`, `os.py`, etc., as it shadows the standard library.

6. **Not using virtual environments** – global installs pollute the system Python and
   cause dependency conflicts between projects.

7. **Hardcoding file paths** – use `os.path.join` or `pathlib.Path` for cross-platform
   compatibility.
