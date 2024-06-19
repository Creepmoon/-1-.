from memory_profiler import memory_usage
from datetime import datetime

def check_brackets(sequence):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for i, char in enumerate(sequence):
        if char in brackets:
            stack.append((char, i + 1))
        elif char in brackets.values():
            if not stack:
                return i + 1
            top, top_index = stack.pop()
            if brackets[top] != char:
                return i + 1

    if stack:
        return stack[0][1]

    return "Success"


Start_time = datetime.now()
with open("input.txt", "r") as file:
    sequence = file.read().strip()

result = check_brackets(sequence)

with open("output.txt", "w") as file:
    file.write(str(result))

print(datetime.now() - Start_time)
print(memory_usage())

