try:
    l=[]
    for i in range(int(input("ENTER NUMBER OF ELEMENTS --> "))):
        l.append(int(input("ENTER ITEM --> ")))
    m=int(input("M --> "))
    n=int(input("N --> "))
    l.sort()
    p=len(l)
    print(l)
    print("{}th/rd/st MAXIMUM --> ".format(m),l[p-m])
    print("{}th/rd/st MINIUMUM --> ".format(n),l[n-1])
    print("SUM --> ",l[p-m]+l[n-1])
    print("DIFFERENCE --> ",l[p-m]-l[n-1])
except:
    print("INVALID INPUT")
