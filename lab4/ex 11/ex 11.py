from collections import deque
from memory_profiler import memory_usage
from datetime import datetime

Start_time = datetime.now()


file1 = open("input.txt", "r")
nums = []
stack = deque()
legit = 0

while True:
    line = file1.readline()
    if not line:
        break
    nums.append((line.split()))
file1.close()
for i in range(len(nums[1])):
    stack.append(nums[1][i])
kolvo_spravok=nums[0][1]
for i in range(int(kolvo_spravok)):
    new_kolvo_spravok=int((stack.popleft()))-1
    if new_kolvo_spravok!=0:
        stack.append(new_kolvo_spravok)
    if len(stack)==0:
        legit=-1
if legit==-1:
    print(legit)
else:
    fileVar = open("output.txt", "w")
    fileVar.write(str(len(stack))+'\n')
    fileVar.write(str(stack)[7:-2].replace(",",'').replace("\'",""))
    fileVar.close()
print(datetime.now() - Start_time)
print(memory_usage())

