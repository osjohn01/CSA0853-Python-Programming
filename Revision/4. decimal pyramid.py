n=int(input("ENTER THE NUMBER OF LINES --> "))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print((j+1)/10,end=" ")
    print()
