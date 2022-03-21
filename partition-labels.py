from collections import deque
def partitionLabels(s):
    halves = lambda s: ((s[0:i], s[i:]) for i in range(1, len(s)))
    disjoint = lambda s, t: not(set(t) & set(s))
    partition = lambda s: next((p for p in halves(s) if disjoint(*p)), None)
    q = partition(s)
    if not q:
        return [len(s)]
    Q = deque(list(q))
    res = []
    while Q:
        curr = Q.popleft()
        if split := partition(curr):
            Q.extend(split)
        else:
            res.append(curr)
    return [len(c) for c in res]
# Runtime: 255 ms, faster than 5.04% of Python3 online submissions for Partition Labels.
# Memory Usage: 13.9 MB, less than 36.30% of Python3 online submissions for Partition Labels.


s = "ababcbacadefegdehijhklij"
# s = "aabbc"
# s = "abcddcba"
print(partitionLabels(s))
