s=input("ENTER ELEMENTS OF THE LIST SEPERATED BY SPACE --> ")
l=s.split()
n=0
for a in l:
    b=int(a)
    if b>n:
        n=b
print("THE MAXIMUM ELEMENT IN THE LIST IS --> ",n)
