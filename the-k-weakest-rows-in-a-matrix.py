from itertools import islice


def kWeakestRows(M, k):
    return [
        i
        for i, _ in islice(
            sorted(enumerate(map(sum, M)), key=lambda t: (t[1], t[0])), 0, k
        )
    ]
# Runtime: 248 ms, faster than 5.03% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.2 MB, less than 90.64% of Python3 online submissions for The K Weakest Rows in a Matrix.


mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
]
k = 3
print(kWeakestRows(mat, k))
mat = [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]
k = 2
print(kWeakestRows(mat, k))
