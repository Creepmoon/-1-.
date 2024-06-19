from memory_profiler import memory_usage
from datetime import datetime
import time
Start_time = datetime.now()


f = open('input.txt')
l = [int(x) for x in f.readline().split(',')]  #
ans_f = open('output.txt', 'w')
def H_index(l):
    l.sort()
    for i, cited in enumerate(l):
        result = len(l) - i
        if result <= cited:
            return result
    return 0


ans_f.write(f"{H_index(l)}")
print(datetime.now() - Start_time)
print(memory_usage())
