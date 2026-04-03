"""
09 – Object-Oriented Programming: Practice Problems
====================================================
Each problem is stated as a comment block, followed by the full solution.
Run this file directly:  python practice.py
"""

# ===========================================================================
# Problem 1 – Design a BankAccount class
# ===========================================================================
# Design a BankAccount class that:
#   - Stores owner name and balance (default 0)
#   - Has deposit(amount) and withdraw(amount) methods
#   - withdraw raises ValueError if insufficient funds
#   - Has a __str__ that shows owner and current balance
#   - Tracks total number of transactions (class attribute)
# ===========================================================================

class BankAccount:
    total_transactions = 0   # class attribute – shared across all accounts

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner   = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        BankAccount.total_transactions += 1

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: balance is {self._balance:.2f}")
        self._balance -= amount
        BankAccount.total_transactions += 1

    def __str__(self) -> str:
        return f"BankAccount({self.owner}, balance={self._balance:.2f})"

    def __repr__(self) -> str:
        return f"BankAccount({self.owner!r}, {self._balance})"


def test_problem1():
    print("=== Problem 1: BankAccount ===")
    acc = BankAccount("Alice", 100.0)
    acc.deposit(50)
    acc.withdraw(30)
    print(acc)                              # BankAccount(Alice, balance=120.00)
    print(f"Transactions: {BankAccount.total_transactions}")  # 2

    try:
        acc.withdraw(500)
    except ValueError as e:
        print(f"Caught: {e}")              # Caught: Insufficient funds: ...


# ===========================================================================
# Problem 2 – Inheritance hierarchy: Animal → Dog / Cat
# ===========================================================================
# Create:
#   - Animal base class: __init__(name, age), speak(), __str__
#   - Dog(Animal): speak() returns "Woof!", can fetch(item)
#   - Cat(Animal): speak() returns "Meow!", can purr()
#   - GuardDog(Dog): overrides speak() to add "BARK BARK!" prefix
# ===========================================================================

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age  = age

    def speak(self) -> str:
        return f"{self.name} makes a sound."

    def __str__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r}, age={self.age})"


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Woof!"

    def fetch(self, item: str) -> str:
        return f"{self.name} fetches the {item}!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Meow!"

    def purr(self) -> str:
        return f"{self.name} purrs... ~purrr~"


class GuardDog(Dog):
    def speak(self) -> str:
        parent_sound = super().speak()
        return f"BARK BARK! {parent_sound}"


def test_problem2():
    print("\n=== Problem 2: Animal Hierarchy ===")
    animals = [Dog("Rex", 3), Cat("Whiskers", 2), GuardDog("Titan", 4)]
    for a in animals:
        print(a)
        print(a.speak())
    print(Dog("Buddy", 1).fetch("ball"))
    print(Cat("Luna", 3).purr())


# ===========================================================================
# Problem 3 – Implement comparison operators for a Student class
# ===========================================================================
# Create a Student class with name and gpa attributes.
# Implement __eq__, __lt__, __le__, __gt__, __ge__ so students
# can be compared and sorted by GPA.
# Also implement __repr__.
# ===========================================================================

from functools import total_ordering

@total_ordering   # fills in the missing comparison methods automatically
class Student:
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa  = gpa

    def __repr__(self) -> str:
        return f"Student({self.name!r}, gpa={self.gpa})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa == other.gpa

    def __lt__(self, other) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.gpa < other.gpa


def test_problem3():
    print("\n=== Problem 3: Student Comparison Operators ===")
    students = [
        Student("Alice", 3.9),
        Student("Bob",   3.5),
        Student("Carol", 3.7),
    ]
    print("Unsorted:", students)
    students.sort()                        # uses __lt__
    print("By GPA asc:", students)
    print("Best student:", max(students))  # uses __gt__ (from total_ordering)
    print("Alice > Bob:", Student("Alice", 3.9) > Student("Bob", 3.5))  # True


# ===========================================================================
# Problem 4 – Class with properties and validation
# ===========================================================================
# Create a Rectangle class with:
#   - width and height properties that reject non-positive values
#   - Read-only area and perimeter properties (computed, no setter)
#   - __str__ showing dimensions, area, perimeter
# ===========================================================================

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width  = width    # goes through property setter
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        if value <= 0:
            raise ValueError(f"Width must be positive, got {value}")
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        if value <= 0:
            raise ValueError(f"Height must be positive, got {value}")
        self._height = value

    @property
    def area(self) -> float:
        return self._width * self._height

    @property
    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

    def __str__(self) -> str:
        return (f"Rectangle(w={self.width}, h={self.height}) "
                f"area={self.area}, perimeter={self.perimeter}")


def test_problem4():
    print("\n=== Problem 4: Rectangle with Properties ===")
    r = Rectangle(5, 3)
    print(r)                    # Rectangle(w=5, h=3) area=15, perimeter=16
    r.width = 10
    print(r)                    # Rectangle(w=10, h=3) area=30, perimeter=26

    try:
        r.height = -1
    except ValueError as e:
        print(f"Caught: {e}")   # Height must be positive, got -1


# ===========================================================================
# Problem 5 – Mixin classes
# ===========================================================================
# Create:
#   - JSONMixin: adds to_json() method (returns dict representation)
#   - LogMixin:  adds log() method (prints timestamped message)
# Apply both to a Product class.
# ===========================================================================

import json
from datetime import datetime


class JSONMixin:
    def to_json(self) -> str:
        # Serialize the instance's public attributes to JSON
        data = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return json.dumps(data, indent=2)


class LogMixin:
    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {type(self).__name__}: {message}")


class Product(JSONMixin, LogMixin):
    def __init__(self, name: str, price: float, stock: int):
        self.name  = name
        self.price = price
        self.stock = stock

    def sell(self, qty: int) -> None:
        if qty > self.stock:
            raise ValueError("Not enough stock")
        self.stock -= qty
        self.log(f"Sold {qty} units of '{self.name}'. Stock: {self.stock}")


def test_problem5():
    print("\n=== Problem 5: Mixins ===")
    p = Product("Widget", 9.99, 100)
    p.sell(10)
    print(p.to_json())


# ===========================================================================
# Problem 6 – Abstract class for a plugin system
# ===========================================================================
# Design an abstract Exporter class with:
#   - abstract method export(data: list) -> str
#   - abstract property format_name -> str
# Implement CSVExporter and JSONExporter.
# ===========================================================================

from abc import ABC, abstractmethod


class Exporter(ABC):
    @property
    @abstractmethod
    def format_name(self) -> str: ...

    @abstractmethod
    def export(self, data: list) -> str: ...

    def export_and_announce(self, data: list) -> str:
        result = self.export(data)
        print(f"[{self.format_name}] Export complete ({len(result)} chars)")
        return result


class CSVExporter(Exporter):
    @property
    def format_name(self) -> str:
        return "CSV"

    def export(self, data: list) -> str:
        if not data:
            return ""
        header = ",".join(data[0].keys())
        rows   = [",".join(str(v) for v in row.values()) for row in data]
        return header + "\n" + "\n".join(rows)


class JSONExporter(Exporter):
    @property
    def format_name(self) -> str:
        return "JSON"

    def export(self, data: list) -> str:
        return json.dumps(data, indent=2)


def test_problem6():
    print("\n=== Problem 6: Abstract Exporter ===")
    records = [
        {"name": "Alice", "score": 95},
        {"name": "Bob",   "score": 87},
    ]
    for exporter in [CSVExporter(), JSONExporter()]:
        output = exporter.export_and_announce(records)
        print(output)
        print()


# ===========================================================================
# Problem 7 – Iterator class
# ===========================================================================
# Implement a Countdown class that iterates from n down to 1.
# Must support: for x in Countdown(5):  and  list(Countdown(3))
# ===========================================================================

class Countdown:
    def __init__(self, start: int):
        if start < 0:
            raise ValueError("start must be non-negative")
        self.start = start

    def __iter__(self):
        current = self.start
        while current >= 1:
            yield current
            current -= 1

    def __len__(self) -> int:
        return self.start

    def __repr__(self) -> str:
        return f"Countdown({self.start})"


def test_problem7():
    print("\n=== Problem 7: Countdown Iterator ===")
    print(list(Countdown(5)))    # [5, 4, 3, 2, 1]
    for n in Countdown(3):
        print(n, end=" ")        # 3 2 1
    print()
    print(len(Countdown(10)))    # 10


# ===========================================================================
# Problem 8 – Callable object (__call__)
# ===========================================================================
# Implement a RateLimiter class that acts like a function.
# When called, it increments a counter and raises RuntimeError
# if the call count exceeds a set limit within the same instance lifetime.
# ===========================================================================

class RateLimiter:
    def __init__(self, max_calls: int):
        self.max_calls = max_calls
        self._calls    = 0

    def __call__(self, func_name: str = "action") -> str:
        self._calls += 1
        if self._calls > self.max_calls:
            raise RuntimeError(
                f"Rate limit exceeded: {self._calls}/{self.max_calls} calls"
            )
        return f"'{func_name}' executed (call {self._calls}/{self.max_calls})"

    def reset(self) -> None:
        self._calls = 0

    def __repr__(self) -> str:
        return f"RateLimiter(max={self.max_calls}, used={self._calls})"


def test_problem8():
    print("\n=== Problem 8: Callable RateLimiter ===")
    limiter = RateLimiter(max_calls=3)
    for _ in range(3):
        print(limiter("API call"))

    try:
        limiter("one more")
    except RuntimeError as e:
        print(f"Caught: {e}")

    limiter.reset()
    print("After reset:", limiter)


# ===========================================================================
# Problem 9 – Context manager class (__enter__ / __exit__)
# ===========================================================================
# Implement a Timer context manager that:
#   - Records start time on enter
#   - Records end time and prints elapsed seconds on exit
#   - Exposes elapsed attribute after the block
# ===========================================================================

import time


class Timer:
    def __enter__(self) -> "Timer":
        self._start   = time.perf_counter()
        self.elapsed  = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.elapsed = time.perf_counter() - self._start
        print(f"Elapsed: {self.elapsed:.6f}s")
        return False   # do not suppress exceptions


def test_problem9():
    print("\n=== Problem 9: Timer Context Manager ===")
    with Timer() as t:
        total = sum(range(1_000_000))
    print(f"Sum={total}, took {t.elapsed:.4f}s")


# ===========================================================================
# Run all problems
# ===========================================================================
if __name__ == "__main__":
    test_problem1()
    test_problem2()
    test_problem3()
    test_problem4()
    test_problem5()
    test_problem6()
    test_problem7()
    test_problem8()
    test_problem9()
