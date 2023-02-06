def delchar(s,c):
    l=[]
    if len(c)==1:
        for a in s:
            if a!=c:
                l.append(a)
        print("".join(l))
    else:
        print(s)
s=input("ENTER STRING --> ")
c=input("ENTER CHARACTER TO DELETE FROM STRING --> ")
delchar(s,c)
