"""
09 – Object-Oriented Programming: Examples
==========================================
Run this file directly:  python examples.py
Each example is wrapped in a function and called at the bottom.
"""

# ---------------------------------------------------------------------------
# Example 1 – Basic class with __init__ and methods
# ---------------------------------------------------------------------------
def example1_basic_class():
    print("=== Example 1: Basic Class ===")

    class Dog:
        """A simple Dog class."""

        def __init__(self, name: str, age: int):
            self.name = name
            self.age  = age

        def bark(self) -> str:
            return f"{self.name} says: Woof!"

        def human_age(self) -> int:
            return self.age * 7

    rex = Dog("Rex", 3)
    print(rex.bark())                    # Rex says: Woof!
    print(f"{rex.name} is {rex.human_age()} in human years")  # Rex is 21 in human years

    buddy = Dog("Buddy", 5)
    print(f"{buddy.name} is {buddy.age} years old")           # Buddy is 5 years old


# ---------------------------------------------------------------------------
# Example 2 – Class vs instance attributes
# ---------------------------------------------------------------------------
def example2_class_vs_instance():
    print("\n=== Example 2: Class vs Instance Attributes ===")

    class Counter:
        count = 0            # CLASS attribute – shared by every instance

        def __init__(self, label: str):
            Counter.count += 1
            self.label = label       # INSTANCE attribute – unique per object
            self.id    = Counter.count

    a = Counter("first")
    b = Counter("second")
    c = Counter("third")

    print(f"Total counters created: {Counter.count}")   # 3
    print(f"a.id={a.id}, b.id={b.id}, c.id={c.id}")    # 1, 2, 3
    # Each instance has its own 'label' and 'id', but 'count' is shared.


# ---------------------------------------------------------------------------
# Example 3 – Inheritance
# ---------------------------------------------------------------------------
def example3_inheritance():
    print("\n=== Example 3: Inheritance ===")

    class Animal:
        def __init__(self, name: str):
            self.name = name

        def speak(self) -> str:
            return f"{self.name} makes a sound."

        def describe(self) -> str:
            return f"I am {self.name}"

    class Dog(Animal):
        def speak(self) -> str:          # override parent method
            return f"{self.name} says Woof!"

    class Cat(Animal):
        def speak(self) -> str:
            return f"{self.name} says Meow!"

    animals = [Animal("Generic"), Dog("Rex"), Cat("Whiskers")]
    for a in animals:
        print(a.speak())
        print(a.describe())             # inherited from Animal, not overridden


# ---------------------------------------------------------------------------
# Example 4 – Multiple inheritance and MRO
# ---------------------------------------------------------------------------
def example4_multiple_inheritance_mro():
    print("\n=== Example 4: Multiple Inheritance and MRO ===")

    class Flyable:
        def move(self):
            return "flying"

    class Swimmable:
        def move(self):
            return "swimming"

    class Duck(Flyable, Swimmable):
        # Python resolves 'move' left-to-right: Flyable first
        pass

    class TalkingDuck(Duck):
        def speak(self):
            return "Quack!"

    d = TalkingDuck()
    print(d.move())          # flying  (Flyable is first in MRO)
    print(d.speak())         # Quack!

    print("MRO:", [cls.__name__ for cls in TalkingDuck.__mro__])
    # ['TalkingDuck', 'Duck', 'Flyable', 'Swimmable', 'object']


# ---------------------------------------------------------------------------
# Example 5 – Polymorphism with method overriding
# ---------------------------------------------------------------------------
def example5_polymorphism():
    print("\n=== Example 5: Polymorphism ===")

    class Shape:
        def area(self) -> float:
            raise NotImplementedError

        def describe(self) -> str:
            return f"I am a {type(self).__name__} with area {self.area():.2f}"

    class Circle(Shape):
        def __init__(self, radius: float):
            self.radius = radius

        def area(self) -> float:
            import math
            return math.pi * self.radius ** 2

    class Rectangle(Shape):
        def __init__(self, width: float, height: float):
            self.width  = width
            self.height = height

        def area(self) -> float:
            return self.width * self.height

    class Triangle(Shape):
        def __init__(self, base: float, height: float):
            self.base   = base
            self.height = height

        def area(self) -> float:
            return 0.5 * self.base * self.height

    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
    for shape in shapes:
        print(shape.describe())   # same interface, different behaviour


# ---------------------------------------------------------------------------
# Example 6 – Dunder methods (__str__, __repr__, __len__, __eq__)
# ---------------------------------------------------------------------------
def example6_dunder_methods():
    print("\n=== Example 6: Dunder Methods ===")

    class Book:
        def __init__(self, title: str, author: str, pages: int):
            self.title  = title
            self.author = author
            self.pages  = pages

        def __repr__(self) -> str:
            # Should ideally look like a constructor call
            return f"Book({self.title!r}, {self.author!r}, {self.pages})"

        def __str__(self) -> str:
            # Human-friendly
            return f'"{self.title}" by {self.author}'

        def __len__(self) -> int:
            return self.pages

        def __eq__(self, other) -> bool:
            if not isinstance(other, Book):
                return NotImplemented
            return self.title == other.title and self.author == other.author

    b1 = Book("1984", "Orwell", 328)
    b2 = Book("1984", "Orwell", 328)
    b3 = Book("Brave New World", "Huxley", 311)

    print(str(b1))         # "1984" by Orwell
    print(repr(b1))        # Book('1984', 'Orwell', 328)
    print(len(b1))         # 328
    print(b1 == b2)        # True
    print(b1 == b3)        # False


# ---------------------------------------------------------------------------
# Example 7 – Property decorator (getter / setter / deleter)
# ---------------------------------------------------------------------------
def example7_property():
    print("\n=== Example 7: Property Decorator ===")

    class Temperature:
        def __init__(self, celsius: float = 0.0):
            self._celsius = celsius   # underscore = "internal" storage

        @property
        def celsius(self) -> float:
            return self._celsius

        @celsius.setter
        def celsius(self, value: float):
            if value < -273.15:
                raise ValueError(f"Temperature below absolute zero: {value}")
            self._celsius = value

        @property
        def fahrenheit(self) -> float:
            return self._celsius * 9 / 5 + 32

        @fahrenheit.setter
        def fahrenheit(self, value: float):
            self.celsius = (value - 32) * 5 / 9   # reuse celsius setter validation

        def __repr__(self):
            return f"Temperature({self._celsius}°C / {self.fahrenheit}°F)"

    t = Temperature(100)
    print(t)                  # Temperature(100°C / 212.0°F)
    t.fahrenheit = 32
    print(t)                  # Temperature(0.0°C / 32.0°F)

    try:
        t.celsius = -300      # should raise ValueError
    except ValueError as e:
        print(f"Caught: {e}") # Caught: Temperature below absolute zero: -300


# ---------------------------------------------------------------------------
# Example 8 – Class method and static method
# ---------------------------------------------------------------------------
def example8_classmethod_staticmethod():
    print("\n=== Example 8: Class Method and Static Method ===")

    class Date:
        def __init__(self, year: int, month: int, day: int):
            self.year  = year
            self.month = month
            self.day   = day

        @classmethod
        def from_string(cls, date_str: str) -> "Date":
            """Factory method: create a Date from 'YYYY-MM-DD' string."""
            year, month, day = map(int, date_str.split("-"))
            return cls(year, month, day)   # works even if subclassed

        @staticmethod
        def is_valid(year: int, month: int, day: int) -> bool:
            """Utility: validate without needing an instance."""
            return 1 <= month <= 12 and 1 <= day <= 31

        def __str__(self):
            return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    d1 = Date(2024, 6, 15)
    d2 = Date.from_string("2024-12-25")       # class method as factory
    print(d1, d2)                              # 2024-06-15 2024-12-25

    print(Date.is_valid(2024, 2, 29))          # True
    print(Date.is_valid(2024, 13, 1))          # False (month 13 invalid)


# ---------------------------------------------------------------------------
# Example 9 – Abstract class (abc module)
# ---------------------------------------------------------------------------
def example9_abstract_class():
    print("\n=== Example 9: Abstract Class ===")

    from abc import ABC, abstractmethod

    class Vehicle(ABC):
        def __init__(self, make: str, model: str):
            self.make  = make
            self.model = model

        @abstractmethod
        def fuel_type(self) -> str:
            """Every vehicle must declare its fuel type."""
            ...

        @abstractmethod
        def max_speed(self) -> int:
            """Every vehicle must declare its max speed in km/h."""
            ...

        def describe(self) -> str:
            return (f"{self.make} {self.model}: {self.fuel_type()} powered, "
                    f"top speed {self.max_speed()} km/h")

    class ElectricCar(Vehicle):
        def fuel_type(self) -> str:  return "electric"
        def max_speed(self) -> int:  return 250

    class PetrolBike(Vehicle):
        def fuel_type(self) -> str:  return "petrol"
        def max_speed(self) -> int:  return 180

    car  = ElectricCar("Tesla", "Model 3")
    bike = PetrolBike("Honda", "CBR")
    print(car.describe())   # Tesla Model 3: electric powered, top speed 250 km/h
    print(bike.describe())  # Honda CBR: petrol powered, top speed 180 km/h

    # Cannot instantiate abstract class directly
    try:
        v = Vehicle("X", "Y")
    except TypeError as e:
        print(f"Caught: {e}")


# ---------------------------------------------------------------------------
# Example 10 – Operator overloading
# ---------------------------------------------------------------------------
def example10_operator_overloading():
    print("\n=== Example 10: Operator Overloading ===")

    class Vector:
        """2D vector with arithmetic operator support."""

        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y

        def __repr__(self) -> str:
            return f"Vector({self.x}, {self.y})"

        def __add__(self, other: "Vector") -> "Vector":
            return Vector(self.x + other.x, self.y + other.y)

        def __sub__(self, other: "Vector") -> "Vector":
            return Vector(self.x - other.x, self.y - other.y)

        def __mul__(self, scalar: float) -> "Vector":
            return Vector(self.x * scalar, self.y * scalar)

        def __rmul__(self, scalar: float) -> "Vector":
            # Allows:  3 * v  (scalar on the left)
            return self.__mul__(scalar)

        def __eq__(self, other) -> bool:
            return isinstance(other, Vector) and self.x == other.x and self.y == other.y

        def __abs__(self) -> float:
            return (self.x ** 2 + self.y ** 2) ** 0.5

        def __iter__(self):
            yield self.x
            yield self.y

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1 + v2)         # Vector(4, 6)
    print(v2 - v1)         # Vector(2, 2)
    print(v1 * 3)          # Vector(3, 6)
    print(3 * v1)          # Vector(3, 6)  — uses __rmul__
    print(abs(v2))         # 5.0
    x, y = v1              # unpacking via __iter__
    print(f"x={x}, y={y}") # x=1, y=2


# ---------------------------------------------------------------------------
# Run all examples
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    example1_basic_class()
    example2_class_vs_instance()
    example3_inheritance()
    example4_multiple_inheritance_mro()
    example5_polymorphism()
    example6_dunder_methods()
    example7_property()
    example8_classmethod_staticmethod()
    example9_abstract_class()
    example10_operator_overloading()
