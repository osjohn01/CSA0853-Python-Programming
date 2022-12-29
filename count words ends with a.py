s=input("ENTER THE STRING --> ")
l=s.split()
count=0
for i in l:
    if i.endswith('a') or i.endswith('A'):
        count+=1
print("THE NUMBER OF ELEMENTS WITH WORDS THAT END IN 'a' or 'A' IS --> ",count)
