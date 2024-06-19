from memory_profiler import memory_usage
from datetime import datetime
import time

class Heap:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.array = array
        self.length = len(array)
        self.heapify_full()

    def add(self, value):
        self.array.append(value)
        self.length += 1
        if self.length > 1:
            self.heapify_full()

    def pop_minimal(self):
        if self.length > 0:
            value = self.array.pop(0)
            self.length -= 1
            self.heapify_full()
            return value
        return None

    def heapify(self, arr, n, i):
        left_ch = i * 2 + 1
        right_ch = i * 2 + 2
        smallest = i
        if left_ch < n and arr[smallest] > arr[left_ch]:
            smallest = left_ch
        if right_ch < n and arr[smallest] > arr[right_ch]:
            smallest = right_ch
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)

    def heapify_full(self):
        for i in range(self.length - 1, -1, -1):
            self.heapify(self.array, self.length, i)

    def heap_sort(self):
        arr = self.array[:]
        for i in range(self.length - 1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i])
            self.heapify(arr, i, 0)
        return arr

    def change(self, value_to_change, value_to_change_to):
        if value_to_change in self.array:
            to_change = self.array.index(value_to_change)
            self.array[to_change] = value_to_change_to
            self.heapify_full()


def main():
    Start_time = datetime.now()
    with open("input.txt") as f:
        _ = f.readline()
        nums = list(map(int, f.readline().split()))
    heap = Heap(nums)
    sorted_nums = heap.heap_sort()

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, sorted_nums)))
    print(datetime.now() - Start_time)
    print(memory_usage())

main()
