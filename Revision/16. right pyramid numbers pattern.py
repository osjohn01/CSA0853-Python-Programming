n=int(input("ENTER THE NUMBER OF LINES --> "))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
