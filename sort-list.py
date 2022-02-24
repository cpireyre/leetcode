from ListNodes import *

def mergeTwoLists(list1, list2):
    if not list1 or not list2:
        return list1 or list2
    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

def sortList(head):
    if not head or not head.next:
        return head
    elif not head.next.next:
        tmp = head.next
        head.next = None
        return mergeTwoLists(head, tmp)
    else:
        _mid, _end = head, head
        while _end and _end.next:
            _mid = _mid.next
            _end = _end.next.next
        tmp = _mid.next
        _mid.next = None
        head = sortList(head)
        _mid.next = sortList(tmp)
        return mergeTwoLists(head, _mid.next)

nums = [3,1,2]
# nums = [4,3]
xs = testListFunc(sortList, nums)
print(xs)
