# ============Brute Force=======================

# def isprime(n):
#     if n == 1:
#         return False
#
#     if n == 2 or n == 3:
#         return True
#
#     elif n % 2 == 0 or n % 3 == 0:
#         return False
#
#     i = 5
#     while i * i < n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#
#     return True
#
#
# def prime_fac(n):
#     i = 2
#     while i < n:
#         if isprime(i) == True:
#             x = i
#             while n % x == 0:
#                 print(i)
#                 x = x * i
#         i += 1
#
#
# prime_fac(12)

# ===================Other Method================================

def prime_fac(n):
    tar = n
    i = 2
    while tar > 1:
        if tar % i == 0:
            tar = tar // i


        else:
            i += 1
            continue

        print(i)


prime_fac(17)
