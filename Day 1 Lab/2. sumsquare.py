def sumsquare(l):
    lnew=[]
    odd=0
    even=0
    for a in l:
        if a%2==0:
            even+=a*a
        else:
            odd+=a*a
    lnew.append(odd)
    lnew.append(even)
    print(lnew)
n=int(input("ENTER THE NUMBER OF ELEMENTS --> "))
l=[]
if n>0:
    for i in range(n):
        l.append(int(input("ENTER ELEMENT --> ")))
    sumsquare(l)
else:
    print("INVALID INPUT")
