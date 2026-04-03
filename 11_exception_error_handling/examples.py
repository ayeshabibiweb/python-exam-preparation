"""
11 – Exception and Error Handling: Examples
============================================
Run this file directly:  python examples.py
"""


# ---------------------------------------------------------------------------
# Example 1 – Basic try/except
# ---------------------------------------------------------------------------
def example1_basic_try_except():
    print("=== Example 1: Basic try/except ===")

    def safe_divide(a: float, b: float) -> float:
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return float("inf")

    print(safe_divide(10, 2))    # 5.0
    print(safe_divide(10, 0))    # Cannot divide by zero!  → inf


# ---------------------------------------------------------------------------
# Example 2 – Multiple except clauses
# ---------------------------------------------------------------------------
def example2_multiple_except():
    print("\n=== Example 2: Multiple except Clauses ===")

    def parse_and_index(data: list, key: str):
        try:
            index = int(key)
            return data[index]
        except ValueError:
            print(f"'{key}' is not a valid integer index")
        except IndexError:
            print(f"Index {key} is out of range (list length: {len(data)})")

    items = ["apple", "banana", "cherry"]
    print(parse_and_index(items, "1"))    # banana
    parse_and_index(items, "abc")         # ValueError message
    parse_and_index(items, "99")          # IndexError message


# ---------------------------------------------------------------------------
# Example 3 – try / except / else / finally
# ---------------------------------------------------------------------------
def example3_else_finally():
    print("\n=== Example 3: else and finally ===")

    def read_number(s: str) -> int:
        try:
            result = int(s)
        except ValueError as e:
            print(f"  [except] Could not convert: {e}")
            result = None
        else:
            # Runs ONLY if no exception was raised in try
            print(f"  [else]   Successfully converted: {result}")
        finally:
            # ALWAYS runs
            print(f"  [finally] Done processing '{s}'")
        return result

    read_number("42")      # else + finally run
    print()
    read_number("oops")    # except + finally run


# ---------------------------------------------------------------------------
# Example 4 – Catching exception info with 'as e'
# ---------------------------------------------------------------------------
def example4_exception_info():
    print("\n=== Example 4: Exception Info (as e) ===")

    def risky(x):
        if x < 0:
            raise ValueError(f"Expected non-negative, got {x}")
        return 100 / x

    for val in [5, 0, -3]:
        try:
            result = risky(val)
            print(f"  risky({val}) = {result:.2f}")
        except ZeroDivisionError as e:
            print(f"  ZeroDivision  | type={type(e).__name__} | msg={e}")
        except ValueError as e:
            print(f"  ValueError    | type={type(e).__name__} | msg={e}")


# ---------------------------------------------------------------------------
# Example 5 – Raising exceptions
# ---------------------------------------------------------------------------
def example5_raising():
    print("\n=== Example 5: Raising Exceptions ===")

    def set_age(age: int) -> int:
        if not isinstance(age, int):
            raise TypeError(f"age must be int, not {type(age).__name__}")
        if age < 0 or age > 150:
            raise ValueError(f"age must be 0–150, got {age}")
        return age

    for val in [25, -1, 200, "old"]:
        try:
            print(f"  set_age({val!r}) = {set_age(val)}")
        except (TypeError, ValueError) as e:
            print(f"  Error [{type(e).__name__}]: {e}")


# ---------------------------------------------------------------------------
# Example 6 – Custom exception class
# ---------------------------------------------------------------------------
def example6_custom_exception():
    print("\n=== Example 6: Custom Exceptions ===")

    class AppError(Exception):
        """Base exception for this application."""

    class InsufficientFundsError(AppError):
        def __init__(self, balance: float, amount: float):
            self.balance = balance
            self.amount  = amount
            super().__init__(
                f"Cannot withdraw {amount:.2f}: balance is only {balance:.2f}"
            )

    class AccountLockedError(AppError):
        pass

    def withdraw(balance: float, amount: float, locked: bool = False) -> float:
        if locked:
            raise AccountLockedError("Account is locked. Contact support.")
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
        return balance - amount

    # Withdraw normally
    print(f"  Balance after: {withdraw(100.0, 30.0):.2f}")

    # Insufficient funds
    try:
        withdraw(50.0, 200.0)
    except InsufficientFundsError as e:
        print(f"  [{type(e).__name__}] {e}")
        print(f"  Short by: {e.amount - e.balance:.2f}")

    # Locked account
    try:
        withdraw(100.0, 50.0, locked=True)
    except AccountLockedError as e:
        print(f"  [{type(e).__name__}] {e}")


# ---------------------------------------------------------------------------
# Example 7 – Exception chaining
# ---------------------------------------------------------------------------
def example7_exception_chaining():
    print("\n=== Example 7: Exception Chaining ===")

    import traceback

    def load_config(raw: str) -> dict:
        try:
            # Simulate JSON parsing failure
            key, value = raw.split("=")
            return {key.strip(): value.strip()}
        except ValueError as e:
            # Chain: the original ValueError is the "cause" of ConfigError
            raise RuntimeError("Failed to parse configuration") from e

    try:
        load_config("broken config line without equals")
    except RuntimeError as e:
        print(f"  Caught: {e}")
        print(f"  Caused by: {e.__cause__}")

    # Suppress chaining context with 'from None'
    def silent_chain():
        try:
            int("not a number")
        except ValueError:
            raise RuntimeError("Internal error") from None  # context hidden

    try:
        silent_chain()
    except RuntimeError as e:
        print(f"  Suppressed chain: __cause__={e.__cause__}, __context__={e.__context__}")


# ---------------------------------------------------------------------------
# Example 8 – assert statement
# ---------------------------------------------------------------------------
def example8_assert():
    print("\n=== Example 8: assert Statement ===")

    def binary_search(lst: list, target) -> int:
        """Returns index of target in sorted lst, or -1 if not found."""
        assert all(lst[i] <= lst[i+1] for i in range(len(lst)-1)), \
            "Input list must be sorted"
        low, high = 0, len(lst) - 1
        while low <= high:
            mid = (low + high) // 2
            if lst[mid] == target:
                return mid
            elif lst[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    sorted_list = [2, 5, 8, 12, 16, 23, 38, 56]
    print(f"  Index of 23: {binary_search(sorted_list, 23)}")  # 5
    print(f"  Index of  7: {binary_search(sorted_list, 7)}")   # -1

    try:
        binary_search([3, 1, 2], 2)     # unsorted – assertion fires
    except AssertionError as e:
        print(f"  AssertionError: {e}")


# ---------------------------------------------------------------------------
# Example 9 – Exception hierarchy exploration
# ---------------------------------------------------------------------------
def example9_hierarchy():
    print("\n=== Example 9: Exception Hierarchy ===")

    exceptions = [
        ValueError("bad value"),
        TypeError("wrong type"),
        KeyError("missing key"),
        IndexError("out of range"),
        ZeroDivisionError("div by 0"),
        FileNotFoundError("no such file"),
    ]

    for exc in exceptions:
        # Show the inheritance chain
        chain = [cls.__name__ for cls in type(exc).__mro__ if cls is not object]
        print(f"  {type(exc).__name__:25s} → {' → '.join(chain)}")

    print()
    # LookupError is the parent of KeyError and IndexError
    ke = KeyError("x")
    ie = IndexError(5)
    print(f"  KeyError   is LookupError: {isinstance(ke, LookupError)}")   # True
    print(f"  IndexError is LookupError: {isinstance(ie, LookupError)}")   # True


# ---------------------------------------------------------------------------
# Example 10 – Context manager for resource cleanup
# ---------------------------------------------------------------------------
def example10_context_manager():
    print("\n=== Example 10: Context Manager for Cleanup ===")
    from contextlib import contextmanager

    class DatabaseConnection:
        """Simulated database connection."""
        def __init__(self, url: str):
            self.url    = url
            self.closed = False

        def query(self, sql: str) -> list:
            if self.closed:
                raise RuntimeError("Connection already closed")
            print(f"    Executing: {sql}")
            return [{"id": 1}, {"id": 2}]

        def close(self):
            self.closed = True
            print(f"    Connection to {self.url} closed")

        def __enter__(self):
            print(f"    Opened connection to {self.url}")
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.close()
            if exc_type is not None:
                print(f"    Exception during transaction: {exc_val}")
            return False   # do not suppress exceptions

    # Normal usage
    print("  Normal transaction:")
    with DatabaseConnection("db://localhost/app") as db:
        rows = db.query("SELECT * FROM users")
        print(f"    Got {len(rows)} rows")
    print(f"  Connection closed after with block: {db.closed}")

    # Exception inside with block
    print("\n  Failing transaction:")
    try:
        with DatabaseConnection("db://localhost/app") as db:
            db.query("SELECT * FROM logs")
            raise RuntimeError("Simulated query failure")
    except RuntimeError:
        print(f"  Exception propagated; connection still closed: {db.closed}")

    # Generator-based context manager
    @contextmanager
    def timer_context(label: str):
        import time
        start = time.perf_counter()
        try:
            yield
        finally:
            elapsed = time.perf_counter() - start
            print(f"    [{label}] elapsed: {elapsed:.4f}s")

    print("\n  Generator-based context manager:")
    with timer_context("loop"):
        total = sum(range(500_000))
    print(f"  Sum = {total}")


# ---------------------------------------------------------------------------
# Run all examples
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    example1_basic_try_except()
    example2_multiple_except()
    example3_else_finally()
    example4_exception_info()
    example5_raising()
    example6_custom_exception()
    example7_exception_chaining()
    example8_assert()
    example9_hierarchy()
    example10_context_manager()
