l=[]
count=0
n=int(input("ENTER NUMBER OF ELEMENTS --> "))
for a in range(n):
    l.append(int(input("ENTER ELEMENT FOR POSITION "+str(a+1)+" --> ")))
print("THE LIST IS --> ",l)
l.sort()
n=int(input("ENTER THE VALUE OF N FOR NTH LARGEST --> "))
print("THE "+str(n)+"TH/ND/RD LARGEST NUMBER IN THE LIST IS --> ",l[-1*n])
