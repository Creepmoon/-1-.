from memory_profiler import memory_usage
from datetime import datetime
import time
Start_time = datetime.now()



f = open('input.txt')
n = f.readline()
l = [int(x) for x in f.readline().split()]
ans_f = open('output.txt', 'w')

def quick_sort(s):
    if len(s)<=1:
        return s
    elem = s[0]
    left= list(filter(lambda x: x< elem,s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem,s))
    return quick_sort(left) + center + quick_sort(right)

ans_f.write(f"{quick_sort(l)}"[1:-1].replace(",",""))
print(datetime.now() - Start_time)
print(memory_usage())
