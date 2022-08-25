# --------------naive method -----------------------
# def trailing_zero(n):
#     num = n
#     res = 1
#     val = 0
#
#     while num > 0:
#         res = num * res
#         num -= 1
#
#     while (res%10) == 0:
#         val +=1
#         res = res // 10
#     return val
#
# print(trailing_zero(100))

# time complexity = theta(n)

# --------------------Efficient method----------------

def trailing_zero(n):
    res = 0
    a = 5
    while a < n :
        res = res + n//a
        a = a * 5
    return res

print(trailing_zero(251))

# time complexity - theta(log5n) {no overflow issue}