def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
n=int(input("ENTER THE NUMBER OF LINES --> "))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(f(i)//(f(j)*f(i-j)),end=" ")
    print()
