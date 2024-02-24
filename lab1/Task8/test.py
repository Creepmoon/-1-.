import random
OutputFile = open("input.txt","w")
OutputFile.write(str(5000)+ "\n")
for i in range(1,5001):
    OutputFile.write(str(random.randint(-10**9,10**9)) + " ")