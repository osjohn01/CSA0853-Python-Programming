n=int(input("N --> "))
num=input("ENTER "+str(n)+" DIGIT NUMBER --> ")
num=num.lstrip("0")
if len(num)==n:
    num=int(num)
    s=0
    while num!=0:
        s+=num%10
        num//=10
    print("SUM OF DIGITS IS --> ",s)
else:
    print("INVALID ",n," DIGIT NUMBER")
