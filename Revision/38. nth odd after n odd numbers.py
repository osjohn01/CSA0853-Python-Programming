try:
    n=int(input("N --> "))
    if n>0:
        i=1
        n1=0
        while True:
            if i%2!=0:
                n1+=1
                if n1==2*n:
                    print("ANSWER --> ",i)
                    break
            i+=1
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
