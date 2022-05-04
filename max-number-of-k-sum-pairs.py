from collections import Counter
def maxOperations(nums, k):
    c = Counter(nums)
    return sum(min(c[n], c[k - n]) for n in c.keys()) // 2
# Runtime: 733 ms, faster than 76.12% of Python3 online submissions for Max Number of K-Sum Pairs.
# Memory Usage: 27.1 MB, less than 54.91% of Python3 online submissions for Max Number of K-Sum Pairs.

nums = [1,2,3,4]
k = 5
print(maxOperations(nums, k))
nums = [3,1,3,4,3]
k = 6
print(maxOperations(nums, k))
