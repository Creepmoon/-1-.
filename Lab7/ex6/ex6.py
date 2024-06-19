import bisect
from memory_profiler import memory_usage
from datetime import datetime
import time



def find_lis_length_and_sequence(sequence):
    if not sequence:
        return 0, []

    n = len(sequence)
    dp = []
    parent = [-1] * n
    lis_end_at = [-1] * n

    for i in range(n):
        pos = bisect.bisect_left(dp, sequence[i])
        if pos < len(dp):
            dp[pos] = sequence[i]
        else:
            dp.append(sequence[i])

        if pos > 0:
            parent[i] = lis_end_at[pos - 1]
        lis_end_at[pos] = i

    # Reconstruct the LIS
    lis_length = len(dp)
    lis = []
    k = lis_end_at[lis_length - 1]
    while k >= 0:
        lis.append(sequence[k])
        k = parent[k]
    lis.reverse()

    return lis_length, lis


def main():
    Start_time = datetime.now()
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        sequence = list(map(int, f.readline().strip().split()))

    lis_length, lis = find_lis_length_and_sequence(sequence)

    with open('output.txt', 'w') as f:
        f.write(f"{lis_length}\n")
        f.write(" ".join(map(str, lis)) + "\n")
    print(datetime.now() - Start_time)
    print(memory_usage())

if __name__ == "__main__":
    main()
