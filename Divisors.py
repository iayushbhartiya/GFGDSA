#----------------Naive method--------------

# def divisors(n):
#     i = 1
#     while i <= n:
#         if n%i == 0:
#             print(i)
#         i +=1
#
# divisors(12)

# time complexity - O(n)

# ---------------Efficient method----------

# def divisors(n):
#     i = 1
#     while i*i <= n:
#         if n%i == 0:
#             res = n//i
#             print(i)
#             if i!= res:
#                 print(res)
#         i+=1
#
# divisors(25)
# results are not sorted
# time complexity O(sqrt(n))

# ---------------Efficient & Sorted---------

def divisors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
        i += 1

    while i >= 1:
        if n % i == 0:
            print(n//i)
        i -= 1



divisors(24)

# time complexity O(sqrt(n))