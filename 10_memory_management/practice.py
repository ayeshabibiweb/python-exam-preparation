"""
10 – Memory Management: Practice Problems
==========================================
Each problem is stated as a comment block, followed by the full solution.
Run this file directly:  python practice.py
"""

import copy
import sys

# ===========================================================================
# Problem 1 – Predict the output (memory puzzle)
# ===========================================================================
# Without running the code, predict what each print statement outputs.
# Then run the file to verify.
# ===========================================================================

def problem1_predict_output():
    print("=== Problem 1: Predict the Output ===")

    # Puzzle A
    x = [1, 2, 3]
    y = x
    y += [4]        # list += is in-place (__iadd__)
    print("A:", x)  # Expected: [1, 2, 3, 4]  – x sees the change (same object)

    # Puzzle B
    a = (1, 2, 3)
    b = a
    b += (4,)       # tuple += creates a NEW tuple (immutable)
    print("B:", a, "|", b)  # Expected: (1,2,3) | (1,2,3,4)  – a unchanged

    # Puzzle C
    nums = [0] * 5
    nums[2] = 99
    print("C:", nums)  # [0, 0, 99, 0, 0]

    # Puzzle D – the aliasing trap
    grid = [[0] * 2] * 3
    grid[0][0] = 7
    print("D:", grid)  # [[7,0],[7,0],[7,0]]  – all rows share one list


# ===========================================================================
# Problem 2 – Fix the aliasing bug
# ===========================================================================
# The function below is supposed to return an n×n identity matrix (1s on
# diagonal, 0s elsewhere). Fix the aliasing bug.
# ===========================================================================

def make_identity_broken(n: int):
    """BROKEN – all rows are the same object."""
    row   = [0] * n
    matrix = [row] * n        # aliasing bug!
    for i in range(n):
        matrix[i][i] = 1      # modifies ALL rows simultaneously
    return matrix


def make_identity_fixed(n: int):
    """FIXED – each row is an independent list."""
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix


def problem2_fix_aliasing():
    print("\n=== Problem 2: Fix Aliasing Bug ===")
    print("Broken:", make_identity_broken(3))  # wrong
    print("Fixed: ", make_identity_fixed(3))   # [[1,0,0],[0,1,0],[0,0,1]]


# ===========================================================================
# Problem 3 – is vs == scenarios
# ===========================================================================
# For each pair, predict whether 'is' and '==' return True or False.
# ===========================================================================

def problem3_is_vs_eq():
    print("\n=== Problem 3: is vs == ===")

    cases = [
        ("None singleton",   None,       None),
        ("Empty list",        [],         []),
        ("Small int cache",   256,        256),
        ("Large int",         1000,       1000),
        ("Same list alias",   (lambda: (lambda lst: (lst, lst))([1, 2]))()[0],
                              (lambda: (lambda lst: (lst, lst))([1, 2]))()[0]),
    ]

    # Simpler, direct cases:
    a = None;    b = None
    print(f"None is None: {a is b}, None == None: {a == b}")   # True True

    a = [];      b = []
    print(f"[] is []:    {a is b}, [] == []:    {a == b}")     # False True

    a = 256;     b = 256
    print(f"256 is 256:  {a is b}, 256 == 256:  {a == b}")     # True  True

    # Large int - behaviour depends on CPython context
    exec("a = 1000; b = 1000; print(f'1000 is 1000 (exec): {a is b}')")

    lst = [1, 2]
    alias = lst
    print(f"alias is lst: {alias is lst}, alias == lst: {alias == lst}")  # True True


# ===========================================================================
# Problem 4 – Shallow vs deep copy
# ===========================================================================
# Write a function that safely duplicates the structure below,
# so that modifications to the copy do not affect the original.
#
# structure = {
#     "scores": [90, 85, 92],
#     "info":   {"name": "Alice", "tags": ["python", "oop"]},
# }
# ===========================================================================

def problem4_deep_copy():
    print("\n=== Problem 4: Shallow vs Deep Copy ===")

    structure = {
        "scores": [90, 85, 92],
        "info":   {"name": "Alice", "tags": ["python", "oop"]},
    }

    # Shallow copy – nested objects still shared
    shallow = copy.copy(structure)
    shallow["scores"].append(77)
    print(f"After shallow append: original scores = {structure['scores']}")
    # [90, 85, 92, 77] – CHANGED! Shallow copy wasn't enough.

    # Reset
    structure = {
        "scores": [90, 85, 92],
        "info":   {"name": "Alice", "tags": ["python", "oop"]},
    }

    # Deep copy – fully independent
    deep = copy.deepcopy(structure)
    deep["scores"].append(77)
    deep["info"]["tags"].append("mutable")
    print(f"After deep changes: original scores = {structure['scores']}")  # unchanged
    print(f"After deep changes: original tags   = {structure['info']['tags']}")  # unchanged
    print(f"Deep copy scores: {deep['scores']}")   # [90, 85, 92, 77]


# ===========================================================================
# Problem 5 – Reference count tracking
# ===========================================================================
# Without running the code, trace the reference count of the list object
# through each step. Then verify with sys.getrefcount.
# ===========================================================================

def problem5_refcount_trace():
    print("\n=== Problem 5: Reference Count Trace ===")

    obj = []
    # sys.getrefcount adds 1 temporary reference during the call
    print(f"Step 1 – just obj:         refcount = {sys.getrefcount(obj)}")  # 2

    ref1 = obj
    print(f"Step 2 – obj + ref1:       refcount = {sys.getrefcount(obj)}")  # 3

    lst = [obj, obj]    # two references inside lst
    print(f"Step 3 – obj, ref1, lst×2: refcount = {sys.getrefcount(obj)}")  # 5

    del ref1
    print(f"Step 4 – after del ref1:   refcount = {sys.getrefcount(obj)}")  # 4

    lst.clear()         # removes both references inside lst
    print(f"Step 5 – after lst.clear: refcount = {sys.getrefcount(obj)}")   # 2

    del lst
    print(f"Step 6 – after del lst:   refcount = {sys.getrefcount(obj)}")   # 2 (only obj + call)


# ===========================================================================
# Problem 6 – Implement a simple copy function
# ===========================================================================
# Without using the copy module, implement:
#   my_shallow_copy(obj) for lists of lists (one level of nesting)
#   my_deep_copy(obj)    for lists of lists (one level of nesting)
# ===========================================================================

def my_shallow_copy(lst: list) -> list:
    """Return a new outer list; inner lists are shared references."""
    return list(lst)   # same as lst[:]


def my_deep_copy(lst: list) -> list:
    """Return a new outer list with new inner lists (one level of nesting)."""
    return [list(inner) if isinstance(inner, list) else inner for inner in lst]


def problem6_custom_copy():
    print("\n=== Problem 6: Custom Copy Functions ===")
    original = [[1, 2], [3, 4]]

    shallow = my_shallow_copy(original)
    original[0].append(99)
    print(f"Shallow – original[0]: {original[0]}, copy[0]: {shallow[0]}")
    # Both changed: [1, 2, 99]

    # Reset
    original = [[1, 2], [3, 4]]
    deep = my_deep_copy(original)
    original[0].append(99)
    print(f"Deep    – original[0]: {original[0]}, copy[0]: {deep[0]}")
    # Only original changed: [1, 2, 99] vs [1, 2]


# ===========================================================================
# Problem 7 – Memory-efficient class with __slots__
# ===========================================================================
# Create a Point3D class (x, y, z) using __slots__.
# Compare its size to a version without __slots__.
# ===========================================================================

class Point3D:
    __slots__ = ("x", "y", "z")

    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z


class Point3DRegular:
    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z


def problem7_slots():
    print("\n=== Problem 7: __slots__ Memory Comparison ===")
    p_slots   = Point3D(1.0, 2.0, 3.0)
    p_regular = Point3DRegular(1.0, 2.0, 3.0)

    size_slots   = sys.getsizeof(p_slots)
    size_regular = sys.getsizeof(p_regular)

    print(f"With __slots__:    {size_slots} bytes")
    print(f"Without __slots__: {size_regular} bytes")
    print(f"Saved: ~{size_regular - size_slots} bytes per object")

    # __dict__ is not available on slotted objects
    print(f"Has __dict__: {hasattr(p_regular, '__dict__')}")  # True
    print(f"Has __slots__: {hasattr(p_slots, '__slots__')}")  # True
    try:
        _ = p_slots.__dict__
    except AttributeError as e:
        print(f"__dict__ on slotted: {e}")


# ===========================================================================
# Problem 8 – Detect and break a circular reference
# ===========================================================================
# Create two objects that reference each other, then break the cycle
# by setting one reference to None.  Verify with gc.
# ===========================================================================

def problem8_break_cycle():
    print("\n=== Problem 8: Break Circular Reference ===")
    import gc

    class Container:
        def __init__(self, name: str):
            self.name = name
            self.other = None

    gc.collect()   # clear any existing garbage first
    count_before = len(gc.get_objects())

    a = Container("A")
    b = Container("B")
    a.other = b
    b.other = a   # cycle: a → b → a

    # Break the cycle explicitly (best practice for long-lived objects)
    a.other = None   # removes one link; b's refcount can now drop to 0

    del a, b
    freed = gc.collect()
    print(f"Objects freed by gc.collect(): {freed}")
    # Should be 0 because we broke the cycle before deleting


# ===========================================================================
# Problem 9 – Generator vs list memory usage
# ===========================================================================
# Compare the memory footprint of a list comprehension vs a generator
# expression for 1,000,000 elements.
# ===========================================================================

def problem9_generator_memory():
    print("\n=== Problem 9: Generator vs List Memory ===")

    N = 1_000_000

    # List comprehension – stores all N values in memory
    lst = [x * 2 for x in range(N)]
    size_list = sys.getsizeof(lst)

    # Generator – lazy; only the generator object is stored
    gen = (x * 2 for x in range(N))
    size_gen = sys.getsizeof(gen)

    print(f"List of {N} ints:  {size_list:,} bytes (~{size_list // 1024} KB)")
    print(f"Generator object:   {size_gen:,} bytes")
    print(f"Memory ratio: {size_list // size_gen}x larger for list")

    # Demonstrate that the generator produces the same values
    first_five_list = lst[:5]
    first_five_gen  = [next(gen) for _ in range(5)]
    print(f"First 5 list: {first_five_list}")
    print(f"First 5 gen:  {first_five_gen}")


# ===========================================================================
# Run all problems
# ===========================================================================
if __name__ == "__main__":
    problem1_predict_output()
    problem2_fix_aliasing()
    problem3_is_vs_eq()
    problem4_deep_copy()
    problem5_refcount_trace()
    problem6_custom_copy()
    problem7_slots()
    problem8_break_cycle()
    problem9_generator_memory()
