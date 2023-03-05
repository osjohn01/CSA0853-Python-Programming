s=input("ENTER A STRING -> ")
c=0
for a in s:
    if a.isalpha() or a.isnumeric():
        continue
    else:
        c+=1
        print(a,end=" ")
print("\n",c)
