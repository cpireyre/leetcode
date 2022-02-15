# Ez Counter ver
# from collections import Counter
# def singleNumber(nums):
    # return Counter(nums).most_common()[-1][0]
# Runtime: 63 ms, faster than 75.53% of Python3 online submissions for Single Number II.
# Memory Usage: 16.1 MB, less than 37.20% of Python3 online submissions for Single Number II.

# Bit frequency mod 3 ver
from functools import reduce
def singleNumber(nums):

    def byte2index(byte):
        return (31 - i for i in range(32) if byte & (1 << i))

    res = bytearray(32)
    sign = 0
    while nums:
        pop = nums.pop()
        if pop < 0: sign += 1
        for idx in byte2index(abs(pop)):
            res[idx] = (res[idx] + 1) % 3

    sign = -1 if (sign % 3) else 1
    return sign * reduce(lambda a, b: 2 * a + b, res)
# Turns out Python doesn't do signed bits as such...
# it must be handled somewhere during int boxing and unboxing
# Runtime: 304 ms, faster than 14.54% of Python3 online submissions for Single Number II.
# Memory Usage: 15.8 MB, less than 55.80% of Python3 online submissions for Single Number II.
    

print(singleNumber([2,2,3,2]))
nums = [0,1,0,1,0,1,99]
print(singleNumber(nums))
nums = [-1, -1, -1, 2]
print(singleNumber(nums))
nums = [-2,-2,1,1,4,1,4,4,-4,-2]
print(singleNumber(nums))
