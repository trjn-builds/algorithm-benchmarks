import sys
import time

size = int(sys.argv[1])
number = int(sys.argv[2])

print(f"Allocating array of size {size:,}...")
array = [i for i in range(size)]

REPETITIONS = 1000

print(f"Running simple search {REPETITIONS:,} times for target {number:,}")

start_time = time.perf_counter_ns()

for _ in range(REPETITIONS):
    for i in range(size):
        if array[i] == number:
            break

end_time = time.perf_counter_ns()

total_ns = end_time - start_time
avg_ns = total_ns/REPETITIONS
avg_us = avg_ns/1000

print("---Results---")
print(f"Total time for {REPETITIONS:,} searches: {total_ns / 1e9:.4f} seconds")
print(f"Average time per search: {avg_ns:.2f} ns ({avg_us:.3f} µs)")