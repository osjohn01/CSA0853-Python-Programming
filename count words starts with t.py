s=input("ENTER THE STRING --> ")
l=s.split()
count=0
for i in l:
    if i.startswith('t') or i.startswith("T"):
        count+=1
print("THE NUMBER OF ELEMENTS WITH WORDS THAT END IN 't' or 'T' IS --> ",count)
