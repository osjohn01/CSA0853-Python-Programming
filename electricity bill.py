u=int(input("ENTER THE UNITS CONSUMED --> "))
if u>500:
    cost=u*10.32
elif u<=500 and u>100:
    cost=u*7.43
else:
    cost=u*3.46
print("THE COST IS --> Rs.",cost)
