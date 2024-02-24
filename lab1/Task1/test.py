import random
OutputFile = open("input.txt","w")
OutputFile.write(str(1000)+ "\n")
for i in range(1,1001):
    OutputFile.write(str(random.randint(-10**9,10**9)) + " ")