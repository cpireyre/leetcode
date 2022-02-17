# Actual backtrack ver
def permute(nums):
    """Given an array nums of distinct integers, return all the possible permutations."""

    ans = []

    def helper(nums, res, ans):
        if len(set(res)) < len(res):
            return []
        if not nums:
            ans += [res]
        xs = [x for x in nums]
        for x in xs:
            P = nums.copy()
            P.remove(x)
            xs = helper(P, res + [x], ans)

    helper(nums, [], ans)
    return ans
# Runtime: 55 ms, faster than 49.35% of Python3 online submissions for Permutations.
# Memory Usage: 14.1 MB, less than 72.79% of Python3 online submissions for Permutations.


print(permute([1, 2, 3]))
