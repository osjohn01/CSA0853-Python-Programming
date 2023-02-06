n=int(input("ENTER THE NUMBER OF ELEMENTS --> "))
l=[]
lcount=[]
for i in range(n):
    l.append(int(input("ENTER ELEMENT" + str(i+1)+" --> ")))
for a in l:
    i=0
    for b in l:
        if b<a:
            i+=1
    lcount.append(i)
print(lcount)
