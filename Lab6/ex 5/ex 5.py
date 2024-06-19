from memory_profiler import memory_usage
from datetime import datetime
import time



def add_book(bk: dict, key: str, value: int):
        if key in bk:
            bk[key] += value
            return None
        bk[key] = value
        return None

def qs(a):
    return qs([x for x in a[1:] if x <= a[0]]) + [a[0]] + qs([x for x in a if x > a[0]]) if a else []


def main():
    Start_time = datetime.now()
    a: list = []
    book: dict = {}
    with open('input.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            a.append((line.split()))
    for i in range(len(a)):
        add_book(book, a[i][0], int(a[i][1]))
    result: list = []
    for i in book.items():
        result.append(i)
    result = qs(result)
    with open("output.txt", "w") as f:
        for i in result:
            f.write(str(i).replace('\'',"").replace(",",'')[1:-1] + "\n")
    print(datetime.now() - Start_time)
    print(memory_usage())
main()