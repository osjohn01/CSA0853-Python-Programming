try:
    n=int(input("ENTER THE NUMBER --> "))
    if n>0:
        h=0
        n1=n
        while n!=0:
            h+=n%10
            n//=10
        if n1%h==0:
            print("HARSHAD NUMBER")
        else:
            print("NOT A HARHAD NUMBER")
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
