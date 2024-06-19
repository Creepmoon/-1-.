from memory_profiler import memory_usage
from datetime import datetime
import time



class MN:
    def __init__(self):
        self.a: set = set()

    def A(self, value: int):
        self.a.add(value)
        return None

    def D(self, value: int):
        self.a.discard(value)
        return None

    def Q(self, value: int):
        if value in self.a:
            return "Y"
        else:
            return "N"


def main():
    Start_time = datetime.now()
    mn = MN()
    a: list = []
    with open('input.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            a.append((line.split()))
    with open("output.txt", "w") as f:
        for i in range(len(a)):
            if a[i][0] == "A":
                mn.A(int(a[i][1]))
            elif a[i][0] == "D":
                mn.D(int(a[i][1]))
            elif a[i][0] == "?":
                print(mn.Q(int(a[i][1])), file=f)
    print(datetime.now() - Start_time)
    print(memory_usage())

main()