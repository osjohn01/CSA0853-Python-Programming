s1=input("ENTER WORD 1 --> ")
s2=input("ENTER WORD 2 --> ")
ls1=[]
ls2=[]
for a in s1:
    ls1.append(a)
for a in s2:
    ls2.append(a)
ls1.sort()
ls2.sort()
if ls1==ls2:
    print("THE STRING ARE AN ANAGRAM")
else:
    print("THE STRINGS AREN'T AN ANAGRAM")
