lim=int(input("ENTER LIMIT --> "))
for a in range(1,lim):
    for b in range(1,lim):
        for c in range(1,lim):
            x=a**2
            y=b**2
            z=c**2
            if x+y==z:
                print(a,b,c)
