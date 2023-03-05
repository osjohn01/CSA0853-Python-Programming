sym=int(input("ENTER THE NUMBER TO BE PRINTED --> "))
n=int(input("ENTER THE NUMBER OF TIMES TO BE PRIMTED --> "))
for i in range(n):
    for j in range(i+1):
        print(sym,end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print(sym,end="")
    print()
