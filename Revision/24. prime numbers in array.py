try:
    l=[]
    for i in range(int(input("ENTER NUMBER OF ELEMENTS --> "))):
        l.append(int(input("ENTER ITEM --> ")))
    lprime=[]
    for i in l:
        flag=None
        for j in range(2,i):
            if i%j==0:
                flag=False
                break
            else:
                flag=True
        if flag==True:
            lprime.append(i)
    print("ARRAY --> ",l)
    print("PRIME NUMBERS --> ",lprime)
except:
    print("INVALID INPUT")
