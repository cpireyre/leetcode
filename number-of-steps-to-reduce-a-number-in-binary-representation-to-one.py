def numSteps(s):
    res, n = 0, int(s, base=2)
    while n != 1:
        res += 1 + (n & 1)
        n = (n + (n & 1)) >> 1
    return res
# Runtime: 24 ms, faster than 99.25% of Python3 online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
# Memory Usage: 14 MB, less than 46.79% of Python3 online submissions for Number of Steps to Reduce a Number in Binary Representation to One.
