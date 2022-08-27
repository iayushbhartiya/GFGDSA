# Find the missing number from the list from the range of number
# Given an arr of number between the range of 1 to (n+1) find the missing one from the list

def missing(arr):
    res1 = 0
    res2 = 0
    for i in range(1,len(arr)+2):
        res1 = res1 ^ i
    for j in arr:
        res2 = res2 ^ j

    return res1 ^ res2


val = [1,4,3]
print(len(val))
print(missing(val))

# o/p = 2