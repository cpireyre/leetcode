from typing import *
from itertools import accumulate
from operator import add

# Sophisticated / comprehensible version with map, acc, enum
# Runtime: 1604 ms, faster than 8.75% of Python3 online submissions for Contiguous Array.
# Memory Usage: 19.4 MB, less than 20.79% of Python3 online submissions for Contiguous Array.
#def findMaxLength(nums: List[int]) -> int:
#    maxLength = 0
#    prefixSums = {0: -1}
#    nums = map(lambda x: -1 if not x else 1, nums)
#    nums = accumulate(nums, add)
#    for index, prefixSum in enumerate(nums):
#        if prefixSum not in prefixSums:
#            prefixSums[prefixSum] = index
#        else:
#            maxLength = max(maxLength, index - prefixSums[prefixSum])
#    return maxLength

# Fast normie version doing everything by hand
# Runtime: 832 ms, faster than 95.54% of Python3 online submissions for Contiguous Array.
# Memory Usage: 19.5 MB, less than 17.33% of Python3 online submissions for Contiguous Array.
def findMaxLength(nums: List[int]) -> int:
    acc, i, m, l, d = 0, 0, 0, len(nums), {0: -1}
    while i < l:
        acc += -1 if not nums[i] else 1
        if acc not in d:
            d[acc] = i
        else:
            tmp = i - d[acc]
            m = tmp if tmp > m else m
        i += 1
    return m

nums = [0,0,0,0,0,1,1,1,1]
print(findMaxLength(nums))
nums = [0,1]
print(findMaxLength(nums))
nums = [1]
print(findMaxLength(nums))
nums = [0,1,0,1,0,1,0,1,0,1,0,1,0]
print(findMaxLength(nums))
