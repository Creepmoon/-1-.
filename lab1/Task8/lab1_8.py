import time
from datetime import datetime
from memory_profiler import memory_usage
def Solution(Array):
    length = len(Array)
    OutputFile = open("output.txt", "w")
    for i in range(1, length):
        x = i
        while x > 0 and Array[x - 1] > Array[x]:
            Array[x] = Array[x - 1]
            x -= 1
        if(x!=i):
            OutputFile.write("Swap elements at indices " + str(x+1) + " and " + str(i+1) + ". \n")
    OutputFile.write("No more swaps needed.")

Start_time = datetime.now()
InputFile = open("input.txt", "r")
length = int(InputFile.readline())
String = InputFile.readline().split(" ")
InputFile.close()
array = [0] * length
for i in range(0, length):
    array[i] = int(String[i])
Solution(array)
print(datetime.now()- Start_time)
print(memory_usage())