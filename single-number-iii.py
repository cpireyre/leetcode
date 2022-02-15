from collections import Counter
def singleNumber(nums):
    return [(c := Counter(nums).most_common())[-1][0], c[-2][0]]
# Runtime: 82 ms, faster than 56.20% of Python3 online submissions for Single Number III.
# Memory Usage: 16.2 MB, less than 22.36% of Python3 online submissions for Single Number III.
nums = [1,2,1,3,2,5]
print(singleNumber(nums))
