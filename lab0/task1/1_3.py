

In = open("input.txt","r")
a, b = (int(x) for x in In.read().split())
In.close()
Out = open("output.txt","w")
Out.write(str(a+b))

