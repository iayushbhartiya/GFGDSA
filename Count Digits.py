def digits(n):
    num = n
    res = 0
    if num==0:
        return 1
    while num>0:
        num = num//10
        res+=1
    return res

print(digits(123))

# complexity = theta(d) where d - number of digits

