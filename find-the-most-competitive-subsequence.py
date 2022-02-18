def mostCompetitive(nums, k):
    res = []
    k = len(nums) - k
    for n in nums:
        while res and k and n < res[-1]:
            res.pop()
            k -= 1
        res.append(n)
    return res[0:len(res)-k]
# Runtime: 1828 ms, faster than 53.47% of Python3 online submissions for Find the Most Competitive Subsequence.
# Memory Usage: 27.1 MB, less than 66.76% of Python3 online submissions for Find the Most Competitive Subsequence.

print(mostCompetitive([3,5,2,6], 2))
print(mostCompetitive([2,4,3,3,5,4,9,6], 4))
print(mostCompetitive([2,1], 1))
print(mostCompetitive([9,8,7,6,5,4,3,2,1], 1))
