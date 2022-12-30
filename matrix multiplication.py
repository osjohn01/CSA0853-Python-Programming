a=[[1,2,3],[3,2,5],[8,3,4]]
b=[[1,2,3],[3,2,5],[8,3,4]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
for i in c:
    print(i)
