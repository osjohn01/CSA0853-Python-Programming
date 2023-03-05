lnum=[]
n=int(input("N --> "))
if n>=2:
    for i in range(n):
        lnum.append(int(input("ENTER NUMBER "+str(i+1)+" --> ")))
    s=2
    while True:
        for a in lnum:
            if s%a==0:
                flag=True
            else:
                flag=False
                break
        if flag==True:
            print("LCM --> ",s)
            break
        else:
            s+=1
    s=2
    d=[]
    p=None
    while True:
        for a in lnum:
            if s==a:
                p=True
                break
            if a%s==0:
                flag=True
            else:
                flag=False
                break
        if p==True:
            break
        if flag==True:
            d.append(s)
        s+=1
    print("GCD --> ", d[len(d)-1])
else:
    print("INVALID INPUT")
