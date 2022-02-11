from typing import *
def minWindow(s: str, t: str) -> str:
    l, left, right, res, ct = len(s), 0, len(t), s, Counter(t)
    if not (ct <= Counter(s)): return ""
    acc = Counter(s[left:right])
    while right < l:
        while not (ct <= acc) and right < l:
            acc.update({s[right]: 1})
            right += 1
        while ct <= acc and left < right:
            res = s[left:right] if right - left < len(res) else res
            acc.update({s[left]: -1})
            left += 1
    return res
#Runtime: 1219 ms, faster than 5.00% of Python3 online submissions for Minimum Window Substring.
#Memory Usage: 14.7 MB, less than 95.87% of Python3 online submissions for Minimum Window Substring.

print(minWindow("ab", "a"))
print(minWindow("a", "a"))
print(minWindow("abc", "cba"))
