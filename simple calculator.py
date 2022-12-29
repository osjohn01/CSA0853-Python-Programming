ans='y'
a=int(input("ENTER YOUR FIRST NUMBER --> "))
b=int(input("ENTER YOUR SECOND NUMBER --> "))
while ans in 'yY':
    ch=int(input("ENTER YOUR CHOICE\n\t1. ADDITION\n\t2. SUBTRACTION\n\t3. MULTIPLICATION\n\t4. DIVISION  --> "))
    if ch==1:
        print("SUM --> ",a+b)
    elif ch==2:
        print("DIFFERENCE --> ",a-b)
    elif ch==3:
        print("PRODUCT --> ",a*b)
    elif ch==4:
        print("QUOTIENT --> ",a/b)
    else:
        print("INVALID INPUT, TRY AGAIN")
    ans=input("DO YOU WANNA TRY OTHER OPERATIONS? y/n --> ")
    
