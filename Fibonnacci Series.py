# Printing nth fibonacci number Using recursive approach

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6)) 