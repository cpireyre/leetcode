from itertools import pairwise, groupby
def canMakeArithmeticProgression(ns):
    def all_equal(iterable):
        g = groupby(iterable)
        return next(g, True) and not next(g, False)

        return all_equal(high - low for low, high in pairwise(sorted(ns)))
# Runtime: 46 ms, faster than 71.03% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
# Memory Usage: 14 MB, less than 52.92% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
