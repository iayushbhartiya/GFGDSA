# Find only two odd occuring elements

def odd(arr):
    # Dividing the array into array of set bit and unset bit
    res1 = []
    res2 = []
    for i in arr:
        if i & 1 == 1:
            res1.append(i)
        else:
            res2.append(i)
    ans1 = 0
    ans2 = 0
    for i in res1:
        ans1 = ans1 ^ i
    for j in res2:
        ans2 = ans2 ^ j

    return ans1, ans2


val = [1, 2, 1, 4, 3, 4, 4, 4, 5, 5]
print(odd(val))
