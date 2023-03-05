n=int(input("ENTER NUMBER --> "))
sq=str(n**(1/2))
if ".0" in sq:
    print(sq)
    print(-1*float(sq))
else:
    print("NOT A PERFECT SQUARE")
