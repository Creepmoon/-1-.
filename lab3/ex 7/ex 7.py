from memory_profiler import memory_usage
from datetime import datetime


def transform_strings(n, m, vertical_strings):
    strings = ['' for _ in range(n)]
    for i in range(n):
        for j in range(m):
            strings[i] += vertical_strings[j][i]
    return strings

def counting_sort_indices(strings, indices, index):
    count = [0] * 26
    output = [0] * len(indices)
    for i in indices:
        count[ord(strings[i][index]) - ord('a')] += 1
    for i in range(1, 26):
        count[i] += count[i - 1]
    for i in reversed(indices):
        char_index = ord(strings[i][index]) - ord('a')
        output[count[char_index] - 1] = i
        count[char_index] -= 1
    return output

def radix_sort_indices(strings, k):
    n = len(strings)
    indices = list(range(n))
    m = len(strings[0])
    for i in range(m - 1, m - k - 1, -1):
        indices = counting_sort_indices(strings, indices, i)
    return indices

def main():
    Start_time = datetime.now()
    with open("input.txt", "r") as file:
        n, m, k = map(int, file.readline().strip().split())
        vertical_strings = [file.readline().strip() for _ in range(m)]
    strings = transform_strings(n, m, vertical_strings)
    sorted_indices = radix_sort_indices(strings, k)
    with open("output.txt", "w") as file:
        file.write(" ".join(map(str, [i + 1 for i in sorted_indices])) )
    print(datetime.now() - Start_time)
    print(memory_usage())

main()

