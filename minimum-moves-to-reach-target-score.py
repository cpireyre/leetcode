def minMoves(target, maxDoubles):
    res = 0
    while maxDoubles and target != 1:
        res += 1 + (target & 1)
        maxDoubles -= 1
        target >>= 1
    return res + target - 1
# Runtime: 32 ms, faster than 87.38% of Python3 online submissions for Minimum Moves to Reach Target Score.
# Memory Usage: 14 MB, less than 89.30% of Python3 online submissions for Minimum Moves to Reach Target Score.
