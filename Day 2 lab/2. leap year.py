try:
    y=int(input("ENTER THE YEAR --> "))
    if y>0:
        if y%4==0:
            print(y,"IS A LEAP YEAR")
        else:
            print(y,"IS NOT A LEAP YEAR")
            print("PREVIOUS LEAP YEAR --> ",(y//4)*4)
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
