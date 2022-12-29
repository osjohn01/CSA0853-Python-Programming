s=input("ENTER ANY STRING --> ")
se=input("ENTER CHARACTER TO SEARCH --> ")
if se in s:
    print("CHARACTER FOUND!")
    for i in range(len(s)):
        if s[i]==se:
            print("INDEX --> ",i)
            break
else:
    print("CHARACTER NOT FOUND")
