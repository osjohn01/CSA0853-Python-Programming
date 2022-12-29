s=input("ENTER THE STRING --> ")
cv=0
for a in s:
    if a in 'aeiouAEIOU':
        cv+=1
print("THE NUMBER OF VOWELS ARE --> ",cv)
