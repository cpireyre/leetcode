# no-thoughts-head-empty BFS ver:
from collections import deque
def minMoves(target, maxDoubles):
    res = 0
    while target != 1:
        if maxDoubles == 0:
            return res + target - 1
        if target & 1:
            target -= 1
        else:
            target >>= 1
            maxDoubles -= 1
        res += 1
    return res
# Runtime: 36 ms, faster than 72.37% of Python3 online submissions for Minimum Moves to Reach Target Score.
# Memory Usage: 13.9 MB, less than 89.30% of Python3 online submissions for Minimum Moves to Reach Target Score.

from sys import argv
print(minMoves(int(argv[1]), int(argv[2])))
