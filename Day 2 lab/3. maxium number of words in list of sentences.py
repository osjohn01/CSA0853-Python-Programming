n=int(input("ENTER NUMBER OF SENTENCES --> "))
lsen=[]
lcount=[]
for i in range(n):
    lsen.append(input("ENTER THE SENTENCE --> "))
for i in lsen:
    lcount.append(len(i.split()))
print(lcount)
lcount.sort()
print("MAXIMUM NUMBER OF WORDS IS --> ",lcount[n-1])
