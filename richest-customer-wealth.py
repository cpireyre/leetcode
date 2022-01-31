from typing import *

#Runtime: 68 ms, faster than 42.35% of Python3 online submissions for Richest Customer Wealth.
#Memory Usage: 13.9 MB, less than 99.25% of Python3 online submissions for Richest Customer Wealth.
def maximumWealth(accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
# What on earth did everyone else do but this, lol

# Somebody on the forum claims this is faster:
# return (most := 0) or [(most := wealth) for wealth in [sum(row) for row in accounts] if wealth > most][-1]
# But not the case for me when I run it on Leetcode (100+ms)
