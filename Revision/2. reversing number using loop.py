try:
    n=int(input("ENTER A NUMBER --> "))
    nrev=0
    if n>0:
        while n!=0:
            nrev=nrev*10+n%10
            n//=10
        print("THE REVERSED NUMBER IS --> ",nrev)
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
