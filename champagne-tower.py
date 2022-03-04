from itertools import pairwise, islice
from pprint import pprint

# boring old iterate on the successor function code
def champagneTower(poured, query_row, query_glass):
    def iterate(f, x):
        while True:
            yield x
            x = f(x)

    def nth(iterable, n, default=None):
        return next(islice(iterable, n, None), default)

    def succ(ns):
        return [(left > 1) * ((left - 1) / 2) + (right > 1) * ((right - 1) / 2)
            for left, right in pairwise([0] + ns + [0])]

    return min(1.0, nth(iterate(succ, [poured]), query_row)[query_glass])
# Runtime: 177 ms, faster than 48.54% of Python3 online submissions for Champagne Tower.
# Memory Usage: 13.8 MB, less than 95.15% of Python3 online submissions for Champagne Tower.
# not super fast but i hate mutating arrays in place repeatedly and refuse to write loops, so


pprint(champagneTower(100000009, 33, 17))
