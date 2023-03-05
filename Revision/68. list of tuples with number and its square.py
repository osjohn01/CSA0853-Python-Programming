u=int(input("UPPER RANGE --> "))
l=int(input("LOWER RANGE --> "))
li=[]
for i in range(u,l+1):
    t=(i,i**2)
    li.append(t)
print(li)
