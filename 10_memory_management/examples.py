"""
10 – Memory Management: Examples
=================================
Run this file directly:  python examples.py
All examples print descriptive output to illustrate memory behaviour.
"""

import sys
import copy


# ---------------------------------------------------------------------------
# Example 1 – id() and object identity
# ---------------------------------------------------------------------------
def example1_id_and_identity():
    print("=== Example 1: id() and Object Identity ===")

    x = [1, 2, 3]
    y = x            # y and x are bound to the SAME object
    z = [1, 2, 3]    # z is a different object with the same value

    print(f"id(x) = {id(x)}")
    print(f"id(y) = {id(y)}")
    print(f"id(z) = {id(z)}")
    print(f"x is y: {x is y}")   # True  – same object
    print(f"x is z: {x is z}")   # False – different objects
    print(f"x == z: {x == z}")   # True  – same value


# ---------------------------------------------------------------------------
# Example 2 – is vs == comparison
# ---------------------------------------------------------------------------
def example2_is_vs_equals():
    print("\n=== Example 2: is vs == ===")

    # Use 'is' correctly: None check
    value = None
    print(f"value is None: {value is None}")    # True  ✓ correct way
    print(f"value == None: {value == None}")    # True  (works, but not idiomatic)

    # Dangerous: 'is' with strings (interning is implementation-defined)
    s1 = "hello"
    s2 = "hello"
    print(f"s1 is s2: {s1 is s2}")   # True for short literals (CPython interns them)
    # But for dynamically built strings, 'is' can be False even if values match:
    s3 = "hel" + "lo"                # same value; may or may not be same object
    print(f"s1 is s3: {s1 is s3}")   # typically True due to interning, but unreliable
    print(f"s1 == s3: {s1 == s3}")   # True  – always correct


# ---------------------------------------------------------------------------
# Example 3 – Mutable vs immutable behaviour
# ---------------------------------------------------------------------------
def example3_mutable_vs_immutable():
    print("\n=== Example 3: Mutable vs Immutable ===")

    # --- Immutable: int ---
    a = 42
    b = a
    print(f"Before: a={a}, b={b}, same object: {a is b}")
    a = 100          # rebinds 'a' to a new int object; 'b' is unaffected
    print(f"After a=100: a={a}, b={b}, same object: {a is b}")

    # --- Mutable: list ---
    lst1 = [1, 2, 3]
    lst2 = lst1
    print(f"\nBefore: lst1={lst1}, lst2={lst2}, same object: {lst1 is lst2}")
    lst1.append(4)   # modifies the shared object in place
    print(f"After lst1.append(4): lst1={lst1}, lst2={lst2}")
    # Both see the change because they reference the same list!


# ---------------------------------------------------------------------------
# Example 4 – Variable rebinding
# ---------------------------------------------------------------------------
def example4_rebinding():
    print("\n=== Example 4: Variable Rebinding ===")

    x = "original"
    print(f"id before: {id(x)}")
    x = "new value"      # x now points to a completely different string object
    print(f"id after:  {id(x)}")
    print(f"Value: {x}") # new value

    # Augmented assignment with immutable vs mutable
    n = 10
    id_before = id(n)
    n += 5               # creates a NEW int object (15), rebinds n
    print(f"\nint: id changed: {id(n) != id_before}")  # True

    lst = [1, 2]
    id_before = id(lst)
    lst += [3]           # calls __iadd__, extends list IN PLACE
    print(f"list: id changed: {id(lst) != id_before}")  # False


# ---------------------------------------------------------------------------
# Example 5 – List aliasing problem
# ---------------------------------------------------------------------------
def example5_list_aliasing():
    print("\n=== Example 5: List Aliasing ===")

    # Classic trap: creating a 2D grid the wrong way
    wrong = [[0] * 3] * 3   # all 3 rows are the SAME list object!
    wrong[0][0] = 99
    print("Wrong grid (all rows share the same object):")
    print(wrong)             # [[99, 0, 0], [99, 0, 0], [99, 0, 0]]

    # Correct way: use a list comprehension to create independent rows
    correct = [[0] * 3 for _ in range(3)]
    correct[0][0] = 99
    print("\nCorrect grid (independent rows):")
    print(correct)           # [[99, 0, 0], [0, 0, 0], [0, 0, 0]]


# ---------------------------------------------------------------------------
# Example 6 – Shallow copy
# ---------------------------------------------------------------------------
def example6_shallow_copy():
    print("\n=== Example 6: Shallow Copy ===")

    original = [[1, 2], [3, 4], [5, 6]]
    # Shallow copy: new outer list, but inner lists are still shared
    shallow  = copy.copy(original)

    print(f"original is shallow: {original is shallow}")   # False
    print(f"original[0] is shallow[0]: {original[0] is shallow[0]}")  # True!

    original.append([7, 8])       # only affects original's outer list
    print(f"After append to original: {len(original)} vs {len(shallow)}")  # 4 vs 3

    original[0].append(99)        # affects BOTH (shared inner list)
    print(f"original[0]: {original[0]}, shallow[0]: {shallow[0]}")  # both [1,2,99]


# ---------------------------------------------------------------------------
# Example 7 – Deep copy
# ---------------------------------------------------------------------------
def example7_deep_copy():
    print("\n=== Example 7: Deep Copy ===")

    original = {"data": [1, 2, 3], "nested": {"key": "value"}}
    deep = copy.deepcopy(original)

    print(f"original is deep: {original is deep}")                        # False
    print(f"original['data'] is deep['data']: {original['data'] is deep['data']}")  # False

    original["data"].append(99)
    original["nested"]["key"] = "changed"
    print(f"original['data']: {original['data']}")   # [1, 2, 3, 99]
    print(f"deep['data']:     {deep['data']}")        # [1, 2, 3]   – independent
    print(f"original nested: {original['nested']}")  # {'key': 'changed'}
    print(f"deep nested:     {deep['nested']}")       # {'key': 'value'}  – independent


# ---------------------------------------------------------------------------
# Example 8 – Reference counting with sys.getrefcount
# ---------------------------------------------------------------------------
def example8_refcount():
    print("\n=== Example 8: Reference Counting ===")

    x = object()
    # sys.getrefcount always adds 1 (the argument reference)
    print(f"Just x:            refcount={sys.getrefcount(x)}")   # 2

    y = x
    print(f"x and y:           refcount={sys.getrefcount(x)}")   # 3

    container = [x, x, x]   # three references inside the list
    print(f"x, y, list(x,x,x): refcount={sys.getrefcount(x)}")  # 6

    del container
    print(f"After del container: refcount={sys.getrefcount(x)}") # 3

    del y
    print(f"After del y:        refcount={sys.getrefcount(x)}")  # 2


# ---------------------------------------------------------------------------
# Example 9 – Small integer caching demo
# ---------------------------------------------------------------------------
def example9_small_int_cache():
    print("\n=== Example 9: Small Integer Caching ===")

    # Integers in [-5, 256] are cached singletons in CPython
    a = 100
    b = 100
    print(f"100 is 100: {a is b}")   # True  (cached)

    c = 300
    d = 300
    print(f"300 is 300: {c is d}")   # False (not cached – two separate objects)
    # Note: this is a CPython implementation detail; never rely on it!

    # The cache also applies to small booleans and None
    print(f"True is True:   {True is True}")     # True
    print(f"None is None:   {None is None}")     # True


# ---------------------------------------------------------------------------
# Example 10 – Circular reference illustration
# ---------------------------------------------------------------------------
def example10_circular_reference():
    print("\n=== Example 10: Circular References ===")
    import gc

    class Node:
        def __init__(self, name: str):
            self.name = name
            self.next = None

        def __repr__(self):
            return f"Node({self.name!r})"

    # Create a cycle: a → b → a
    a = Node("A")
    b = Node("B")
    a.next = b
    b.next = a   # cycle!

    print(f"a.next={a.next}, b.next={b.next}")

    # Even after deleting the names, the cycle keeps refcounts > 0.
    # Python's cyclic garbage collector handles this.
    del a, b     # names gone, but objects may still exist in memory

    # Force the cyclic GC to run
    collected = gc.collect()
    print(f"gc.collect() freed {collected} objects (includes the cycle)")

    # Weak references avoid cycles for caching scenarios
    import weakref

    class Cache:
        pass

    obj = Cache()
    weak = weakref.ref(obj)   # weak reference: does NOT increment refcount
    print(f"Weakly referenced obj alive: {weak() is not None}")  # True
    del obj
    print(f"After del obj, alive:        {weak() is not None}")  # False


# ---------------------------------------------------------------------------
# Run all examples
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    example1_id_and_identity()
    example2_is_vs_equals()
    example3_mutable_vs_immutable()
    example4_rebinding()
    example5_list_aliasing()
    example6_shallow_copy()
    example7_deep_copy()
    example8_refcount()
    example9_small_int_cache()
    example10_circular_reference()
