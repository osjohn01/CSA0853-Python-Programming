s=input("ENTER THE STRING --> ")
si=s.lower()
if si[::-1]==si:
    print("THE STRING IS A PALINDROME!")
else:
    print("NOT A PALINDROME")
