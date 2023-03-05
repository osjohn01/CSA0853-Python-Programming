sym=input("ENTER SYMBOL --> ")
s=int(input("ENTER THE SIZE OF THE SQUARE --> "))
for i in range(s):
    for j in range(s):
        if i==0 or j==0 or i==s-1 or j==s-1:
            print(sym,end=" ")
        else:
            print(end="  ")
    print()
