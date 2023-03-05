sym=input("ENTER THE CHARACTER TO BE PRINTED --> ")
n=int(input("ENTER THE NUMBER OF LINES --> "))
for i in range(n+1):
    for j in range(i):
        print(sym,end=" ")
    print()
