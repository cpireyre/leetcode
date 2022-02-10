from typing import *
from collections import Counter
from itertools import accumulate, chain, zip_longest
from operator import add

# It really bothers me that I can't take the state out of this function
def subarraySum(nums: List[int], k: int) -> int:
    c = Counter({0: 1})
    ret = 0
    for p in accumulate(nums, add):
        ret += c[p - k]
        c.update({p: 1})
    return ret
#Runtime: 600 ms, faster than 5.05% of Python3 online submissions for Subarray Sum Equals K.
#Memory Usage: 16.7 MB, less than 76.55% of Python3 online submissions for Subarray Sum Equals K.

nums = [1,1,1]
print(subarraySum(nums, 2)) # 2
nums = [1,2,3]
print(subarraySum(nums, 3)) # 2
nums = [1,2,1,2,1]
print(subarraySum(nums, 3)) # 4
nums = [6]
print(subarraySum(nums, 6)) # 1
nums = [1]
print(subarraySum(nums, 0)) # 0
