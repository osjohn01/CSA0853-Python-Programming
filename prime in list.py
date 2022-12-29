l=[]
for i in range(7):
    a=int(input("ENTER ELEMENT "+str(i+1)+" FOR LIST --> "))
    l.append(a)
print("THE FOLLOWING ARE PRIME FROM THE LIST --> ")
for a in l:
    flag=True
    for i in range(2,a):
        if a%i!=0:
            flag=False
        else:
            flag=True
            break
    if flag==False:
        print(a, end=" ")
