import cmath as m
a=int(input("ENTER VALUE OF A --> "))
b=int(input("ENTER VALUE OF B --> "))
c=int(input("ENTER VALUE OF C --> "))
print("THE QUADRATIC EQUATION IS --> ",a,"x² +",b,"x +",c)
d=b**2-4*a*c
if d==0:
    print("ROOTS ARE REAL AND EQUAL")
elif d>0:
    print("ROOTS ARE REAL AND UNEQUAL")
else:
    print("ROOTS ARE IMAGINARY")

x1=((-1*b)+m.sqrt(d))/(2*a)
x2=((-1*b)-m.sqrt(d))/(2*a)
print("THE FIRST ROOT IS ",x1)
print("THE SECOND ROOT IS ",x2)
