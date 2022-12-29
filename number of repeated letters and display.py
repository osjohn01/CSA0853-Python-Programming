s=input("ENTER ANY WORD --> ")
l=[]
count=0
for i in s:
    if i not in l:
        n=s.count(i)
        if n>1:
            print(i)
            count+=1
            print("THE NUMBER OF TIMES "+i+" HAS BEEN REPEATED IS --> ",n)
            l.append(i)
