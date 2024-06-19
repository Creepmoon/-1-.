import time
from memory_profiler import memory_usage

S_time= time.perf_counter()

def fibonacci(i, n1, n2):
    if i<1:
        return n2
    return fibonacci(i-1, n2, n1 + n2)
In = open("input.txt", "r")
i = int(In.read())
In.close()
Out = open("output.txt", "w")
if i == 1:
    Out.write("0")
elif i == 2:
    Out.write("1")
else:
    Out.write(str(fibonacci(i-1, 0, 1)))
print(time.perf_counter() - S_time)
print(memory_usage())