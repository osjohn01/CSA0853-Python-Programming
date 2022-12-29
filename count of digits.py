n=int(input("ENTER THE DIGIT --> "))
count=0
while n!=0:
    n//=10
    count+=1
print("NUMBER OF DIGITS IS --> ",count)
