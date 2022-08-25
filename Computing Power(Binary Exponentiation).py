# -----------without using inbuilt funtion----------------------
# --------------naive method-------------------------

def power(x, n):
    if n == 0:
        return 1
    i = 1
    res = 1
    while i <= n:
        res = res * x
        i += 1
    return res


print(power(3, 4))

# time complexity - O(n)

# ----------------Efficient method----------------------------------
