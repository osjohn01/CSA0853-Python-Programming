def large(l,n):
    print("THE LIST IS --> ",l)
    l.sort()
    print("THE FIRST LARGEST NUMBERS IN THE LIST ARE --> ",l[-1:n:-1])
l=[]
n=int(input("ENTER NUMBER OF ELEMENTS --> "))
for a in range(n):
    l.append(int(input("ENTER ELEMENT FOR POSITION "+str(a+1)+" --> ")))
n=int(input("ENTER THE VALUE OF N TO FIND THE FIRST N LARGEST NUMBERS --> "))
large(l,n)
