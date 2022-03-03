from itertools import pairwise, groupby
def numberOfArithmeticSlices(ns):
    arithmetics = (len(list(g)) - 1 for _, g in groupby(high - low for low, high in pairwise(ns)))
    return sum((n**2 + n) >> 1 for n in arithmetics if n >= 1)
# Runtime: 63 ms, faster than 31.69% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.2 MB, less than 53.58% of Python3 online submissions for Arithmetic Slices.

ns = [1,2,3,4,5]
print(numberOfArithmeticSlices(ns))
