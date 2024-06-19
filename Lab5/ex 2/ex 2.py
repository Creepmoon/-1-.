from memory_profiler import memory_usage
from datetime import datetime
import time


def main():
    Start_time = datetime.now()
    with open("input.txt") as f:
        n = int(f.readline())
        nums = list(map(int, f.readline().split()))
    x = max(nums)
    k = 1
    while x != -1:
        x = nums[x]
        k += 1
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(str(k))
    print(datetime.now() - Start_time)
    print(memory_usage())


main()
