"""
Topic 14: Concurrency and Parallelism - Practice Problems
Each problem includes the problem statement as a comment followed by the solution.
"""

import threading
import multiprocessing
import asyncio
import time
import queue
import concurrent.futures

# ─────────────────────────────────────────────
# PROBLEM 1: Create a thread that prints numbers 1-10 with a small delay
# ─────────────────────────────────────────────
# Write a function `count_up` that prints numbers 1-10, sleeping 0.05s between
# each print. Run it in a daemon thread and wait for it to finish.

def count_up():
    for i in range(1, 11):
        print(f"  count_up: {i}")
        time.sleep(0.05)

t = threading.Thread(target=count_up, daemon=True)
t.start()
t.join()
print("Problem 1 done.\n")


# ─────────────────────────────────────────────
# PROBLEM 2: Simulate downloading multiple URLs concurrently with ThreadPoolExecutor
# ─────────────────────────────────────────────
# Given a list of URLs (strings), simulate a download (sleep 0.1s) and return
# the url with "downloaded" appended. Use ThreadPoolExecutor with max_workers=4.

def simulate_download(url):
    time.sleep(0.1)
    return f"{url} - downloaded"

urls = [f"http://example.com/page{i}" for i in range(6)]

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(simulate_download, url): url for url in urls}
    for future in concurrent.futures.as_completed(futures):
        print(f"  {future.result()}")

print("Problem 2 done.\n")


# ─────────────────────────────────────────────
# PROBLEM 3: Thread-safe counter using Lock
# ─────────────────────────────────────────────
# Implement a ThreadSafeCounter class with increment() and value property,
# protected by a Lock. Spawn 10 threads each incrementing 100 times.

class ThreadSafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self._count += 1

    @property
    def value(self):
        return self._count

counter = ThreadSafeCounter()

def bump(c, times):
    for _ in range(times):
        c.increment()

threads = [threading.Thread(target=bump, args=(counter, 100)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"  Counter (expected 1000): {counter.value}")
print("Problem 3 done.\n")


# ─────────────────────────────────────────────
# PROBLEM 4: Producer-consumer pattern with queue.Queue
# ─────────────────────────────────────────────
# Create a producer that puts 5 items into a queue and a consumer that
# processes them. Use queue.Queue for thread-safe communication.

def producer(q):
    for i in range(5):
        item = f"item-{i}"
        q.put(item)
        print(f"  Produced: {item}")
        time.sleep(0.02)
    q.put(None)  # sentinel to stop consumer

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"  Consumed: {item}")
        q.task_done()

q = queue.Queue()
p_thread = threading.Thread(target=producer, args=(q,))
c_thread = threading.Thread(target=consumer, args=(q,))
p_thread.start()
c_thread.start()
p_thread.join()
c_thread.join()
print("Problem 4 done.\n")


# ─────────────────────────────────────────────
# PROBLEM 5: Use multiprocessing.Pool to compute squares in parallel
# ─────────────────────────────────────────────
# Use a Pool of 4 processes to compute the square of numbers 1-10.

def square(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(1, 11))
    print(f"  Squares 1-10: {results}")
    print("Problem 5 done.\n")


# ─────────────────────────────────────────────
# PROBLEM 6: Simple async fetch simulation with asyncio
# ─────────────────────────────────────────────
# Write an async function `async_fetch(url)` that simulates a network request
# (asyncio.sleep 0.1s) and returns "response from <url>".
# Fetch 3 URLs concurrently using asyncio.gather.

async def async_fetch(url):
    await asyncio.sleep(0.1)
    return f"response from {url}"

async def fetch_all():
    responses = await asyncio.gather(
        async_fetch("http://api.example.com/a"),
        async_fetch("http://api.example.com/b"),
        async_fetch("http://api.example.com/c"),
    )
    for r in responses:
        print(f"  {r}")

asyncio.run(fetch_all())
print("Problem 6 done.\n")


# ─────────────────────────────────────────────
# PROBLEM 7: Async task with timeout using asyncio.wait_for
# ─────────────────────────────────────────────
# Write a slow coroutine that sleeps 2 seconds. Use asyncio.wait_for with a
# 0.5s timeout and handle asyncio.TimeoutError gracefully.

async def slow_operation():
    await asyncio.sleep(2)
    return "finished"

async def run_with_timeout():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.5)
        print(f"  Result: {result}")
    except asyncio.TimeoutError:
        print("  Task timed out as expected!")

asyncio.run(run_with_timeout())
print("Problem 7 done.\n")


# ─────────────────────────────────────────────
# PROBLEM 8: Compare threading vs multiprocessing for CPU-bound vs I/O-bound
# ─────────────────────────────────────────────
# Time a CPU-bound task (sum of large range) using threads vs processes.
# Time an I/O-bound task (sleep) using threads vs processes.
# Observe which is faster for each type.

def cpu_task(_):
    return sum(range(500_000))

def io_task(_):
    time.sleep(0.05)
    return "done"

tasks = list(range(4))

# CPU-bound with threads
start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    list(ex.map(cpu_task, tasks))
thread_cpu = time.time() - start

# I/O-bound with threads
start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    list(ex.map(io_task, tasks))
thread_io = time.time() - start

print(f"  CPU-bound with threads:  {thread_cpu:.3f}s")
print(f"  I/O-bound with threads:  {thread_io:.3f}s")
print("  (For CPU-bound, multiprocessing avoids the GIL and is typically faster)")
print("Problem 8 done.\n")
