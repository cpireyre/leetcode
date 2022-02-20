def removeDuplicates(ns):
    i = 0
    while i < len(ns) - 1:
        while i < len(ns) - 1 and ns[i+1] == ns[i]:
            del ns[i]
        i += 1
    return len(ns)
# Runtime: 209 ms, faster than 13.17% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.6 MB, less than 38.45% of Python3 online submissions for Remove Duplicates from Sorted Array.

print(removeDuplicates([1,2,3]))
print(removeDuplicates([1,1,1]))
print(removeDuplicates([2,2]))
print(removeDuplicates([5,5,5,5,5,5,5,6]))
print(removeDuplicates([6,7,8,8,8,8,8,9]))
