from collections import Counter
# Counter ver
# def singleNumber(nums):
#     return Counter(nums).most_common()[-1][0]
#Runtime: 145 ms, faster than 68.35% of Python3 online submissions for Single Number.
#Memory Usage: 16.9 MB, less than 6.05% of Python3 online submissions for Single Number.

# reduce XOR ver I stole from Leetcode
# from functools import reduce
# def singleNumber(nums):
#     return reduce(lambda a, b: a^b, nums)
# Runtime: 195 ms, faster than 49.33% of Python3 online submissions for Single Number.
# Memory Usage: 16.8 MB, less than 30.94% of Python3 online submissions for Single Number.

# Meme tail recurse ver
def singleNumber(nums):
    return 0 if not nums else nums[0] ^ singleNumber(nums[1:])
# Memory limit exceeded lol

nums = [4,1,2,1,2]
print(singleNumber(nums))
nums = [2,2,1]
print(singleNumber(nums))
nums = [1]
print(singleNumber(nums))
