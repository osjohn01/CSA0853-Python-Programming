w=input("ENTER THE WORD --> ")
w1=[]
s=""
for i in w:
    w1.append(i)
w1.sort()
for i in w1:
    s=i+s
print(s)
