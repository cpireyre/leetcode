from itertools import combinations, product
def combinationSum(k, n):
    return [list(xs) for xs in combinations((1,2,3,4,5,6,7,8,9), k) if sum(xs) == n]
# Runtime: 53 ms, faster than 29.27% of Python3 online submissions for Combination Sum III.
# Memory Usage: 14 MB, less than 29.87% of Python3 online submissions for Combination Sum III.

k = 3
n = 7
print(combinationSum(k, n)) # [[1,2,4]]
k = 3
n = 9
print(combinationSum(k, n)) # [[1,2,6],[1,3,5],[2,3,4]]
k = 4
n = 1
print(combinationSum(k, n)) # []
for k, n in product((1,2,3,4,5,6,7), range(1, 61)):
    print(combinationSum(k, n))
