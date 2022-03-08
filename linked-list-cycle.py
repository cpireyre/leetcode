def hasCycle(head):
    if not head or not head.next:
        return False
    tortoise = head
    hare = head.next
    while hare and hare.next and tortoise:
        if tortoise in (hare, hare.next):
            return True
        tortoise = tortoise.next
        hare = hare.next.next
    return False
# Runtime: 71 ms, faster than 62.32% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.7 MB, less than 42.75% of Python3 online submissions for Linked List Cycle.
