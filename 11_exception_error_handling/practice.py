"""
11 – Exception and Error Handling: Practice Problems
=====================================================
Each problem is stated as a comment block, followed by the full solution.
Run this file directly:  python practice.py
"""


# ===========================================================================
# Problem 1 – Safe input parsing
# ===========================================================================
# Write a function safe_int(s) that:
#   - Tries to convert string s to an integer
#   - Returns the integer on success
#   - Returns None if conversion fails (no crash)
#   - Prints a user-friendly message on failure
# ===========================================================================

def safe_int(s: str):
    """Safely convert a string to int; return None on failure."""
    try:
        return int(s)
    except ValueError:
        print(f"  Could not convert '{s}' to an integer.")
        return None


def test_problem1():
    print("=== Problem 1: Safe Input Parsing ===")
    for val in ["42", "3.14", "hello", "-7", "1_000"]:
        result = safe_int(val)
        if result is not None:
            print(f"  safe_int({val!r}) = {result}")


# ===========================================================================
# Problem 2 – Robust division function
# ===========================================================================
# Write divide(a, b) that:
#   - Returns a / b
#   - Raises TypeError if either argument is not a number
#   - Raises ZeroDivisionError with a descriptive message if b == 0
#   - Include proper docstring documenting what is raised
# ===========================================================================

def divide(a, b) -> float:
    """
    Divide a by b.

    Raises:
        TypeError: if a or b are not numeric.
        ZeroDivisionError: if b is zero.
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"Dividend must be numeric, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Divisor must be numeric, got {type(b).__name__}")
    if b == 0:
        raise ZeroDivisionError(f"Cannot divide {a} by zero")
    return a / b


def test_problem2():
    print("\n=== Problem 2: Robust Division ===")
    cases = [(10, 2), (5, 0), ("a", 3), (6, "b")]
    for a, b in cases:
        try:
            print(f"  divide({a!r}, {b!r}) = {divide(a, b)}")
        except (TypeError, ZeroDivisionError) as e:
            print(f"  [{type(e).__name__}] {e}")


# ===========================================================================
# Problem 3 – Custom exception hierarchy
# ===========================================================================
# Create exceptions for an online shop:
#   ShopError (base)
#     ├── OutOfStockError(product, requested, available)
#     └── PaymentError
#           ├── InsufficientFundsError(balance, required)
#           └── CardDeclinedError(reason)
#
# Write a checkout(product, qty, stock, balance, price) function that
# raises the appropriate exception in each scenario.
# ===========================================================================

class ShopError(Exception):
    """Base for all shop errors."""

class OutOfStockError(ShopError):
    def __init__(self, product: str, requested: int, available: int):
        self.product   = product
        self.requested = requested
        self.available = available
        super().__init__(
            f"'{product}': requested {requested} but only {available} in stock"
        )

class PaymentError(ShopError):
    """Base for payment-related errors."""

class InsufficientFundsError(PaymentError):
    def __init__(self, balance: float, required: float):
        self.balance  = balance
        self.required = required
        super().__init__(
            f"Need {required:.2f} but balance is only {balance:.2f}"
        )

class CardDeclinedError(PaymentError):
    def __init__(self, reason: str):
        self.reason = reason
        super().__init__(f"Card declined: {reason}")


def checkout(product: str, qty: int, stock: int,
             balance: float, price: float, card_ok: bool = True) -> float:
    """
    Process a purchase. Returns remaining balance.

    Raises:
        OutOfStockError: not enough stock.
        InsufficientFundsError: balance too low.
        CardDeclinedError: card was declined.
    """
    if qty > stock:
        raise OutOfStockError(product, qty, stock)
    total = qty * price
    if not card_ok:
        raise CardDeclinedError("suspected fraud")
    if total > balance:
        raise InsufficientFundsError(balance, total)
    return balance - total


def test_problem3():
    print("\n=== Problem 3: Custom Exception Hierarchy ===")

    scenarios = [
        ("Widget", 5,  10, 100.0, 8.0, True),   # success
        ("Widget", 15, 10, 100.0, 8.0, True),   # OutOfStockError
        ("Gadget", 2,  10,  10.0, 8.0, True),   # InsufficientFundsError
        ("Gadget", 1,  10, 100.0, 8.0, False),  # CardDeclinedError
    ]

    for args in scenarios:
        product, qty, stock, balance, price, card_ok = args
        try:
            remaining = checkout(product, qty, stock, balance, price, card_ok)
            print(f"  Bought {qty}x {product} – remaining: {remaining:.2f}")
        except OutOfStockError as e:
            print(f"  [OutOfStock]         {e}")
        except InsufficientFundsError as e:
            print(f"  [InsufficientFunds]  {e}")
        except CardDeclinedError as e:
            print(f"  [CardDeclined]       {e}")


# ===========================================================================
# Problem 4 – Re-raise and chaining
# ===========================================================================
# Write a load_settings(raw_text) function that parses
# "key=value\nkey2=value2" format.
# If parsing fails, raise a ConfigError (custom) chained from the original.
# ===========================================================================

class ConfigError(Exception):
    """Raised when configuration cannot be parsed."""

def load_settings(raw_text: str) -> dict:
    """
    Parse key=value settings from raw_text.

    Raises:
        ConfigError: if any line cannot be parsed.
    """
    settings = {}
    for lineno, line in enumerate(raw_text.strip().splitlines(), start=1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            key, value = line.split("=", maxsplit=1)
        except ValueError as e:
            raise ConfigError(
                f"Line {lineno}: cannot parse {line!r} (missing '=')"
            ) from e
        settings[key.strip()] = value.strip()
    return settings


def test_problem4():
    print("\n=== Problem 4: Re-raise and Exception Chaining ===")

    good_config = """
    host = localhost
    port = 5432
    db   = myapp
    """
    bad_config = """
    host = localhost
    this line has no equals sign
    db = myapp
    """

    try:
        cfg = load_settings(good_config)
        print(f"  Loaded {len(cfg)} settings: {cfg}")
    except ConfigError as e:
        print(f"  ConfigError: {e}")

    try:
        load_settings(bad_config)
    except ConfigError as e:
        print(f"  ConfigError: {e}")
        print(f"  Caused by:   {e.__cause__}")


# ===========================================================================
# Problem 5 – Input validation with multiple exceptions
# ===========================================================================
# Write validate_age(value) that:
#   - Converts value to int (raises TypeError if impossible)
#   - Checks range 0 ≤ age ≤ 120 (raises ValueError if out of range)
#   - Returns the validated integer
# Write a loop that repeatedly asks for input until valid (simulate with list).
# ===========================================================================

def validate_age(value) -> int:
    try:
        age = int(value)
    except (ValueError, TypeError) as e:
        raise TypeError(f"Age must be an integer, got {value!r}") from e
    if not (0 <= age <= 120):
        raise ValueError(f"Age must be between 0 and 120, got {age}")
    return age


def test_problem5():
    print("\n=== Problem 5: Age Validation ===")
    test_inputs = ["25", "-5", "200", "abc", "0", "120"]

    for inp in test_inputs:
        try:
            age = validate_age(inp)
            print(f"  validate_age({inp!r}) = {age}")
        except TypeError as e:
            print(f"  TypeError:   {e}")
        except ValueError as e:
            print(f"  ValueError:  {e}")


# ===========================================================================
# Problem 6 – Finally for cleanup simulation
# ===========================================================================
# Simulate opening a "connection" (just a class), and ensure it is always
# closed even if an error occurs mid-operation.
# ===========================================================================

class FakeConnection:
    def __init__(self, name: str):
        self.name   = name
        self.closed = False
        print(f"  [{self.name}] Opened")

    def execute(self, cmd: str) -> str:
        if self.closed:
            raise RuntimeError("Connection already closed")
        if "fail" in cmd.lower():
            raise RuntimeError(f"Command '{cmd}' failed")
        return f"OK: {cmd}"

    def close(self) -> None:
        self.closed = True
        print(f"  [{self.name}] Closed")


def run_with_cleanup(name: str, commands: list):
    conn = FakeConnection(name)
    try:
        for cmd in commands:
            result = conn.execute(cmd)
            print(f"  {result}")
    except RuntimeError as e:
        print(f"  Error: {e}")
    finally:
        conn.close()


def test_problem6():
    print("\n=== Problem 6: Finally for Cleanup ===")
    print("  -- Success path --")
    run_with_cleanup("DB1", ["SELECT users", "INSERT record"])
    print("\n  -- Failure path --")
    run_with_cleanup("DB2", ["SELECT logs", "FAIL here", "INSERT record"])


# ===========================================================================
# Problem 7 – assert for invariant checking
# ===========================================================================
# Write a merge_sorted(a, b) function that merges two sorted lists.
# Use assert to verify inputs are sorted at the start.
# Use assert to verify the output is sorted at the end (debug check).
# ===========================================================================

def merge_sorted(a: list, b: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Raises:
        AssertionError: if a or b are not sorted (debug mode only).
    """
    assert a == sorted(a), f"First list is not sorted: {a}"
    assert b == sorted(b), f"Second list is not sorted: {b}"

    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])

    assert result == sorted(result), "Bug: merged result is not sorted!"
    return result


def test_problem7():
    print("\n=== Problem 7: assert for Invariants ===")
    print(f"  merge_sorted([1,3,5], [2,4,6]) = {merge_sorted([1,3,5],[2,4,6])}")
    print(f"  merge_sorted([], [1,2]) = {merge_sorted([],[1,2])}")
    print(f"  merge_sorted([1,4,9], []) = {merge_sorted([1,4,9],[])}")

    try:
        merge_sorted([3, 1, 2], [4, 5])   # unsorted input
    except AssertionError as e:
        print(f"  AssertionError: {e}")


# ===========================================================================
# Problem 8 – Catching and logging exceptions
# ===========================================================================
# Create a decorator @safe_call that catches all exceptions from the
# decorated function, prints a formatted error message, and returns None.
# ===========================================================================

import functools
import traceback


def safe_call(func):
    """Decorator: catch all exceptions, log them, return None."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"  [safe_call] {func.__name__} raised {type(e).__name__}: {e}")
            return None
    return wrapper


@safe_call
def risky_divide(x: float, y: float) -> float:
    return x / y


@safe_call
def risky_parse(s: str) -> int:
    return int(s)


def test_problem8():
    print("\n=== Problem 8: @safe_call Decorator ===")
    print(f"  risky_divide(10, 2) = {risky_divide(10, 2)}")
    print(f"  risky_divide(10, 0) = {risky_divide(10, 0)}")
    print(f"  risky_parse('42')   = {risky_parse('42')}")
    print(f"  risky_parse('oops') = {risky_parse('oops')}")


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
