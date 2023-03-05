l=["banana", "carrot", "radish", "apple", "jack"]
ch=input("ENTER CHOICE --> ").lower()
if ch=="a":
    l.sort()
    print(l)
elif ch=="d":
    l.sort(reverse=True)
    print(l)
else:
    print("INVALID CHOICE")
