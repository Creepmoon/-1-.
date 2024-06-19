import os
import psutil
from datetime import datetime


def Solution(array, value, start, stop):
    if start > stop:
        return -1
    else:
        mid = (start + stop) // 2
        if value == array[mid]:
            return mid
        elif value < array[mid]:
            return Solution(array, value, start, mid - 1)
        else:
            return Solution(array, value, mid + 1, stop)


process = psutil.Process(os.getpid())
startTime = datetime.now()

InputFile = open('input.txt')
lengthA = InputFile.readline()
arrayA = sorted([int(x) for x in InputFile.readline().split()])
lengthB = InputFile.readline()
arrayB = [int(x) for x in InputFile.readline().split()]


Outputfile = open('output.txt', 'w')
answer = ''
for i in range(len(arrayB)):
    x = Solution(arrayA, arrayB[i], 0, len(arrayA) - 1) #индекс каждого вместо чисел
    arrayB[i] = x

for i in arrayB:
    answer += str(i) + ' '
Outputfile.write(f'{answer}')

print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))