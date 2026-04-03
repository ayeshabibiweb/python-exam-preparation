# Topic 14: Concurrency and Parallelism

## Concurrency vs Parallelism

- **Concurrency**: Multiple tasks *in progress* at the same time — they may not run simultaneously (e.g., one CPU switches between tasks).
- **Parallelism**: Multiple tasks *executing* simultaneously — requires multiple CPU cores.

Think of concurrency as juggling (one person, multiple balls in the air) and parallelism as multiple jugglers each with their own ball.

---

## Python's Global Interpreter Lock (GIL)

The **GIL** is a mutex (mutual exclusion lock) in CPython that prevents more than one native thread from executing Python bytecode at a time. Implications:

- **Threading is NOT truly parallel** for CPU-bound tasks in CPython.
- **Threading IS useful** for I/O-bound tasks because the GIL is released during I/O operations (file reads, network requests, sleep).
- **Multiprocessing bypasses the GIL** by creating separate processes with separate interpreters.

---

## The `threading` Module

### Thread Creation

```python
import threading

def task(name):
    print(f"Task {name} running")

t = threading.Thread(target=task, args=("A",))
t.start()    # start the thread
t.join()     # wait for it to finish
```

**Key Thread attributes/methods:**

| Method/Attribute | Purpose |
|---|---|
| `Thread(target, args, kwargs)` | Create a thread |
| `.start()` | Begin execution |
| `.join(timeout=None)` | Wait for thread to finish |
| `.is_alive()` | Check if still running |
| `.daemon = True` | Thread dies with the main program |

### Daemon Threads

A **daemon thread** runs in the background and is automatically killed when the main thread exits. Use for background tasks that shouldn't prevent program exit.

```python
t = threading.Thread(target=background_task)
t.daemon = True
t.start()
# main program exits → daemon thread is killed automatically
```

### Thread Synchronization

Without synchronization, concurrent access to shared data causes **race conditions**.

**`threading.Lock`** — basic mutual exclusion:
```python
lock = threading.Lock()
with lock:         # automatically acquired and released
    shared_data += 1
```

**`threading.RLock`** (re-entrant lock) — same thread can acquire multiple times:
```python
rlock = threading.RLock()
with rlock:
    with rlock:    # works; a regular Lock would deadlock here
        ...
```

**`threading.Semaphore(n)`** — allows up to `n` threads simultaneously:
```python
sem = threading.Semaphore(3)   # max 3 threads at once
with sem:
    access_limited_resource()
```

---

## The `concurrent.futures` Module

`ThreadPoolExecutor` provides a higher-level interface for thread pools:

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(task, arg) for arg in args]
    results = [f.result() for f in futures]

# Or use map (like built-in map but concurrent)
with ThreadPoolExecutor() as executor:
    results = list(executor.map(task, args))
```

---

## The `multiprocessing` Module

### Process Creation

```python
from multiprocessing import Process

def worker(n):
    print(f"Process {n}")

p = Process(target=worker, args=(1,))
p.start()
p.join()
```

### Process Pool

`Pool` manages a pool of worker processes:

```python
from multiprocessing import Pool

def square(x):
    return x ** 2

with Pool(processes=4) as pool:
    results = pool.map(square, range(10))   # distributes work across processes
```

`Pool.map` collects and returns all results in order, blocking until done.

---

## I/O-bound vs CPU-bound Tasks

| Type | Examples | Best Solution |
|---|---|---|
| **I/O-bound** | File I/O, network requests, DB queries, `time.sleep` | `threading` or `asyncio` |
| **CPU-bound** | Math, image processing, encryption, sorting | `multiprocessing` |

---

## `asyncio` — Asynchronous I/O

`asyncio` provides cooperative multitasking using **coroutines** — functions that can pause and resume execution, allowing other coroutines to run while waiting for I/O.

### Core Concepts

- **Coroutine**: An `async def` function. Calling it returns a coroutine object (not the result).
- **`await`**: Suspends the coroutine until the awaited operation completes. Only valid inside `async def`.
- **Event loop**: The engine that runs coroutines, switching between them when one is waiting.
- **Task**: A coroutine scheduled to run on the event loop.

### Basic Syntax

```python
import asyncio

async def greet(name):
    await asyncio.sleep(1)    # non-blocking sleep
    print(f"Hello, {name}!")

asyncio.run(greet("Alice"))   # run from synchronous code (Python 3.7+)
```

### `asyncio.gather()` — Concurrent Coroutines

```python
async def main():
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie"),
    )
    # all three greetings run concurrently

asyncio.run(main())
```

`gather` schedules all coroutines concurrently and waits for all to complete. Total time ≈ max individual time (not sum).

---

## When to Use Each Approach

| Scenario | Recommended Tool |
|---|---|
| Many simultaneous web requests | `asyncio` or `ThreadPoolExecutor` |
| Parallelise CPU-heavy computation | `multiprocessing.Pool` |
| Background I/O with simple threading | `threading.Thread` |
| Mixed I/O with many connections | `asyncio` |
| Simple CPU parallelism | `ProcessPoolExecutor` |

---

## Common Mistakes and Thread Safety

### 1. Shared Mutable State Without Locks
```python
# BUG: race condition
counter = 0
def increment():
    global counter
    counter += 1   # not atomic! read-modify-write

# Fix: use a lock
lock = threading.Lock()
def safe_increment():
    global counter
    with lock:
        counter += 1
```

### 2. Forgetting `.join()`
If you start threads but never join them, the main program may exit before they finish.

### 3. Using `threading` for CPU-bound Work
Due to the GIL, CPU-bound threading is often slower than sequential code. Use `multiprocessing` instead.

### 4. Calling `asyncio.run()` Inside an Event Loop
`asyncio.run()` creates a new event loop. Calling it inside an already-running loop raises `RuntimeError`. Use `await` directly or `asyncio.create_task()`.

### 5. Forgetting `if __name__ == '__main__':` in multiprocessing
On Windows (and with `spawn` start method), multiprocessing code must be guarded to prevent recursive subprocess spawning.

### 6. `await` Outside `async def`
`await` can only be used inside an `async def` function.
