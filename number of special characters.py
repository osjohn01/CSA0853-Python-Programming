s=input("ENTER ANY STRING WITH SPECIAL CHARACTERS --> ")
spec=0
for a in s:
    if not a.isalpha() and not a.isdigit():
        spec+=1
print("THE NUMBER OF SPECIAL CHARACTERS IS --> ",spec)
        
