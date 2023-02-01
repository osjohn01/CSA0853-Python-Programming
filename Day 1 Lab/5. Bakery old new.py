new=int(input("ENTER THE NUMBER OF FRESH LOAVES --> "))
old=int(input("ENTER THE NUMBER OF OLD LOAVES --> " ))
if new>=0 and old>=0:
    print("REGULAR PRICE --> ",'%.2f' % ((new+old)*185))
    pnew=new*185.00
    pold=old*(0.40*185.00)  
    print("AMOUNT OF NEW LOAVES --> ", '%.2f' % pnew)
    print("AMOUNT OF DAY OLD LOAVES --> ", '%.2f' % pold)
    print("TOTAL AMOUNT --> ",'%.2f' % (pnew+pold))
else:
    print("INVALID INPUT")
