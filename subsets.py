from typing import *
from itertools import compress
# Cardinality of superset: 2**len(nums)
def subsets(nums: List[int]) -> List[List[int]]:

    def byte2arr(byte):
        return [] if byte == 0 else [byte % 2] + byte2arr(byte // 2)

    return list(
            map(lambda b: list(compress(nums, b)), 
                map(byte2arr, range(2**len(nums)))))
#Runtime: 48 ms, faster than 46.37% of Python3 online submissions for Subsets.
#Memory Usage: 14.2 MB, less than 82.34% of Python3 online submissions for Subsets.

#from sys import argv
#print(byte2arr(int(argv[1])))

nums = [1,2,3]
print(subsets(nums))
nums = [0]
print(subsets(nums))
