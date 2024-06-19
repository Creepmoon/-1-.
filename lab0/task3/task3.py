import time
from memory_profiler import memory_usage

t_start = time.perf_counter();

def last_digit_fibonacci(n):
    if n <= 1:
        return n
    pisano_period = 60
    n %= pisano_period

    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current


with open('input.txt', 'r') as file:
    n = int(file.read().strip())
with open('output.txt', 'w') as file:
    file.write(str(last_digit_fibonacci(n)))
print(time.perf_counter() - t_start)
print(memory_usage())