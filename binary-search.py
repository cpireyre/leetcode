def search(ns, n):
    l, pivot, r = 0, len(ns) // 2, len(ns) - 1
    if n in (ns[l], ns[pivot], ns[r]):
        return {
            ns[l]:l,
            ns[pivot]:pivot,
            ns[r]:r,
            }[n]
    while l < pivot < r:
        if n in (ns[l], ns[pivot], ns[r]):
            return {
                ns[l]:l,
                ns[pivot]:pivot,
                ns[r]:r,
                }[n]
        elif ns[l] < n < ns[pivot]:
            r, pivot = pivot, (pivot + l) // 2
        elif ns[pivot] < n < ns[r]:
            l, pivot = pivot, (r + pivot) // 2
        else:
            return -1
    return -1
# Runtime: 326 ms, faster than 50.88% of Python3 online submissions for Binary Search.
# Memory Usage: 15.6 MB, less than 27.89% of Python3 online submissions for Binary Search.

# ns, target = [-1, 0, 3, 5, 9, 12], 9
# ns, target = [-1,0,3,5,9,12], 2
# ns, target = [5], 5
ns, target = [-1,0,3,5,9,12], 13
print(search(ns, target))
