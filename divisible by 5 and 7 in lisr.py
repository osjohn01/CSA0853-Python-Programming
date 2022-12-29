l=[]
lnew=[]
n=int(input("ENTER NUMBER OF ELEMENTS --> "))
for a in range(n):
    l.append(int(input("ENTER ELEMENT FOR POSITION "+str(a+1)+" --> ")))
for i in l:
    if i%5==0 or i%7==0:
        lnew.append(i)
lnew.sort()
print("THE LIST OF NUMBERS THAT ARE EITHER DIVISBLE BY 5 AND/OR 7 IS --> ",lnew)
