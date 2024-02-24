import sys
from memory_profiler import memory_usage
from datetime import datetime
import time
def swap(Array, FirstIndex, SecondIndex):
    Array[FirstIndex], Array[SecondIndex] = Array[SecondIndex], Array[FirstIndex]

def Solution(Array, FirstIndex, SecondIndex):
    i = FirstIndex
    while 0 < i < SecondIndex and Array[i - 1] < Array[i]:
        swap(Array, i, i - 1)
        i-= 1
    if FirstIndex < SecondIndex:
        Solution(Array,FirstIndex + 1, SecondIndex)

Start_time = datetime.now()
sys.setrecursionlimit(10**3+2)
InputFile = open("../input.txt", "r")
Array = [0] * int(InputFile.readline())
String = InputFile.readline().split(" ")
InputFile.close()
for i in range(0, len(Array)):
    Array[i] = int(String[i])
Solution(Array, 1, len(Array))
OutputFile = open("../output.txt", "w")
OutputFile.write(str(Array).replace(",","")[1:-1])
OutputFile.close()
print(datetime.now() - Start_time)
print(memory_usage())