l=int(input("ENTER THE LENGTH OF THE RECTANGLE --> "))
b=int(input("ENTER THE BREADTH OF THE RECTANGLE --> "))
sym=input("ENTER THE SYMBOL TO BE USED --> ")
for i in range(b):
    for j in range(l):
        print(sym,end=" ")
    print()
