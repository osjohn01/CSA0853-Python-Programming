try:
    n=int(input("ENTER THE NUMBER --> "))
    if n>0:
        a=0
        n1=n
        while n!=0:
            a+=(n%10)**3
            n//=10
        if n1%a==0:
            print("ARMSTRONG NUMBER")
        else:
            print("NOT AN ARMSTRONG NUMBER")
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
