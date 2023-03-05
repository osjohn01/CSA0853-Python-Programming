x=int(input("ENTER VALUE OF X --> "))
n=int(input("ENTER VALUE OF N --> "))
ch=input("ENTER CHOICE POW/ADD/SUB/MUL/DIV --> ").lower()
if ch=="pow":
    print("POW({},{}) --> ".format(x,n),x**n)
elif ch=="add":
    print("ADD({},{}) --> ".format(x,n),x+n)
elif ch=="sub":
    print("SUB({},{}) --> ".format(x,n),x-n)
elif ch=="div":
    print("DIV({},{}) --> ".format(x,n),x/n)
else:
    print("INVALID INPUT")
