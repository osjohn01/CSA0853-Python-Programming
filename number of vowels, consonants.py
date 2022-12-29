s=input("ENTER THE STRING --> ")
cv=cc=0
for a in s:
    if a in 'aeiouAEIOU':
        cv+=1
    elif a.isalpha():
        cc+=1
print("THE NUMBER OF VOWELS ARE --> ",cv)
print("THE NUMBER OF CONSONANTS ARE --> ",cc)
if cv>cc:
    print("VOWELS ARE MAXIMUM")
elif cc>cv:
    print("CONSONANTS ARE MAXIMUM")
else:
    printt("NUMBER OF CONSONANTS AND VOWELS ARE EQUAL")
