from collections import Counter


def minDominoRotations(tops, bottoms):
    def pivot(tops, bottoms):
        count, n = max((n, count) for count, n in Counter(tops).items())
        mustFlip = len(tops) - count
        canFlip = sum(a != n and b == n for a, b in zip(tops, bottoms))
        return mustFlip if canFlip >= mustFlip else -1

    t, b = pivot(tops, bottoms), pivot(bottoms, tops)
    return max(t, b) if t == -1 or b == -1 else min(t, b)
# Runtime: 1633 ms, faster than 38.22% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 15 MB, less than 77.02% of Python3 online submissions for Minimum Domino Rotations For Equal Row.


tops = [2, 1, 2, 4, 2, 2]
bottoms = [5, 2, 6, 2, 3, 2]
print(minDominoRotations(tops, bottoms))
tops = [3, 5, 1, 2, 3]
bottoms = [3, 6, 3, 3, 4]
print(minDominoRotations(tops, bottoms))
tops = [1, 2, 1, 1, 1, 2, 2, 2]
bottoms = [2, 1, 2, 2, 2, 2, 2, 2]
print(minDominoRotations(tops, bottoms))
tops = [1, 1, 1, 1, 1, 1, 1]
bottoms = [1, 1, 1, 1, 1, 1, 1]
print(minDominoRotations(tops, bottoms))
tops = [1, 2, 3, 4, 5]
bottoms = [6, 6, 6, 6, 6]
print(minDominoRotations(tops, bottoms))
