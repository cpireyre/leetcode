from ListNodes import *
from typing import *


def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    ptrs = []
    headPtr = head
    k -= 1
    while headPtr:
        ptrs.append(headPtr)
        headPtr = headPtr.next
    l = len(ptrs)
    if l > 1 and k < l and ptrs[k].val ! ptrs[-(k+1)].val:
        ptrs[k].val, ptrs[-k - 1].val = ptrs[-k - 1].val, ptrs[k].val
    return head
# Runtime: 1112 ms, faster than 74.19% of Python3 online submissions for Swapping Nodes in a Linked List.
# Memory Usage: 48.4 MB, less than 83.86% of Python3 online submissions for Swapping Nodes in a Linked List.


head = [1, 2, 3, 4, 5]
k = 2
print(testListFunc(swapNodes, head, k))
head = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
k = 5
print(testListFunc(swapNodes, head, k))
head = [1]
k = 1
print(testListFunc(swapNodes, head, k))
head = [1, 2]
k = 1
print(testListFunc(swapNodes, head, k))
head = [1, 2, 3, 4, 5]
k = 1
print(testListFunc(swapNodes, head, k))
head = [1,2,3]
k = 2
print(testListFunc(swapNodes, head, k))
