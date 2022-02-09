from collections import Counter
def findPairs(nums: List[int], k: int) -> int:
    if k == 0:
        return sum(count > 1 for count in Counter(nums).values())
    else:
        S = set(nums)
        return sum(s + k in S for s in S)
#Runtime: 96 ms, faster than 57.94% of Python3 online submissions for K-diff Pairs in an Array.
#Memory Usage: 15.9 MB, less than 40.07% of Python3 online submissions for K-diff Pairs in an Array.
