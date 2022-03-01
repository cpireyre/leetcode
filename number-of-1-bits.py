def hammingWeight(n):
    return 0 if not n else 1 + hammingWeight(n & n - 1)
# Runtime: 43 ms, faster than 56.91% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 14 MB, less than 51.17% of Python3 online submissions for Number of 1 Bits.
