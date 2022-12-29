a=[[1,2,3],[3,2,5],[8,3,4]]
b=[[1,2,3],[3,2,5],[8,3,4]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]
for i in range(len(a)):
    for j in range(len(b)):
        print(c[i][j],end="  ")
    print()
