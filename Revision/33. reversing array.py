n=int(input("ENTER NUMBER OF ELEMENTS --> "))
l=[]
lrev=[]
print("ENTER THE ELEMENTS")
for i in range(n):
    l.append(int(input()))
print("ARRAY --> ",l)
for i in range(len(l)-1,-1,-1):
    lrev.append(l[i])
print("REVERSED ARRAY --> ",lrev)
    
