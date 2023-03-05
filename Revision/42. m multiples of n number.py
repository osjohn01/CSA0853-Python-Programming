try:
    m=int(input("M --> "))
    n=int(input("N --> "))
    print(m," MULTIPLES OF ",n," ARE --> ",end=" ")
    if m>=0 and n>=0:
        for i in range(1,m+1):
            print(i*n, end=" ")
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
