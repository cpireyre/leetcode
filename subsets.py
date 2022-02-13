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

# Autie functional with list comprehensions:
def subsets(nums: List[int]) -> List[List[int]]:

    def byte2arr(byte):
        return [byte & (1 << i) for i in range(10)]

    def comp(nums, byte):
        return [num for num, bit in zip(nums, byte) if bit]

    return [comp(nums, byte2arr(i)) for i in range(2**len(nums))]
# Runtime: 46 ms, faster than 49.95% of Python3 online submissions for Subsets.
# Memory Usage: 14.1 MB, less than 95.43% of Python3 online submissions for Subsets.

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
