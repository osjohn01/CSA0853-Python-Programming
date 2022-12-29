a=int(input("ENTER THE FIRST NUMBER --> "))
b=int(input("ENTER THE SECOND NUMBER --> "))
c=int(input("ENTER THE THIRD NUMBER --> "))
if a>b and a>c:
    print("THE GREATEST NUMBER IS ",a)
elif b>c and b>a:
    print("THE GREATEST NUMBER IS ",b)
else:
    print("THE GREATEST NUMBER IS ",c)
