x=(input("ENTER THE NUMBER --> "))
if x.isalpha():
    print("FALSE")
else:
    if int(x)>=0:
        if str(x)==str(x)[::-1]:
            print("TRUE")
        else:
            print("FALSE")
    else:
        print("FALSE")
