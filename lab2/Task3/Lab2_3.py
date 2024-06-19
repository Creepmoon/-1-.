import os
import psutil
from datetime import datetime


def merge(leftArray, rightArray):
    answer = []
    global inv
    l = 0
    r = 0
    while l < len(leftArray) and r < len(rightArray):
        if leftArray[l] < rightArray[r]:
            answer.append(leftArray[l])
            l += 1
            inv += l

        else:
            answer.append(rightArray[r])
            r += 1

    if l < len(leftArray):
        answer += leftArray[l:]
    if r < len(rightArray):
        answer += rightArray[r:]
    return answer


def merge_sort(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))


process = psutil.Process(os.getpid())
startTime = datetime.now()

InputFile = open('input.txt')
length = int(InputFile.readline())
string = InputFile.readline().split()
InputFile.close()
array = []
for i in string:
    array.append(int(i))

OutputFile = open('output.txt', 'w')
inv = 0
merge_sort(array)
OutputFile.write(str(inv))
OutputFile.close()

print(datetime.now() - startTime, process.memory_info().rss / (1024 * 1024))
