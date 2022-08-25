# -----------------iterative solution------------------
def factorial(n):
    num = n
    res = 1
    if n == 0:
        return 1

    while num > 0:
        res = res * num
        num -= 1
    return res


print(factorial(1))

# time complexity - theta(n)

# ----------------recursive solution--------------------

def factorial(n):
    if n == 0:
        return 1            #theta(1)

    return n * factorial(n-1)            #T(n-1)

print(factorial(10))             #T(n) = T(n-1) + theta(1)

# time cmplexity - theta(n)