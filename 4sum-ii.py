# Compute all the sums of nums1 + num2 and put them in a hash map
# Do the same with nums3 + nums4
# Iterate through one hash map looking for the key that will cancel out in
# the other hash map
# O(n^2) time O(n^2) space

from typing import *
from collections import Counter
# Runtime: 552 ms, faster than 99.58% of Python3 online submissions for 4Sum II.
# Memory Usage: 15.1 MB, less than 11.19% of Python3 online submissions for 4Sum II
def fourSumCount(nums1: List[int], nums2: List[int], \
        nums3: List[int], nums4: List[int]) -> int:
    sums12 = Counter([x+y for x in nums1 for y in nums2])
    sums34 = Counter([x+y for x in nums3 for y in nums4])
    return sum((sums12[s] * sums34[-s] for s in sums12.keys()))

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(fourSumCount(nums1, nums2, nums3, nums4))
nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]
print(fourSumCount(nums1, nums2, nums3, nums4))
