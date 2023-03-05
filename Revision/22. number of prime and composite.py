try:
    n=int(input("ENTER NUMBER OF VALUES --> "))
    cp=cc=0
    print("ENTER THE NUMBERS")
    for i in range(n):
        a=int(input())
        flag=None
        if a>0:
            for j in range(2,a):
                if a%j==0:
                    flag=False
                    break
                else:
                    flag=True
            if flag==True:
                cp+=1
            else:
                cc+=1
        else:
            print("INVALID INPUT")
            exit()
    print("PRIME --> ",cp)
    print("COMPOSITE --> ",cc)
except:
    print("INVALID INPUT")
