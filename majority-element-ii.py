from collections import Counter
def majorityElement(ns):
    return [n for n, c in Counter(ns).most_common() if c > (len(ns) // 3)]
# Runtime: 126 ms, faster than 68.16% of Python3 online submissions for Majority Element II.
# Memory Usage: 15.4 MB, less than 21.24% of Python3 online submissions for Majority Element II.

ns = [1,2,1]
print(majorityElement(ns))
