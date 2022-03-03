from itertools import pairwise, groupby
def checkArithmeticSubarrays(ns, l, r):

    def all_equal(iterable):
        g = groupby(iterable)
        return next(g, True) and not next(g, False)

    def isArithmetic(ns):
        return all_equal(high - low for low, high in pairwise(ns))

    return [isArithmetic(sorted(ns[l : r + 1])) for l, r in zip(l, r)]
# Runtime: 322 ms, faster than 36.79% of Python3 online submissions for Arithmetic Subarrays.
# Memory Usage: 14.1 MB, less than 96.19% of Python3 online submissions for Arithmetic Subarrays.

nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]

print(checkArithmeticSubarrays(nums, l, r))
