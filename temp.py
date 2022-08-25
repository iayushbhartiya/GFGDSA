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


def exactly3Divisors(N):
    count = 0
    for i in range(4, N + 1):
        if isprime(i) == True:
            continue
        else:
            res = 0
            for j in range(1,i+1):
                if isprime(j) == True and j*j<=i and i % j == 0 :
                    count +=1
    return count


print(exactly3Divisors(15))
