try:
    n=int(input("N --> "))
    if n>0:
        n1=s=0
        i=1
        ch=int(input("1. ODD\n2. EVEN\n3. SQUARES\n4. CUBE\nENTER CHOICE --> "))
        match ch:
            case 1:
                while n1<n:
                    if i%2!=0:
                        s+=i
                        n1+=1
                    i+=1
                print("MEAN OF FIRST {} ODD NUMBERS IS --> {}".format(n,s/n))
            case 2:
                while n1<n:
                    if i%2==0:
                        n1+=1
                        s+=i
                    i+=1
                print("MEAN OF FIRST {} EVEN NUMBERS IS --> {}".format(n,s/n))
            case 3:
                for i in range(1,n+1):
                    s+=i**2
                print("MEAN OF FIRST {} SQUARES IS --> {}".format(n,s/n))
            case 4:
                for i in range(1,n+1):
                    s+=i**3
                print("MEAN OF FIRST {} CUBES IS --> {}".format(n,s/n))
            case default:
                print("INVALID INPUT")
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
