def deleteDuplicates(head):
    if not head or not head.next:
        return head
    peek = head.next
    while peek and peek.val == head.val:
        peek = peek.next
    head.next = peek
    deleteDuplicates(head.next)
    return head
# Runtime: 45 ms, faster than 76.54% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14 MB, less than 56.17% of Python3 online submissions for Remove Duplicates from Sorted List.
