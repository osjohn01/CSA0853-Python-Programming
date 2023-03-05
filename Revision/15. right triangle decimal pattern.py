n=int(input("ENTER THE NUMBER OF LINES --> "))
a=1
for i in range(n):
    for j in range(i+1):
        print((a)**2/100,end=" ")
        a+=1
    print()
