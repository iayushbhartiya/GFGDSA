# Find the only odd occuring number

def odd(arr):
    res = 0
    for i in arr:
        res = res ^ i

    return res


print(odd([4, 3, 4, 4, 5, 4, 5]))

# concept -  x^0 = x
#            x^(y^z) = (x^y)^z = (x^z)^y
#            x^x = 0