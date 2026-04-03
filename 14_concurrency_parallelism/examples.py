"""
Topic 14: Concurrency and Parallelism - Examples
Python 3.8+ compatible, runnable examples
"""

import threading
import multiprocessing
import asyncio
import time
import concurrent.futures
import queue

print("=" * 60)
print("EXAMPLE 1: Basic Thread Creation")
print("=" * 60)

def greet(name):
    print(f"  Hello from thread, {name}!")

t = threading.Thread(target=greet, args=("Alice",))
t.start()
t.join()
print("Thread finished.\n")


print("=" * 60)
print("EXAMPLE 2: Multiple Threads Running Concurrently")
print("=" * 60)

def worker(worker_id, duration):
    time.sleep(duration)
    print(f"  Worker {worker_id} done after {duration}s")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i, 0.1 * (i + 1)))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("All workers finished.\n")


print("=" * 60)
print("EXAMPLE 3: Thread with Arguments")
print("=" * 60)

def multiply(x, y):
    result = x * y
    print(f"  {x} * {y} = {result}")

t = threading.Thread(target=multiply, args=(6, 7))
t.start()
t.join()
print()


print("=" * 60)
print("EXAMPLE 4: Thread Synchronization with Lock")
print("=" * 60)

counter = 0
lock = threading.Lock()

def increment(n):
    global counter
    for _ in range(n):
        with lock:          # acquire lock, then release automatically
            counter += 1

threads = [threading.Thread(target=increment, args=(1000,)) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"  Final counter (expected 5000): {counter}\n")


print("=" * 60)
print("EXAMPLE 5: ThreadPoolExecutor")
print("=" * 60)

def fetch_data(url):
    time.sleep(0.05)  # simulate network delay
    return f"data from {url}"

urls = ["http://example.com/a", "http://example.com/b", "http://example.com/c"]

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_data, urls))

for r in results:
    print(f"  {r}")
print()


print("=" * 60)
print("EXAMPLE 6: Basic multiprocessing.Process")
print("=" * 60)

def compute_square(n):
    print(f"  Square of {n} = {n * n}")

if __name__ == "__main__":
    p = multiprocessing.Process(target=compute_square, args=(7,))
    p.start()
    p.join()
    print()


print("=" * 60)
print("EXAMPLE 7: multiprocessing.Pool with map")
print("=" * 60)

def square(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(1, 6))
    print(f"  Squares: {results}\n")


print("=" * 60)
print("EXAMPLE 8: Simple async Function with asyncio")
print("=" * 60)

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"  Hello, {name}!")

asyncio.run(say_hello("World", 0.1))
print()


print("=" * 60)
print("EXAMPLE 9: asyncio.gather() for Concurrent Coroutines")
print("=" * 60)

async def task(name, seconds):
    await asyncio.sleep(seconds)
    return f"{name} completed"

async def main():
    results = await asyncio.gather(
        task("Task-A", 0.1),
        task("Task-B", 0.05),
        task("Task-C", 0.15),
    )
    for r in results:
        print(f"  {r}")

asyncio.run(main())
print()


print("=" * 60)
print("EXAMPLE 10: Sequential vs Concurrent Timing")
print("=" * 60)

def slow_task(n):
    time.sleep(0.1)
    return n * n

# Sequential
start = time.time()
seq_results = [slow_task(i) for i in range(5)]
seq_time = time.time() - start
print(f"  Sequential time: {seq_time:.2f}s")

# Concurrent with ThreadPoolExecutor
start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    con_results = list(executor.map(slow_task, range(5)))
con_time = time.time() - start
print(f"  Concurrent time: {con_time:.2f}s")
print(f"  Speedup: ~{seq_time / con_time:.1f}x faster")
