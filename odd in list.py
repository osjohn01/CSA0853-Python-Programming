l=[]
count=0
n=int(input("ENTER NUMBER OF ELEMENTS --> "))
for a in range(n):
    l.append(int(input("ENTER ELEMENT FOR POSITION "+str(a+1)+" --> ")))
print("THE LIST IS --> ",l)
for i in l:
    if i%2!=0:
        count+=1
        print(i, end=" ")
print("\nTHE NUMBER OF ODD NUMBER IN THE LIST IS --> ",count)
