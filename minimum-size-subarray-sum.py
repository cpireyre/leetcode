from typing import *
def minSubArrayLen(target: int, nums: List[int]) -> int:
    l, left, right, acc, res = len(nums), 0, 0, 0, int(10e6)
    while right < l:
        while acc < target and right < l:
            acc += nums[right]
            right += 1
        while acc >= target and left < l:
            res = right - left if right - left < res else res
            if res == 1: return 1
            acc -= nums[left]
            left += 1
    return res if res < int(10e6) else 0
#Runtime: 64 ms, faster than 99.19% of Python3 online submissions for Minimum Size Subarray Sum.
#Memory Usage: 16.8 MB, less than 5.83% of Python3 online submissions for Minimum Size Subarray Sum.

target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))
target = 4
nums = [1,4,4]
print(minSubArrayLen(target, nums))
target = 11
nums = [1,1,1,1,1,1]
print(minSubArrayLen(target, nums))
