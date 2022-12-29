l1=[]
l2=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS --> "))
for i in range(n):
    a=int(input("ENTER THE ELEMENT IN LIST 1 ELEMENT "+str(i+1)+" --> "))
    l1.append(a)
for i in range(n):
    a=int(input("ENTER THE ELEMENT IN LIST 2 ELEMENT "+str(i+1)+" --> "))
    l2.append(a)
l=l1+l2
print("LIST 1 --> ",l1)
print("LIST 2 --> ",l2)
print("MERGED LIST BEFORE SORTING --> ",l)
for i in range(len(l)):
    for j in range(i):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print("MERGED LIST AFTER SORTING --> ",l)
