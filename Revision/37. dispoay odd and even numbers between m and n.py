try:
    m=int(input("M --> "))
    n=int(input("N --> "))
    e=[]
    o=[]
    if m>0 and n>0:
        if m>n:
            m,n=n,m
        for i in range(m+1,n):
            if i%2==0:
                e.append(str(i))
            else:
                o.append(str(i))
        print("ODD --> "," ".join(o))
        print("EVEN --> "," ".join(e))
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
