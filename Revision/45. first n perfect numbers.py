try:
    n=int(input("ENTER N --> "))
    i=0
    j=2
    print("FIRST ",n," PERFECT NUMBERS --> ",end=" ")
    while i<n:
        s=0
        for k in range(1,j):
            if j%k==0:
                s+=k
        if s==j:
            print(j,end=" ")
            i+=1
        j+=1
except:
    print("INVALID INPUT")
