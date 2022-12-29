l=[]
for i in range(5):
    a=input("ENTER ELEMENT "+str(i+1)+" FOR LIST --> ")
    l.append(a)
for i in range(len(l)):
    for j in range(i):
        if len(l[j])>len(l[i]):
            l[i],l[j]=l[j],l[i]
print("THE LIST AFTER SORTING IS --> ",l)
