import math

def count(n):
    res = 1
    for i in range(n, 1, -1):
        res = res + math.log10(i)
    return math.floor(res)

print(count(5))

# fac(5) = 120 output - 3

# number of digit in n! = log10(n!)