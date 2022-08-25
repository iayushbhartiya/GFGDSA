# --------------Brute force-------------------------
# def LCM(x,y):
#     res = max(x,y)
#     while True:
#         if res % x == 0 and res % y == 0:
#             return res
#         res+=1
#
# print(LCM(4,5))
#  time complexity - O(x*y)

# -----------------Efficient method------------------

def GCD(a,b):
    if b == 0 :
        return a
    return GCD(b, a % b)

def LCM(a,b):
    res = (a * b) // GCD(a,b)
    return res

print(LCM(4,6))
# time complexity - O(log(min(a,b))



