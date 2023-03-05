def hollow(sym,a,b):
    for i in range(b):
        for j in range(a):
            if i==0 or j==0 or i==b-1 or j==a-1:
                print(sym,end=" ")
            else:
                print(end="  ")
        print()
def full(sym,a,b):
    for i in range(b):
        for j in range(a):
            print(sym,end=" ")
        print()
sym=input("ENTER THE SYMBOL --> ")
cht=input("PATTERN TYPE HOLLOW/FULL --> ")
chs=input("PATTERN SIZE SQUARE/RECTANGLE --> ")
chs=chs.lower()
cht=cht.lower()
if cht=="hollow" and chs=="square":
    s=int(input("ENTER LENGTH OF SIDE OF SQUARE --> "))
    hollow(sym,s,s)
elif cht=="full" and chs=="square":
    s=int(input("ENTER LENGTH OF SIDE OF SQUARE --> "))
    full(sym,s,s)
elif cht=="hollow" and chs=="rectangle":
    a=int(input("ENTER LENGTH OF RECTANGLE --> "))
    b=int(input("ENTER BREADTH OF RECTANGLE --> "))
    hollow(sym,a,b)
elif cht=="full" and chs=="rectangle":
    a=int(input("ENTER LENGTH OF RECTANGLE --> "))
    b=int(input("ENTER BREADTH OF RECTANGLE --> "))
    full(sym,a,b)
else:
    print("INVALID INPUT")
