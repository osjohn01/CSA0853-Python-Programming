import random
a=int(input("A --> "))
b=int(input("B --> "))
n=int(input("NUMBER OF ELEMENTS --> "))
l=[]
for i in range(n):
    l.append(random.randint(a,b))
print(l)
