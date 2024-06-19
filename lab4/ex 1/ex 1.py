from collections import deque
from memory_profiler import memory_usage
from datetime import datetime
import time
Start_time = datetime.now()


file1=open("input.txt")
nums=[]
stack=deque()
removed=[]
while True:
    line = file1.readline()
    if not line:
       break
    nums.append((line.split()))
for i in range(len(nums)):
    if nums[i][0]=='+':
        stack.append(nums[i][1])
    elif nums[i][0] == '-':
        if len(stack) == 0:
            continue
        else:
            removed.append(str(stack[-1]))
            stack.pop()
g = open('output.txt', 'w')
g.write("".join(str(i + "\n") for i in removed))
g.close()
print(datetime.now() - Start_time)
print(memory_usage())







