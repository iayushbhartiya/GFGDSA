def palindrome(n):
    num = n
    res = 0

    while num >0:
        res = res * 10 + (num % 10)
        num = num//10

    if res == n:
        return True
    else:
        return False

print(palindrome(1232))

# complexity -- theta(d) d - number of digits