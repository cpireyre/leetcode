from functools import reduce
from operator import lt
from itertools import combinations

def maximumSwap(num):
    def decomp(n):
        return [n] if n < 10 else decomp(n // 10) + [n % 10]
    def recomp(n):
        return reduce(lambda a,b: 10*a+b, n)
    
    ns = decomp(num)
    l = len(ns)
    for i in range(l):
        curr = ns[i] + 1
        kcurr = i
        for j in range(i + 1, l):
            if ns[j] >= curr:
                kcurr = j
                curr = ns[j]
        if kcurr > i:
            ns[i], ns[kcurr] = ns[kcurr], ns[i]
            return recomp(ns)
    return num
# Runtime: 59 ms, faster than 11.47% of Python3 online submissions for Maximum Swap.
# Memory Usage: 14 MB, less than 71.41% of Python3 online submissions for Maximum Swap

# print(maximumSwap(848748772))

def bruteforce(n):
    def decomp(n):
        return [n] if n < 10 else decomp(n // 10) + [n % 10]
    xs = decomp(n)
    res = [reduce(lambda a,b: 10*a+b, xs)]
    for x, y in combinations(range(len(xs)), 2):
        curr = list(xs)
        curr[x], curr[y] = curr[y], curr[x]
        res.append(reduce(lambda a,b: 10*a+b, curr))
    return max(res)

from numpy.random import randint
for _ in range(100000):
    n = randint(10e8)
    b = bruteforce(n)
    m = maximumSwap(n)
    if m != b:
        print("%d <- %d -> %d" % (bruteforce(n), n, maximumSwap(n)))
