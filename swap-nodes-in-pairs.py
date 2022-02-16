from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def listMap(self, func):
        func(self.val)
        if self.next:
            self.next.listMap(func)


def fromArray(nums):
    if nums:
        ret = ListNode(nums[0])
        tmp = ret
        for n in nums[1:]:
            tmp.next = ListNode(n)
            tmp = tmp.next
        return ret
    else:
        return []


def toArray(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


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
