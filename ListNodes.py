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

def testListFunc(func, head, *kwargs):
    h = fromArray(head)
    res = func(h, *kwargs)
    return toArray(res)
