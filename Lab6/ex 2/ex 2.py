from memory_profiler import memory_usage
from datetime import datetime
import time


class tel_book:
    def __init__(self):
        self.book: dict = {}

    def add_number_name(self, number: str, name: str):
        self.book[f"{number}"] = name
        return None

    def del_number(self, number: str):
        if number in self.book:
            del self.book[number]
        return None

    def find_number(self, number: str):
        if self.book.get(number) is None:
            return "Not found"
        else:
            return self.book.get(number)


def main():
    with open("output.txt", "w") as f:
        for i in range(len(a)):
            if a[i][0] == "add":
                book.add_number_name(a[i][1], a[i][2])
            elif a[i][0] == "del":
                book.del_number(a[i][1])
            elif a[i][0] == "find":
                print(book.find_number(a[i][1]), file=f)
        print(datetime.now() - Start_time)
        print(memory_usage())


if __name__ == "__main__":
    Start_time = datetime.now()
    book = tel_book()
    a: list = []
    with open('input.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            a.append((line.split()))
    main()