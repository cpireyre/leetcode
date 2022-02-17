from itertools import combinations
# lol
# def combine(n, k):
#     """Given two integers n and k, return all possible combinations of
#     k numbers out of the range [1, n]."""
#     return [list(p) for p in combinations(list(range(1, n + 1)), k)]
# Runtime: 134 ms, faster than 84.32% of Python3 online submissions for Combinations.
# Memory Usage: 15.9 MB, less than 43.72% of Python3 online submissions for Combinations.

from itertools import accumulate
from operator import lt
def combine(n, k):

    ans = []
    def backtrack(n, k, res):
        nonlocal ans
        if not all(accumulate(res, lt)): return
        if k == 0: ans.append(res)
        for x in [x for x in range(1, n+1)]:
            backtrack(n-1, k-1, [x] + res)

    backtrack(n, k, [])
    return ans
# Runtime: 7211 ms, faster than 5.01% of Python3 online submissions for Combinations.
# Memory Usage: 16.1 MB, less than 15.27% of Python3 online submissions for Combinations.

print(combine(4, 2))
print(combine(4, 3))
print(combine(4, 1))
# print(combine(1, 1, []))
