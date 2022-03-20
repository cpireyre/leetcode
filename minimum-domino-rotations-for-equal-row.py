from itertools import product
def minDominoRotations(tops, bottoms):
    def count(tops, bottoms):
        ns = (1, 2, 3, 4, 5, 6)
        res = {n: (0, 0) for n in ns}
        for n, (top, bottom) in product(ns, zip(tops, bottoms)):
            x, y = res[n]
            x += (top == n)
            y += (bottom == n and top != n)
            res[n] = (x, y)
        return min((min(a, b) for a, b in res.values() if a + b == len(tops)), default=-1)
    return min(count(tops, bottoms), count(bottoms, tops))
# Runtime: 2673 ms, faster than 5.02% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 16.5 MB, less than 5.77% of Python3 online submissions for Minimum Domino Rotations For Equal Row.

tops    = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
print(minDominoRotations(tops, bottoms))
tops    = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
print(minDominoRotations(tops, bottoms))
tops    = [1,2,1,1,1,2,2,2]
bottoms = [2,1,2,2,2,2,2,2]
print(minDominoRotations(tops, bottoms))
