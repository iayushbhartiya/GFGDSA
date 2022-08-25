# check if the kth bit is set


def setbit(n, k):
    # left shift
    # if n & 1 << (k - 1) != 0:
    #     return True
    # else:
    #     return False
#------------------------------------------
#     right shift
    if 1 & n >> (k-1) != 0:
        return True

    else:
        return False


n = 5
k = 2
print(setbit(n, 3))
