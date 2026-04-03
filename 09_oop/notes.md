# 09 – Object-Oriented Programming (OOP)

## 1. Classes and Objects

A **class** is a blueprint for creating objects. An **object** (instance) is a concrete
realisation of that blueprint, with its own data (attributes) and behaviours (methods).

```
Class  ──►  Blueprint / Template
Object ──►  Concrete instance created from the blueprint
```

Everything in Python is an object – integers, strings, lists, functions.

---

## 2. Class Definition Syntax

```python
class ClassName:          # PascalCase by convention
    class_attribute = 0   # shared by ALL instances

    def __init__(self, arg1, arg2):
        self.instance_attr1 = arg1   # unique per instance
        self.instance_attr2 = arg2

    def instance_method(self):
        return self.instance_attr1
```

---

## 3. `__init__` and Instance Attributes

`__init__` is the **initialiser** (not constructor – `__new__` is the actual constructor).
It runs automatically when you call `ClassName(...)` and sets up instance-specific data.

```python
class Student:
    def __init__(self, name, grade):
        self.name  = name    # instance attribute
        self.grade = grade
```

`self` refers to the specific instance being created. It is always the first parameter of
instance methods but is passed automatically by Python.

---

## 4. Instance Methods vs Class Methods vs Static Methods

| Type              | Decorator        | First param | Has access to          |
|-------------------|------------------|-------------|------------------------|
| Instance method   | (none)           | `self`      | instance & class data  |
| Class method      | `@classmethod`   | `cls`       | class data only        |
| Static method     | `@staticmethod`  | (none)      | neither                |

```python
class MyClass:
    count = 0

    def instance_method(self):          # accesses self.x and MyClass.count
        return self.x

    @classmethod
    def class_method(cls):              # factory or counter patterns
        cls.count += 1

    @staticmethod
    def static_method(a, b):            # utility, no class/instance access needed
        return a + b
```

---

## 5. Inheritance

**Single inheritance** – one parent:

```python
class Animal:
    def speak(self): return "..."

class Dog(Animal):
    def speak(self): return "Woof"
```

**Multiple inheritance** – several parents:

```python
class Flyable:
    def fly(self): return "flying"

class Swimmable:
    def swim(self): return "swimming"

class Duck(Flyable, Swimmable):
    pass
```

---

## 6. Method Resolution Order (MRO)

Python uses the **C3 linearisation** algorithm to decide which class in the hierarchy
provides a method when there are multiple candidates. You can inspect it with:

```python
print(Duck.__mro__)     # tuple of classes in resolution order
print(Duck.mro())       # same, as a list
```

Rule of thumb: left-to-right, depth-first, but each class appears only once and a class
always precedes its parents.

---

## 7. Polymorphism

Different classes can share the same method name but provide different implementations.
Code that calls the method does not need to know the concrete type:

```python
for animal in [Dog(), Cat(), Bird()]:
    print(animal.speak())   # each responds differently
```

Python uses **duck typing**: if it has the right method, it works – no explicit interface
needed.

---

## 8. Encapsulation and Name Mangling

Python does not have true private members, but uses conventions:

| Naming           | Meaning                                      |
|------------------|----------------------------------------------|
| `name`           | Public – use freely                          |
| `_name`          | Protected – "internal use" by convention     |
| `__name`         | Name-mangled to `_ClassName__name`; harder to access from outside |

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance   # stored as _Account__balance

    def get_balance(self):
        return self.__balance
```

---

## 9. Dunder / Magic Methods

These allow your class to integrate with Python's built-in operations.

| Method                   | Triggered by                          |
|--------------------------|---------------------------------------|
| `__init__(self, ...)`    | `ClassName(...)`                      |
| `__str__(self)`          | `str(obj)`, `print(obj)`              |
| `__repr__(self)`         | `repr(obj)`, interactive REPL display |
| `__len__(self)`          | `len(obj)`                            |
| `__eq__(self, other)`    | `obj == other`                        |
| `__lt__(self, other)`    | `obj < other`                         |
| `__add__(self, other)`   | `obj + other`                         |
| `__iter__(self)`         | `for x in obj`, `iter(obj)`           |
| `__next__(self)`         | `next(obj)`                           |
| `__contains__(self, x)`  | `x in obj`                            |
| `__getitem__(self, key)` | `obj[key]`                            |
| `__del__(self)`          | Object about to be garbage-collected  |

Best practice: always define `__repr__` so that objects are inspectable; define `__str__`
for human-readable output separately.

---

## 10. Property Decorator

`@property` turns a method into an attribute-style getter. Add `@attr.setter` and
`@attr.deleter` for controlled write and delete access:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):            # getter
        return self._radius

    @radius.setter
    def radius(self, value):     # setter with validation
        if value < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = value

    @radius.deleter
    def radius(self):            # deleter
        del self._radius
```

Usage: `c.radius = 5` (calls setter), `c.radius` (calls getter).

---

## 11. `super()` Function

`super()` returns a proxy to the **next class in the MRO**, enabling you to call the
parent's implementation without hard-coding the class name:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # call Animal.__init__
        self.breed = breed
```

Using `super()` is essential in cooperative multiple inheritance.

---

## 12. Abstract Classes (`abc` module)

An **abstract class** cannot be instantiated directly. It defines an interface that
subclasses must implement:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self) -> float:
        return self.w * self.h
```

Attempting `Shape()` raises `TypeError`. Any subclass that omits `area` also cannot be
instantiated.

---

## 13. Common Mistakes

1. **Mutable default argument in `__init__`**
   ```python
   # WRONG – all instances share the same list
   def __init__(self, items=[]):
       self.items = items

   # CORRECT
   def __init__(self, items=None):
       self.items = items if items is not None else []
   ```

2. **Forgetting `self`** – calling `method()` instead of `self.method()` inside the class.

3. **Confusing class and instance attributes**
   ```python
   class A:
       x = 0          # class attribute
   a = A()
   a.x = 5            # creates an INSTANCE attribute; A.x is still 0
   ```

4. **`__str__` vs `__repr__`** – `__str__` should be human-readable; `__repr__` should
   ideally be a string that `eval()` could use to recreate the object.

5. **Diamond problem without `super()`** – in multiple inheritance, not using `super()`
   can cause a parent's `__init__` to be called twice or not at all.

6. **Overriding without calling super** – forgetting `super().__init__(...)` leaves
   parent attributes uninitialised.

7. **Using `__del__` for cleanup** – `__del__` is called by the GC at an unpredictable
   time; use context managers (`with` / `__enter__` / `__exit__`) instead.
