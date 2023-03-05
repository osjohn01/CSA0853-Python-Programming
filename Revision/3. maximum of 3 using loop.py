n1=int(input("ENTER NUMBER 1 --> "))
n2=int(input("ENTER NUMBER 2 --> "))
n3=int(input("ENTER NUMBER 3 --> "))
l=[n1,n2,n3]
for i in range(len(l)):
    for j in range(i):
        if l[j]>l[i]:
            l[i],l[j]=l[j],l[i]
print("MAX --> ",l[2])
