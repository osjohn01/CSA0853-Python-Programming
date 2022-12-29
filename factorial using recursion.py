def fact(n):
    if n!=0:
        return n*fact(n-1)
    else:
        return 1
n=int(input("ENTER THE NUMBER --> "))
print("THE FACTORIAL IS --> ",fact(n))
