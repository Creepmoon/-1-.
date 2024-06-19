from memory_profiler import memory_usage
from datetime import datetime
import time


def lcs(a: list, b: list, c: list) -> int:
    matrix: list = [[[0 for _ in range(len(c) + 1)] for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for a_index, a_el in enumerate(a):
        for b_index, b_el in enumerate(b):
            for c_index, c_el in enumerate(c):
                if a_el == b_el == c_el:
                    matrix[a_index + 1][b_index + 1][c_index + 1] = matrix[a_index][b_index][c_index] + 1
                else:
                    matrix[a_index + 1][b_index + 1][c_index + 1] = max(matrix[a_index + 1][b_index][c_index],
                                                                        matrix[a_index][b_index + 1][c_index],
                                                                        matrix[a_index][b_index][c_index + 1],
                                                                        matrix[a_index + 1][b_index + 1][c_index],
                                                                        matrix[a_index + 1][b_index][c_index + 1],
                                                                        matrix[a_index][b_index + 1][c_index + 1])
    return matrix[-1][-1][-1]



Start_time = datetime.now()
input_arrays: list[list[int]] = [[], [], []]
with open("input.txt") as input_file:
    for i in range(3):
        input_file.readline()
        input_arrays[i] = list(map(int, input_file.readline().split(" ")))
with open("output.txt", "w") as output:
    print(lcs(input_arrays[0], input_arrays[1], input_arrays[2]), file=output)
print(datetime.now() - Start_time)
print(memory_usage())