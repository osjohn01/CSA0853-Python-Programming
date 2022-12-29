s=input("ENTER THE STRING TO CHECK THE PALINDROME --> ")
i=0
j=-1
while i<len(s):
    if s[i]==s[j]:
        flag=True
    else:
        flag=False
        break
    i+=1
    j-=1
if flag==True:
    print("THE STRING IS A PALINDROME")
else:
    print("THE STRING IS NOT A PALINDROME")
