att=int(input("ENTER THE ATTENDENCE OF THE STUDENT --> "))
med='f'
if att>=75:
    print("THE STUDENT IS ELIGIBLE FOR THE EXAM")
else:
    while med not in 'yYnN':
        med=input("DOES THE STUDENT HAVE A MEDICAL CONDITION? Y/N --> ")
        if med in 'yY':
            print("THE STUDENT IS ELIGIBLE")
        elif med in 'nN':
            print("THE STUDENT IS NOT ELIGIBLE")
        else:
            print("INVALID INPUT! TRY AGAIN")
    
