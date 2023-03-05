c=int(input("CASE 1 --> WORD\nCASE 2 --> NUMBER\nENTER YOUR CHOICE --> "))
s=input("INPUT --> ")
flag=True
if c==1:
    for a in s:
        if a.isnumeric():
            print("INVALID INPUT")
            flag=False
elif c==2:
    for a in s:
        if a.isalpha():
            print("INVALID INPUT")
            flag=False
else:
    print("INVALID INPUT")
if flag==True:
    if s==s[::-1]:
        print("PALINDROME")
    else:
        print("NOT A PALINDROME") 
