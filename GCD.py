# def HCF(n1, n2):
#     if n1 > n2:
#         num1 = n1
#         num2 = n2
#     else:
#         num1 = n2
#         num2 = n1
#
#     while num2 >0:
#         if num1 % num2 == 0:
#             return num2
#         num2-=1
#
# print(HCF(9,6))

# time complexity - O(min(a,b))

# -------------------Euclidean Algorithm(Recursion)-----------------

# def GCD(a, b):
#     if b == 0:
#         return a
#     return GCD(b, a % b)
#
#
# print(GCD(12, 20))

# ------------------Euclidean Algorithm(Loop)-------------------

def GCD(a, b):
    x = a
    y = b

    while x % y != 0:
        i = x % y
        x = y
        y = i

    return y


print(GCD(15, 9))
