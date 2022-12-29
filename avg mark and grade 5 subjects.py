m1=int(input("ENTER THE MARKS OF FIRST SUBJECT --> "))
m2=int(input("ENTER THE MARKS OF SECOND SUBJECT --> "))
m3=int(input("ENTER THE MARKS OF THIRD SUBJECT --> "))
m4=int(input("ENTER THE MARKS OF FOURTH SUBJECT --> "))
m5=int(input("ENTER THE MARKS OF FIFTH SUBJECT --> "))
avg=(m1+m2+m3+m4+m5)/5
print("THE AVERAGE MARK IS --> ",avg)
if avg==100:
    grade="A+"
elif avg<100 and avg>90:
    grade="A"
elif avg<=90 and avg>80:
    grade="B"
elif avg<=80 and avg>70:
    grade="C"
elif avg<=70 and avg>60:
    grade="D"
elif avg<=60 and avg>50:
    grade="E"
else:
    grade="F"
print("THE GRADE IS --> ",grade)
    
