l1=[]
l2=[]
lnew=[]
n=int(input("ENTER NUMBER OF ELEMENTS --> "))
print("LIST 1 --> ")
for a in range(n):
    l1.append(int(input("ENTER ELEMENT FOR POSITION "+str(a+1)+" --> ")))
print("LIST 2 --> ")
for a in range(n):
    l2.append(int(input("ENTER ELEMENT FOR POSITION "+str(a+1)+" --> ")))
lnew=l1+l2
print("LIST 1 --> ",l1)
print("LIST 2 --> ",l2)
print("MERGED LIST --> ",lnew)
