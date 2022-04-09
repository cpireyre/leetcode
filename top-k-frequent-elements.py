from collections import Counter
def topKFrequent(nums, k):
    return [n for n, _ in Counter(nums).most_common(k)]
# Runtime: 159 ms, faster than 36.51% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.5 MB, less than 91.71% of Python3 online submissions for Top K Frequent Elements.

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
nums = [1]
k = 1
print(topKFrequent(nums, k))
