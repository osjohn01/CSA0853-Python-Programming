try:
    d=int(input("ENTER DECIMAL NUMBER --> "))
    l_bin=['0','1']
    l_oct=['0','1','2','3','4','5','6','7']
    d1=d2=d
    o=b=""
    while d1!=0:
        b=l_bin[d1%2]+b
        d1//=2
    while d2!=0:
        o=l_oct[d2%8]+o
        d2//=8
    print(b, o)
except:
    print("INVALID INPUT")
