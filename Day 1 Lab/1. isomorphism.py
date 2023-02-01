s=input("ENTER STRING 1 --> ")
t=input("ENTER STRING 2 --> ")
snew=""
d={}
L=len(s)
if len(s)==len(t):
    for i in range(L):
        for j in 'abcdefghijklmnopqrstuvwxyz':
            if j==t[i]:
                d[s[i]]=t[i]
    for i in s:
        snew+=d[i]
    if snew==t:
        print("TRUE")
    else:
        print("FALSE")
                
else:
    print("FALSE")
