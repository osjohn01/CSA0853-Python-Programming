s=input("ENTER ANY WORD --> ")
a=[]
b=""
for i in s:
    a.append(i)
a.sort()
for i in a:
    b+=i
print("THE WORD IN NORMAL ORDER --> ",b)
print("THE WORD IN REVERSE ORDER --> ",b[::-1])
