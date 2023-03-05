l=int(input("ENTER THE LENGTH OF THE RECTANGLE --> "))
b=int(input("ENTER THE BREADTH OF THE RECTANGLE --> "))
s=int(input("ENTER THE SIZE OF THE SQUARE --> "))
for i in range(s):
    for j in range(s):
        if i==0 or j==0 or i==s-1 or j==s-1:
            print("$",end=" ")
        else:
            print(end="  ")
    print()
print()
for i in range(b):
    for j in range(l):
        print("*",end=" ")
    print()
