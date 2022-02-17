from typing import *

# Stupid BFS ver:
# def combinationSum(candidates: List[int], target: int) -> List[List[int]]:

#     ans = []
#     cs = [[c] for c in candidates]
#     while cs:
#         _next = []
#         for c in cs:
#             if sum(c) == target:
#                 ans += [c]
#             else:
#                 _next += (
#                     c + [n] for n in candidates if n >= c[-1] and n + sum(c) <= target
#                 )
#         cs = _next
#     return ans
# Runtime: 133 ms, faster than 34.96% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.3 MB, less than 38.91% of Python3 online submissions for Combination Sum.

# Actual backtracking ver
def combinationSum(candidates, target):
    ans = []
    def backtrack(target, res):
        nonlocal ans
        if target == 0: ans.append(res)
        else:
            m = 0 if not res else res[-1]
            for x in (c for c in candidates if c <= target and c >= m):
                backtrack(target - x, res + [x])
    backtrack(target, [])
    return ans
# Runtime: 64 ms, faster than 90.83% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.9 MB, less than 87.78% of Python3 online submissions for Combination Sum.

candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
candidates = [2, 3, 5]
target = 8
print(combinationSum(candidates, target))
candidates = [3]
target = 8
print(combinationSum(candidates, target))
candidates = [3]
target = 3
print(combinationSum(candidates, target))
