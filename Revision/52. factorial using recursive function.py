def f(n):
    if n!=0:
        return n*f(n-1)
    else:
        return 1
n=int(input("ENTER NUMBER --> "))
print(f(n))
