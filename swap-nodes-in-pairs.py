from typing import *
from ListNodes import *
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    elif not head.next:
        return head
    elif _next := head.next:
        head.next = swapPairs(_next.next)
        _next.next = head
        return _next
# Runtime: 64 ms, faster than 8.37% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 13.9 MB, less than 90.54% of Python3 online submissions for Swap Nodes in Pairs.

def test(func, head):
    h = fromArray(head)
    res = func(h)
    return toArray(res)

head = [1, 2]  # [2,1]
print(test(swapPairs, head))
head = [1, 2, 3]  # [2,1,3]
print(test(swapPairs, head))
head = [1, 2, 3, 4]  # [2,1,4,3]
print(test(swapPairs, head))
head = []  # []
print(test(swapPairs, head))
head = [1]  # [1]
print(test(swapPairs, head))
head = [1,2,3,4,5] # [2,1,4,3,5]
print(test(swapPairs, head))
