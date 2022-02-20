from functools import cache
@cache
def climbStairs(n):
    return n if n <= 2 else climbStairs(n - 1) + climbStairs(n - 2)
# Runtime: 39 ms, faster than 54.15% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14 MB, less than 65.79% of Python3 online submissions for Climbing Stairs.

for i in range(20):
    print((i, climbStairs(i)))
