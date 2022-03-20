from collections import Counter


def minDominoRotations(tops, bottoms):
    c = Counter(a for a, b in zip(tops, bottoms) if a == b)
    t, b = Counter(tops) - c, Counter(bottoms) - c
    return min(
        (
            min(b[n], t[n])
            for n in (1, 2, 3, 4, 5, 6)
            if t[n] + b[n] == len(tops) - c[n]
        ),
        default=-1,
    )
# Runtime: 1216 ms, faster than 80.89% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
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
