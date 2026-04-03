# 12 – Modules, Packages & Libraries Key Points (Quick Reference)

## import Syntax

```python
import module                      # whole module; use as module.name
import module as alias             # shorten a long name
from module import name            # bring one name into scope
from module import name as alias   # import with alias
from module import a, b, c         # multiple names at once
from module import *               # ⚠ avoid – pollutes namespace
```

---

## `__name__ == "__main__"` Pattern

```python
# script.py
def main():
    ...

if __name__ == "__main__":
    main()    # only runs when executed directly, NOT when imported
```

---

## Standard Library Quick Reference

### `os` Module

| Call                               | Result / Effect                          |
|------------------------------------|------------------------------------------|
| `os.getcwd()`                      | Current working directory string         |
| `os.listdir(path)`                 | List directory contents                  |
| `os.path.join(a, b)`               | Cross-platform path join                 |
| `os.path.exists(p)`                | True/False                               |
| `os.path.isfile(p)` / `isdir(p)`   | Type checks                              |
| `os.path.basename(p)` / `dirname`  | Last component / parent dir              |
| `os.path.splitext("f.py")`         | `("f", ".py")`                           |
| `os.makedirs(p, exist_ok=True)`    | Create directories (including parents)   |
| `os.environ.get("VAR", default)`   | Read environment variable                |

### `sys` Module

| Name                      | Purpose                              |
|---------------------------|--------------------------------------|
| `sys.argv`                | Command-line arguments list          |
| `sys.path`                | Module search paths                  |
| `sys.exit(code)`          | Exit interpreter                     |
| `sys.version`             | Python version string                |
| `sys.platform`            | OS string (`"linux"`, `"win32"`, …)  |
| `sys.stdin/stdout/stderr` | Standard streams                     |

### `json` Module

```python
json.dumps(obj)           # Python → JSON string
json.dumps(obj, indent=2) # pretty-printed
json.loads(text)          # JSON string → Python
json.dump(obj, fp)        # Python → file
json.load(fp)             # file → Python
```

### `re` Module

```python
re.match(pat, s)          # match at start
re.search(pat, s)         # match anywhere → Match or None
re.findall(pat, s)        # list of all matches (strings)
re.sub(pat, repl, s)      # replace matches
re.split(pat, s)          # split by pattern
m.group(0)                # full match; group(1) = first capture group
```

### `datetime` Module

```python
from datetime import date, datetime, timedelta
date.today()
datetime.now()
datetime(2024, 12, 25)
dt.strftime("%Y-%m-%d")   # format to string
datetime.strptime(s, fmt) # parse string
d + timedelta(days=7)     # date arithmetic
```

### `math` Module

```python
math.sqrt(x)   math.pi    math.e
math.floor(x)  math.ceil(x)   math.factorial(n)
math.log(x, base)   math.sin/cos/tan(radians)
math.gcd(a, b)   math.comb(n, k)   math.inf
```

### `random` Module

```python
random.random()            # float [0, 1)
random.randint(a, b)       # int [a, b] inclusive
random.choice(seq)         # one random element
random.sample(seq, k)      # k unique elements
random.shuffle(lst)        # in-place shuffle
random.seed(n)             # reproducible
```

---

## Package Structure

```
mypackage/
├── __init__.py      ← required; may re-export public API
├── module_a.py
└── subpackage/
    ├── __init__.py
    └── module_b.py
```

Relative imports inside package:
```python
from . import module_a          # sibling module
from .module_a import MyClass   # specific name
from .. import parent_module    # one level up
```

---

## pip & venv Cheatsheet

```bash
python -m venv venv              # create virtual environment
source venv/bin/activate         # activate (Linux/macOS)
pip install package==1.2.3       # install specific version
pip freeze > requirements.txt    # save dependencies
pip install -r requirements.txt  # install from file
pip list                         # show installed packages
deactivate                       # exit virtual environment
```

---

## Common Pitfalls Checklist

- [ ] File named same as stdlib module (e.g., `os.py`, `json.py`)
- [ ] `from module import *` used in non-REPL code
- [ ] Missing `if __name__ == "__main__":` guard in script
- [ ] Circular imports between modules
- [ ] Not using virtual environments for projects
- [ ] Hardcoded `/` paths instead of `os.path.join` / `pathlib`
- [ ] `__init__.py` missing from package directory
