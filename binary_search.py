import sys
import time

size = int(sys.argv[1])
number = int(sys.argv[2])

print(f"Allocating array of size {size:,}...")
array = [i for i in range(size)]

REPETITIONS = 100000

print(f"Running binary search {REPETITIONS:,} times for target {number:,}")

start_time = time.perf_counter_ns()

for _ in range(REPETITIONS):
    low = 0
    high = size - 1
    
    while low <= high:
        mid = (low + high) // 2
        value = array[mid]
        if number == value:
            break
        elif number > value:
            low = mid + 1
        else:
            high = mid - 1

end_time = time.perf_counter_ns()

total_ns = end_time - start_time
avg_ns = total_ns/REPETITIONS
avg_us = avg_ns/1000

print("---Results---")
print(f"Total time for {REPETITIONS:,} searches: {total_ns / 1e9:.4f} seconds")
print(f"Average time per search: {avg_ns:.2f} ns ({avg_us:.3f} µs)")