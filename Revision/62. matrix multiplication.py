m1=[]
m2=[]
mul=[]
r=2
c=2
print("\nMATRIX 1\n")
for i in range(r):
    l=[]
    for j in range(c):
        l.append(int(input()))
    m1.append(l)
print("\nMATRIX 2\n")
for i in range(r):
    l=[]
    for j in range(c):
        l.append(int(input()))
    m2.append(l)
print("\nMATRIX 1\n")
for i in range(r):
    print()
    for j in range(c):
        print(m1[i][j], end=" ")
print("\nMATRIX 2\n")
for i in range(r):
    print()
    for j in range(c):
        print(m2[i][j], end=" ")
for i in range(r):
    l=[]
    for j in range(c):
        s=0
        for k in range(2):
            s+=m1[i][k]*m2[k][j]
        l.append(s)
    mul.append(l)
print("\nMATRIX MUL\n")
for i in range(r):
    print()
    for j in range(c):
        print(mul[i][j], end=" ")
