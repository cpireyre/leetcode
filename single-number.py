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
    i = 1
    while i < len(nums):
        nums[i] ^= nums[i - 1]
        i += 1
    return nums[-1]
# Runtime: 167 ms, faster than 60.44% of Python3 online submissions for Single Number.
# Memory Usage: 16.5 MB, less than 96.68% of Python3 online submissions for Single Number.
# lol lmao

nums = [4,1,2,1,2]
print(singleNumber(nums))
nums = [2,2,1]
print(singleNumber(nums))
nums = [1]
print(singleNumber(nums))
