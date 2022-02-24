def mergeTwoLists(list1, list2):
    if not list1 or not list2:
        return list1 or list2
    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
# Runtime: 39 ms, faster than 81.71% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14 MB, less than 55.55% of Python3 online submissions for Merge Two Sorted Lists.
