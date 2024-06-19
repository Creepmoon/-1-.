from memory_profiler import memory_usage
from datetime import datetime




Start_time = datetime.now()

q = []

f = open('input.txt')
n = open('output.txt', 'w')
cmds = [el.replace('\n', '') for el in f.readlines()]
for cmd in cmds:
    if cmd[0] == '+':
        q.append(int(cmd[2:]))
    elif cmd == '-':
        del q[0]
    elif cmd == '?':
        m = 10**9+1
        for el in q:
            if el < m:
                m = el
        print(m, file=n)
print(datetime.now() - Start_time)
print(memory_usage())


