from itertools import pairwise, groupby
def numberOfArithmeticSlices(ns):
    return sum((n**2 + n) >> 1 for n in (len(list(g)) - 1 for _, g in groupby(high - low for low, high in pairwise(ns))) if n >= 1)
# Runtime: 55 ms, faster than 50.00% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.1 MB, less than 97.59% of Python3 online submissions for Arithmetic Slices.

ns = [1,2,3,4,5]
print(numberOfArithmeticSlices(ns))
