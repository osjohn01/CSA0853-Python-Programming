li=[200, 180, 180, 270, 160, 270, 270, 190, 200]
s=0
mean=0
mode=0
c=0
l=len(li)
li.sort()
if l%2==0:
    median=(li[int(l/2)-1]+li[int((l+1)/2)-1])/2
else:
    median=li[int((l+1)/2)-1]
for a in li:
    s+=a
    c1=li.count(a)
    if c1>c:
        c,c1=c1,c
        mode=a
print("MEAN --> ",s/l)
print("MEDIAN --> ",median)
print("MODE --> ",mode)
