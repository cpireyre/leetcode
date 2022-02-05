from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def listMap(self, func):
        func(self.val)
        if self.next:
            self.next.listMap(func)

    def __lt__(self, other): # necessary for heapify to work
        return self.val < other.val

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

from heapq import *
# For some reason this heap API isn't OO like the other Python data structures,
# so all the heap functions take a heap as their first argument
# instead of being methods. I mean, like, good I guess, but, inconsistent.

# This solution is correct but won't run on Leetcode because they don't allow
# you to define __lt__ in the ListNode class they provide 🙄
#def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#    h = [(node, node.next) for node in lists]
#    if not h:
#        return []
#    heapify(h)
#    out = ListNode(h[0][0].val)
#    first = out
#    while len(h) > 1:
#        s = heappop(h)
#        out.next = ListNode(s[0].val)
#        out = out.next
#        if s[1]:
#            heappush(h, (s[1], s[1].next))
#    out.next = h[0][0]
#    return first

# Runtime: 101 ms, faster than 84.19% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.7 MB, less than 79.64% of Python3 online submissions for Merge k Sorted Lists.
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    res = ListNode() # no need to compute first element, just use the default
    h = [(node.val, index, node) for index, node in enumerate(lists) if node]
    if not h:
        return None
    heapify(h)
    cur = res
    while len(h) > 1:
        _, i, node = heappop(h) # neat destructuring here
        if node.next:
            heappush(h, (node.next.val, i, node.next))
        cur.next = node # rerouting
        cur = node # preparing to reroute next time
    cur.next = h[0][2] # Short-circuit
    return res.next # next because the first one was a dud

l1 = fromArray([1,4,5,7,8,9,10])
l2 = fromArray([1,3,4])
l3 = fromArray([2,6])
lists = [l3,l2,l1]
mergeKLists(lists).listMap(print)

#l1 = fromArray([])
#l2 = fromArray([])
#l3 = fromArray([])
#lists = [[],[],[]]
#mergeKLists(lists).listMap(print)

#class Solution:
#    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
