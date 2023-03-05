try:
    n=int(input("N --> "))
    if n>0:
        a=2
        i=2
        while i<=2*n:
            flag=None
            for j in range(2,a):
                if a%j==0:
                    flag=False
                    break
                else:
                    flag=True
            if flag==True:
                if i==n:
                    print("{}th/rd/st PRIME NUMBER IS ".format(i),a)
                    print("{} PRIME NUMBERS AFTER {} ARE ".format(n,a), end=" ")
                if i>n:
                    print(a,end=" ")
                i+=1
            a+=1
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
            
