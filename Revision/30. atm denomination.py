lden=[2000,500,200,100]
i=1
s=0
while i<=4:
    d=int(input("\nENTER THE {}st/rd/th DENOMINATION --> ".format(i)))
    if d in lden:
        n=int(input("ENTER NUMBER OF {} NOTES --> ".format(d)))
        s+=d*n
        i+=1
    else:
        print("\nINVALID DENOMINATION, TRY AGAIN!")
print("TOTAL AVAILABLE BALANCE IN ATM --> ",s)
