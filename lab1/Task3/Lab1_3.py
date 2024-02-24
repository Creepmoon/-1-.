from memory_profiler import memory_usage
from datetime import datetime
import time
def swap(Array,FirstIndex,SecondIndex):
    Array[FirstIndex], Array[SecondIndex] = Array[SecondIndex], Array[FirstIndex]

def Solution(Array):
    length = len(Array)
    for i in range(1, length):
        x = i
        while x > 0 and Array[x - 1] < Array[x]:
            swap(Array, x, x-1)
            x -= 1
Start_time = datetime.now()
InputFile = open("input.txt", "r")
Array = [0] * int(InputFile.readline())
String = InputFile.readline().split(" ")
InputFile.close()
for i in range(0,len(Array)):
    Array[i] = int(String[i])
Solution(Array)
OutputFile = open("output.txt", "w")
OutputFile.write(str(Array).replace(",","")[1:-1])
OutputFile.close()

print(datetime.now() - Start_time)
print(memory_usage())