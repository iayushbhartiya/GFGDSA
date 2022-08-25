# ---------------All prime numbers uptill n---------------
def prime_no(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i < n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes(n):
    for i in range(1, n + 1):
        if prime_no(i) == True:
            print(i)


primes(17)

# time complexity - O(n*sqrt(n))

# -----------------Efficient Method(Sieve of eratosthenes)------------------


