try:
    y=input("ENTER YEAR IN DD/MM/YYYY FORMAT --> ")
    y=y.split("/")
    if int(y[0])>=1 and int(y[0])<=31 and int(y[1])>=1 and int(y[1])<=12 and int(y[2]):
        if int(y[2])%4==0:
            print("LEAP YEAR")
        else:
            print("NOT A LEAP YEAR")
    else:
        print("INVALID YEAR")
except:
    print("INVALID YEAR")
