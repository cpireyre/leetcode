from itertools import product
from collections import Counter
def minDominoRotations(tops, bottoms):
    def count(tops, bottoms):
        count, val = max((v, k) for k, v in Counter(tops).items())
        if count + sum(a != val and b == val for a, b in zip(tops, bottoms)) >= len(tops):
            return len(tops) - count
        else:
            return -1
    t, b = count(tops, bottoms), count(bottoms, tops)
    if t == -1 or b == -1:
        return t if b == -1 else b
    else:
        return min(t, b)
# Runtime: 1216 ms, faster than 80.89% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 15.1 MB, less than 77.02% of Python3 online submissions for Minimum Domino Rotations For Equal Row.

tops    = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
print(minDominoRotations(tops, bottoms))
tops    = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
print(minDominoRotations(tops, bottoms))
tops    = [1,2,1,1,1,2,2,2]
bottoms = [2,1,2,2,2,2,2,2]
print(minDominoRotations(tops, bottoms))
tops    = [1,1,1,1,1,1,1]
bottoms = [1,1,1,1,1,1,1]
print(minDominoRotations(tops, bottoms))
tops    = [1,2,3,4,5]
bottoms = [6,6,6,6,6]
print(minDominoRotations(tops, bottoms))
