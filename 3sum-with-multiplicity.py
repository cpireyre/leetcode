from collections import Counter
from itertools import combinations
from math import factorial

def nchoosek(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def threeSumMulti(arr, target):
    c = Counter(arr)
    ret = 0
    for k, v in c.items():
        if k * 3 == target and v >= 3:
            ret += nchoosek(v, 3)
    for (ka, va), (kb, vb) in combinations(c.items(), 2):
        if vb >= 2 and ka + 2 * kb == target:
            ret += va * nchoosek(vb, 2)
        elif va >= 2 and 2 * ka + kb == target:
            ret += vb * nchoosek(va, 2)
    for (ka, va), (kb, vb), (kc, vc) in combinations(c.items(), 3):
        if ka + kb + kc == target:
            ret += va * vb * vc
    return ret % (10**9 + 7)
# Runtime: 288 ms, faster than 43.60% of Python3 online submissions for 3Sum With Multiplicity.
# Memory Usage: 14 MB, less than 92.44% of Python3 online submissions for 3Sum With Multiplicity.

arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
print(threeSumMulti(arr, target)) # 20
arr = [1,1,2,2,2,2]
target = 5
print(threeSumMulti(arr, target)) # 12
arr = [0,0,0]
target = 0
print(threeSumMulti(arr, target)) # 1
arr = [2,1,3]
target = 6
print(threeSumMulti(arr, target)) # 1
arr = [1,2,3,3,1]
target = 5
print(threeSumMulti(arr, target)) # 2
