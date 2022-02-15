# Ez Counter ver
from collections import Counter
def singleNumber(nums):
    return Counter(nums).most_common()[-1][0]
# Runtime: 63 ms, faster than 75.53% of Python3 online submissions for Single Number II.
# Memory Usage: 16.1 MB, less than 37.20% of Python3 online submissions for Single Number II.
