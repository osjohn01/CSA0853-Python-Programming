def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
def countWays(s):
    return fib(s + 1)
n=int(input("ENTER NUMBER OF STAIRS -> "))
print("NUMBER OF OUTCOMES --> ",countWays(n))
