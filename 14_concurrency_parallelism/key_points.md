# Topic 14: Concurrency & Parallelism — Key Points

## Quick Decision Guide

| Scenario | Best Tool |
|---|---|
| I/O-bound (network, disk) | `threading` or `asyncio` |
| CPU-bound (heavy computation) | `multiprocessing` |
| Many concurrent I/O tasks | `asyncio` |
| Simple parallel execution | `concurrent.futures` |

---

## The GIL (Global Interpreter Lock)
- CPython has a GIL: only **one thread** executes Python bytecode at a time.
- Threads are still useful for **I/O-bound** tasks (GIL is released during I/O waits).
- Use **multiprocessing** to bypass the GIL for **CPU-bound** tasks.

---

## threading Cheat Sheet

```python
import threading

# Create & start
t = threading.Thread(target=func, args=(arg1, arg2))
t.start()
t.join()          # wait for thread to finish

# Lock (prevents race conditions)
lock = threading.Lock()
with lock:
    shared_resource += 1

# Common attributes
t.daemon = True   # thread dies when main program exits
t.is_alive()      # check if running
```

---

## concurrent.futures Cheat Sheet

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(func, iterable))   # ordered results

    # Submit individual tasks
    future = executor.submit(func, arg1, arg2)
    result = future.result()                        # blocks until done

# Use as_completed for non-blocking iteration
from concurrent.futures import as_completed
for future in as_completed(futures):
    print(future.result())
```

---

## multiprocessing Cheat Sheet

```python
import multiprocessing

# Single process
p = multiprocessing.Process(target=func, args=(x,))
p.start()
p.join()

# Pool (parallel map)
with multiprocessing.Pool(processes=4) as pool:
    results = pool.map(func, iterable)

# Shared state
manager = multiprocessing.Manager()
shared_list = manager.list()
```

---

## asyncio Cheat Sheet

```python
import asyncio

async def my_coroutine():
    await asyncio.sleep(1)   # non-blocking sleep
    return "done"

# Run a single coroutine
asyncio.run(my_coroutine())

# Run multiple concurrently
async def main():
    results = await asyncio.gather(coro1(), coro2(), coro3())

asyncio.run(main())

# Timeout
result = await asyncio.wait_for(my_coroutine(), timeout=5.0)

# Create task (schedule without awaiting immediately)
task = asyncio.create_task(my_coroutine())
await task
```

---

## Common Pitfalls
- **Race conditions**: use `Lock` when multiple threads share mutable state.
- **Deadlocks**: avoid acquiring multiple locks in different orders.
- **`if __name__ == "__main__":`** guard is **required** for `multiprocessing` on Windows/macOS.
- Don't mix `asyncio.run()` inside an already-running event loop.
- `ThreadPoolExecutor` won't speed up CPU-bound code due to the GIL.
