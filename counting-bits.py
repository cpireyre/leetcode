def countBits(n):
    def count(n):
        return 0 if not n else 1 + count(n & (n - 1))
    return [count(i) for i in range(n + 1)]
# Runtime: 160 ms, faster than 34.65% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.8 MB, less than 52.29% of Python3 online submissions for Counting Bits.


print(countBits(25))
