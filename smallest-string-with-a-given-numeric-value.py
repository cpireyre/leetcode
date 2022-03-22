# def getSmallestString(n, k):
#     res = []
#     while n and k:
#         n -= 1
#         diff = 26 if k - n > 26 else k - n
#         k -= diff
#         res.append(diff)
#     return "".join(chr(ord('a') + c - 1) for c in reversed(res))
# Runtime: 1016 ms, faster than 37.79% of Python3 online submissions for Smallest String With A Given Numeric Value.
# Memory Usage: 16.5 MB, less than 7.83% of Python3 online submissions for Smallest String With A Given Numeric Value.

def getSmallestString(n, k):
    q, r = divmod(k - n - 1, 25)
    return (n - q - 1) * 'a' + chr(97 + r + 1) + 'z' * q
# Runtime: 72 ms, faster than 81.57% of Python3 online submissions for Smallest String With A Given Numeric Value.
# Memory Usage: 14.9 MB, less than 87.56% of Python3 online submissions for Smallest String With A Given Numeric Value.



n, k = 3, 27 # "aay"
n, k = 5, 73 # "aaszz"
# n, k = 100000, 26 * 100000
print(getSmallestString(n, k))
