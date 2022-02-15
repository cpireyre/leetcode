from collections import Counter
def singleNumber(nums):
    return Counter(nums).most_common()[-1][0]
#Runtime: 145 ms, faster than 68.35% of Python3 online submissions for Single Number.
#Memory Usage: 16.9 MB, less than 6.05% of Python3 online submissions for Single Number.

nums = [4,1,2,1,2]
print(singleNumber(nums))
nums = [2,2,1]
print(singleNumber(nums))
nums = [1]
print(singleNumber(nums))
