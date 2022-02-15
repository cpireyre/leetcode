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
# def singleNumber(nums):
#     return 0 if not nums else nums[0] ^ singleNumber(nums[1:])
# Memory limit exceeded lol

# Primitive bare metal ver
def singleNumber(nums):
    acc = 0
    for n in nums:
        acc ^= n
    return acc
# Runtime: 241 ms, faster than 28.20% of Python3 online submissions for Single Number.
# Memory Usage: 16.7 MB, less than 30.94% of Python3 online submissions for Single Number.
# Where is all that memory going???

# Disgusting mutate everything in place ver
def singleNumber(nums):
    while len(nums) > 1: nums[0] ^= nums.pop()
    return nums[0]
# Runtime: 183 ms, faster than 54.51% of Python3 online submissions for Single Number.
# Memory Usage: 16 MB, less than 99.46% of Python3 online submissions for Single Number.

def singleNumber(nums):

nums = [4,1,2,1,2]
print(singleNumber(nums))
nums = [2,2,1]
print(singleNumber(nums))
nums = [1]
print(singleNumber(nums))
