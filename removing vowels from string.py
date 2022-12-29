s=input("ENTER ANY STRING --> ")
b=""
for a in s:
    if a not in 'aeiouAEIOU':
        b+=a
print("THE STRING AFTER REMOVING THE VOWELS IS --> ",b)
