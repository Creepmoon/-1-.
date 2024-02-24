from memory_profiler import memory_usage
from datetime import datetime
import time
def Solution(Array):
    length = len(Array)
    for i in range(1, length):
        element = Array[i]
        x = i
        while x > 0 and Array[x - 1] > element:
            Array[x] = Array[x - 1]
            x -= 1
        Array[x] = element
    return Array

Start_time = datetime.now()
InputFile = open("input.txt", "r")
length = int(InputFile.readline())
String = InputFile.readline().split(" ")
InputFile.close()
array = [0] * length
for i in range(0, length):
    array[i] = int(String[i])

array = Solution(array)
OutputFile = open("output.txt", "w")
OutputFile.write(str(array).replace(",","")[1:-1])
OutputFile.close()
print(datetime.now() - Start_time)
print(memory_usage())