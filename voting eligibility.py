age=int(input("ENTER THE AGE OF THE PERSON --> "))
if age>=18:
    print("THE PERSON IS ELIIBLE TO VOTE")
else:
    print("THE PERSON ISNT ELIGIBLE TO VOTE\nTHE PERSON CAN VOTE AFTER ", 18-age, "YEARS")
