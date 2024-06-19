import random
OutputFile = open("input.txt","w")
OutputFile.write(str(100000)+ "\n")
array = []
for i in range(1,100001):
    array.append(random.randint(-10**9,10**9))
array.sort(reverse=True)
OutputFile.write(str(array)[1:-1].replace(",", ""))