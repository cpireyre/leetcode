from typing import *

# Runtime: 82 ms, faster than 38.05% of Python3 online submissions for Remove Duplicates from Sorted Array II.
# Memory Usage: 13.8 MB, less than 96.82% of Python3 online submissions for Remove Duplicates from Sorted Array II.
def removeDuplicates(nums: List[int]) -> int:
    ref, l, i, count = nums[0], len(nums), 1, 1
    while i < l:
        while nums[i] == ref:
            if count < 2:
                i += 1
                count += 1
            else:
                del nums[i]
                l -= 1
            if i >= l: return l
        ref = nums[i]
        count = 0
    return l

def testRemoveDuplicates(nums):
    print(nums)
    print(removeDuplicates(nums))
    print(nums)

testRemoveDuplicates([1,1,1,2,2,3])
testRemoveDuplicates([0,0,1,1,1,1,2,3,3])
testRemoveDuplicates([1])
testRemoveDuplicates([1,1,1])
testRemoveDuplicates([1,2,2,2])
