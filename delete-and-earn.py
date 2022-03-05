from pprint import pprint
from collections import Counter

# slow but concise, also i kind of stole this from the forum
def deleteAndEarn(ns):
    prev, res, ns = 0, 0, Counter({n: n * ns.count(n) for n in ns})
    for n in sorted(ns.keys()):
        prev, res = res, max(prev + ns[n], res) if ns[n - 1] > 0 else res + ns[n]
    return res
# Runtime: 552 ms, faster than 5.02% of Python3 online submissions for Delete and Earn.
# Memory Usage: 14.3 MB, less than 65.62% of Python3 online submissions for Delete and Earn.

nums = [2, 2, 3, 3, 3, 4]
print(deleteAndEarn(nums))
nums = [3, 4, 2]
print(deleteAndEarn(nums))
nums = [8, 10, 4, 9, 1, 3, 5, 9, 4, 10]
print(deleteAndEarn(nums))
nums = [3,7,10,5,2,4,8,9,9,4,9,2,6,4,6,5,4,7,6,10]
print(deleteAndEarn(nums))
nums = [8,7,3,8,1,4,10,10,10,2]
print(deleteAndEarn(nums))
