try:
    m=int(input("M --> "))
    n=int(input("N --> "))
    e=o=0
    if m>0 and n>0:
        if m>n:
            m,n=n,m
        for i in range(m+1,n):
            if i%2==0:
                e+=1
            else:
                o+=1
        print("ODD --> ",o)
        print("EVEN --> ",e)
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
