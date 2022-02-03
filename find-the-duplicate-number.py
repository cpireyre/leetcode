from typing import *
# Runtime: 2818 ms, faster than 5.03% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 28.8 MB, less than 25.49% of Python3 online submissions for Find the Duplicate Number.
def findDuplicate(nums: List[int]) -> int:
    acc = 0
    for n in nums:
        mask = 1 << n
        if mask & acc:
            return n
        else:
            acc |= mask
