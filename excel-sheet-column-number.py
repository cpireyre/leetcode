from functools import reduce
def titleToNumber(xs):
    return reduce(lambda a,b: 26*a+b, (ord(c)-64for c in xs))
# Runtime: 36 ms, faster than 77.88% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.9 MB, less than 83.72% of Python3 online submissions for Excel Sheet Column Number.

xs = "AA"
print(titleToNumber(xs))
xs = "ZY"
print(titleToNumber(xs))
xs = "AB"
print(titleToNumber(xs))
xs = "FXSHRXW"
print(titleToNumber(xs))
