try:
    l=[]
    count=0
    for i in range(int(input("ENTER NUMBER OF ELEMENTS --> "))):
        l.append(int(input("ENTER ITEM --> ")))
    for i in l:
        for j in range(2,i):
            if i%j==0:
                count+=1
                break
    print("ARRAY --> ",l)
    print("NUMBER OF COMPOSITE NUMBERS --> ",count)
except:
    print("INVALID INPUT")
