from typing import *
# from itertools import compress
# Cardinality of superset: 2**len(nums)
# Autie functional ver
# def subsets(nums: List[int]) -> List[List[int]]:

#     def byte2arr(byte):
#         return [] if byte == 0 else [byte % 2] + byte2arr(byte // 2)

#     return list(
#             map(lambda b: list(compress(nums, b)), 
#                 map(byte2arr, range(2**len(nums)))))
#Runtime: 48 ms, faster than 46.37% of Python3 online submissions for Subsets.
#Memory Usage: 14.2 MB, less than 82.34% of Python3 online submissions for Subsets.

# One liner with streamlined bit manipulation ver
def subsets(nums: List[int]) -> List[List[int]]:
    return [[nums[i] for i in [0,1,2,3,4,5,6,7,8,9] if byte & (1 << i)] for byte in range(2**len(nums))]
# Runtime: 36 ms, faster than 79.63% of Python3 online submissions for Subsets.
# Memory Usage: 14.2 MB, less than 82.34% of Python3 online submissions for Subsets.
# Big variance though ngl but it's a small problem

# Normie fast ver:
# def subsets(nums: List[int]) -> List[List[int]]:
    # res = []
    # comp = compress
    # li = list
    # for i in range(2**len(nums)):
    #     byte = []
    #     while i:
    #         byte.append(i % 2)
    #         i >>= 1
    #     res.append(li(comp(nums, byte)))
    # return res
# Runtime: 61 ms, faster than 61.13% of Python3 online submissions for Subsets.
# Memory Usage: 14.1 MB, less than 82.34% of Python3 online submissions for Subsets.
# I don't understand why this is slower than average but OK

# Cheese combinations ver
# from itertools import combinations
# def subsets(nums: List[int]) -> List[List[int]]:
#     res = []
#     for i in range(len(nums) + 1):
#         res.append([c for c in combinations(nums, i)])
#     return res
# combinations returns tuples tho :/


# from sys import argv
# print(byte2arr(int(argv[1])))

nums = [1,2,3]
print(subsets(nums))
nums = [0]
print(subsets(nums))
