from functools import reduce
def reverse(n):
    if abs(n) < 10: return n
    res = []
    sign = -1 if n < 0 else 1
    n *= sign
    while n:
        res.append(n%10)
        n //= 10
    res = sign * reduce(lambda a,b:10*a+b, res)
    if res < -(2**31) or res > 2**31: return 0
    else: return res
# Runtime: 42 ms, faster than 57.11% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.9 MB, less than 66.58% of Python3 online submissions for Reverse Integer.

from sys import argv
print(reverse(int(argv[1])))
