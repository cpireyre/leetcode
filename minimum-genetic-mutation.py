from typing import *
from itertools import product
def minmutation(start: str, end: str, bank: list[str]) -> int:

    def isValidMutation(s1, s2):
        diff = 0
        for i in range(8):
            if s1[i] != s2[i]: diff += 1
        return diff == 1

    seen, q, res = set(), set(), 0
    q.add(start)
    while q:
        if end in q: return res
        _next = set()
        for c, u in product(q, bank):
            if u not in seen and isValidMutation(c, u):
                _next.add(u)
                seen.add(u)
        q = _next
        res += 1
    return -1
#Runtime: 28 ms, faster than 91.08% of Python3 online submissions for Minimum Genetic Mutation.
#Memory Usage: 13.9 MB, less than 97.81% of Python3 online submissions for Minimum Genetic Mutation.

start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
print(minmutation(start, end, bank))
