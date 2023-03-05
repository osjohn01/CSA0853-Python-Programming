s=input("ENTER A STRING --> ")
srev=""
if s.isalpha():
    for i in range(len(s)-1,-1,-1):
        srev+=s[i]
    print("REVERSED STRING --> ",srev)
else:
    print("INVALID WORD INPUT")
