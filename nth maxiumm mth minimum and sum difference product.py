l=[]
n=int(input("ENTER NUMBER OF ELEMENTS --> "))
for a in range(n):
    l.append(int(input("ENTER ELEMENT FOR POSITION "+str(a+1)+" --> ")))
l.sort()
m=int(input("ENTER THE M VALUE FOR MAXIMUM --> "))
n=int(input("ENTER THE N VALUE FOR MINIMUM --> "))
print("MTH MAXIMUM --> ",l[-1*m])
print("NTH MINIMUM --> ",l[n-1])
print("SUM --> ",l[-1*m]+l[n-1])
print("DIFFERENCE --> ",l[-1*m]-l[n-1])
print("PRODUCT --> ",l[-1*m]*l[n-1])
