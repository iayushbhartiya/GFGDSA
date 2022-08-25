#count set bits
# ----------------------------Naive Approach---------------------
# def countbits(n):
#     i = n
#     count = 0
#     k = 0
#     while i != 0:
#         i = n>>(k)
#         if i & 1 == 1:
#             count+=1
#         k+=1
#
#     return count
#
# a = 5
# print(countbits(a))

# time complexity- theta(Total bits in n)

# ----------------Brian Kernighan Algorithm------------------------

# In this algorithm the loop runs proportional to no of set bits

# Concept - When we subtract 1 from a number all the bits after
# the last set bit becomes 1 and that last set bit of the number
# becomes 0

# Step1 - computing n-1
# Step2 - taking AND of n & (n-1)

def countbits(n):
    count = 0
    while n != 0:
        n = n & (n-1)
        count+=1
    return count

a = 5
print(countbits(a))
# time complexity = theta(no. of set bits)

# --------------------------Lookup table method---------------------















