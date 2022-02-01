from collections import deque

# Runtime: 161 ms, faster than 22.84% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14 MB, less than 96.31% of Python3 online submissions for Longest Substring Without Repeating Characters.
def lengthOfLongestSubstring(s):

    q, res = deque(), 0

    for c in s:
        if c not in q:
            q.append(c)
        else:
            res = max(res, len(q))
            while c in q:
                q.popleft()
            q.append(c)

    return max(res, len(q))

from sys import argv
print(lengthOfLongestSubstring(argv[1]))
