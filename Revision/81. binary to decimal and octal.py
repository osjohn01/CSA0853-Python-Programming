b=input("ENTER BINARY NUMBER --> ")
d=0
a=0
for i in range(len(b)-1,-1,-1):
    d+=int(b[i])*2**a
    a+=1
print(d)
print(oct(d).replace('0o',""))
