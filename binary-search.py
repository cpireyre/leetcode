# this is not good code, but; play stupid games, win stupid prizes.
def search(ns, n):
    l, r = 0, len(ns) - 1
    while l < ((l+r)>>1) < r:
        l, r = (l, (l+r)>>1) if ns[(l+r)>>1] > n else ((l+r)>>1, r)
    return next((i for i in (l, r) if ns[i] == n), -1)
# Runtime: 244 ms, faster than 92.47% of Python3 online submissions for Binary Search.
# Memory Usage: 15.4 MB, less than 76.86% of Python3 online submissions for Binary Search.

ns, target = [-1, 0, 3, 5, 9, 12], 9 # 4
print(search(ns, target))
ns, target = [-1,0,3,5,9,12], 2 # -1
print(search(ns, target))
ns, target = [5], 5 # 0
print(search(ns, target))
ns, target = [-1,0,3,5,9,12], 13 # -1
print(search(ns, target))
ns, target = [2,5], 5 # 1
print(search(ns, target))
