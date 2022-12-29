l=[]
for i in range(7):
    a=int(input("ENTER ELEMENT "+str(i+1)+" FOR LIST --> "))
    l.append(a)
srch=int(input("ENTER SEARCH ELEMENT --> "))
flag=False
for i in range(len(l)):
    if l[i]==srch:
        print("ELEMENT FOUND AT INDEX ",i)
        flag=True
        break
if flag==False:
    print("ELEMENT NOT FOUND")
