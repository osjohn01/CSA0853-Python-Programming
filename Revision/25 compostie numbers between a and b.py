try:
    a=int(input("A --> "))
    b=int(input("B --> "))
    if a>0 and b>a and b>0:
        for k in range(a+1,b):
            flag=None
            for i in range(2,k):
                if k%i==0:
                    flag=False
                    break
                else:
                    flag=True
            if flag==False:
                print(k, end=" ")
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
