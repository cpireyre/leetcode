def deleteDuplicates(head):
    if not head or not head.next:
        return head
    if head.val == head.next.val:
        duplicate = head.val
        while head and head.val == duplicate:
            head = head.next
        return self.deleteDuplicates(head)
    else:
        head.next = self.deleteDuplicates(head.next)
        return head
# Runtime: 61 ms, faster than 45.30% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.9 MB, less than 85.61% of Python3 online submissions for Remove Duplicates from Sorted List II.
