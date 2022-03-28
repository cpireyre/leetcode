def findMin(ns):
    if len(ns) == 1 or ns[0] < ns[-1]:
        return ns[0]

    def recur(l, r):
        if ns[l] > ns[l + 1]:
            return ns[l + 1]
        else:
            return recur((l+r)>>1, r) if ns[l] < ns[(l+r)>>1] else recur(l, (l+r)>>1)

    return recur(0, len(ns) - 1)
# Runtime: 32 ms, faster than 99.67% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.3 MB, less than 28.43% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

    
ns = [3, 4, 5, 1, 2] # 1
print(findMin(ns))
ns = [4,5,6,7,0,1,2] # 0
print(findMin(ns))
ns = [11,13,15,17] # 11
print(findMin(ns))
ns = [2] # 2
print(findMin(ns))
ns = [2, 1] # 1
print(findMin(ns))
ns = [1, 2] # 1
print(findMin(ns))
ns = [4,5,1,2,3] # 1
print(findMin(ns))
