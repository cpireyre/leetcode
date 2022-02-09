from typing import *
from collections import Counter
def countKDifference(nums: List[int], k: int) -> int:
    c = Counter(nums)
    return sum(c[x] * c[x + k] for x in c.keys())
#Runtime: 79 ms, faster than 82.18% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
#Memory Usage: 13.8 MB, less than 92.95% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
