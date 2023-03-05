try:
    age=int(input("ENTER THE AGE --> "))
    if age>=18:
        print("ELIGIBLE TO VOTE")
    elif age>=0 and age<18:
        print("NOT ELIGIBLE TO VOTE")
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
