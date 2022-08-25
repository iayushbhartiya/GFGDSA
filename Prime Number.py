def isprime(n):
    if n == 1:
        return False

    if n == 2 or n == 3:
        return True

    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i < n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(isprime(4889))

# time complexity - 3X faster O(sqrt n)
