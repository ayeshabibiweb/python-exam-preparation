# 09 – OOP Key Points (Quick Reference)

## Class Definition Skeleton

```python
class ClassName(ParentClass):
    class_attr = value                        # shared by all instances

    def __init__(self, arg):
        self.instance_attr = arg              # unique per instance

    def instance_method(self): ...           # receives self
    @classmethod
    def class_method(cls): ...               # receives cls
    @staticmethod
    def static_method(): ...                 # receives nothing
```

---

## Method Types at a Glance

| Decorator        | First param | Can access instance? | Can access class? | Typical use             |
|------------------|-------------|----------------------|-------------------|-------------------------|
| (none)           | `self`      | ✅                   | ✅                | Most behaviour          |
| `@classmethod`   | `cls`       | ❌                   | ✅                | Factory, counter        |
| `@staticmethod`  | –           | ❌                   | ❌                | Pure utility            |

---

## Inheritance Syntax

```python
class Child(Parent):           # single
class Child(Parent1, Parent2): # multiple
```

Check MRO:  `ClassName.__mro__`  or  `ClassName.mro()`

---

## Dunder Methods Table

| Dunder              | Purpose / Triggered by              |
|---------------------|-------------------------------------|
| `__init__`          | Initialisation (`ClassName(...)`)   |
| `__str__`           | `str(obj)`, `print(obj)`            |
| `__repr__`          | `repr(obj)`, REPL display           |
| `__len__`           | `len(obj)`                          |
| `__eq__`            | `obj == other`                      |
| `__lt__`            | `obj < other`                       |
| `__le__`            | `obj <= other`                      |
| `__gt__`            | `obj > other`                       |
| `__ge__`            | `obj >= other`                      |
| `__add__`           | `obj + other`                       |
| `__sub__`           | `obj - other`                       |
| `__mul__`           | `obj * other`                       |
| `__iter__`          | `for x in obj`                      |
| `__next__`          | `next(obj)`                         |
| `__contains__`      | `x in obj`                          |
| `__getitem__`       | `obj[key]`                          |
| `__setitem__`       | `obj[key] = val`                    |
| `__delitem__`       | `del obj[key]`                      |
| `__enter__`         | `with obj as ...`                   |
| `__exit__`          | End of `with` block                 |
| `__call__`          | `obj(...)`                          |
| `__bool__`          | `bool(obj)`, `if obj:`              |
| `__hash__`          | `hash(obj)`, dict/set keys          |

---

## Property Decorator

```python
class MyClass:
    @property
    def value(self):          # getter
        return self._value

    @value.setter
    def value(self, v):       # setter (validation here)
        self._value = v

    @value.deleter
    def value(self):          # deleter
        del self._value
```

---

## Abstract Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...       # subclass MUST implement
```

---

## Name Mangling

| Name       | Stored as            | Access outside class |
|------------|----------------------|----------------------|
| `name`     | `name`               | Direct               |
| `_name`    | `_name`              | Allowed (convention) |
| `__name`   | `_ClassName__name`   | Discouraged          |

---

## super() Pattern

```python
class Child(Parent):
    def __init__(self, a, b):
        super().__init__(a)   # call Parent.__init__
        self.b = b
```

---

## Common Pitfalls Checklist

- [ ] Mutable default argument → use `None` sentinel
- [ ] Class vs instance attribute confusion
- [ ] Forgot `self` parameter on method
- [ ] `__str__` returns non-string
- [ ] Overrode method without calling `super().__init__`
- [ ] Using `__del__` instead of context manager for cleanup
