# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next = b
b.next = c
c.next = d
d.next = b

e = ListNode(1)
f = ListNode(2)
e.next = f
f.next = e

g = ListNode(1)

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        curr = head
        addresses = set()
        while curr != None:
            if id(curr) in addresses:
                return curr
            else:
                addresses.add(id(curr))
            curr = curr.next
        return None

    print(detectCycle(a, a).val)
    print(detectCycle(e, e).val)
    print(detectCycle(g, g))
    print(detectCycle(g, None))
    print(detectCycle(None, g))
# s = set('henlol')
# print(s)

# l = [1, 2, 3]
# id(l)
# print(id(l))
