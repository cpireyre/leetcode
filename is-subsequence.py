def isSubsequence(s, t):
    if not s:
        return True
    for c in s:
        idx = t.find(c)
        if idx == -1:
            return False
        t = t[idx + 1:]
    return True
# Runtime: 57 ms, faster than 28.94% of Python3 online submissions for Is Subsequence.
# Memory Usage: 14 MB, less than 73.22% of Python3 online submissions for Is Subsequence.

s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
