def addTwoNumbers(l1, l2):
    def addRecur(l1, l2, carry=0):
        if not l1 and not l2:
            return ListNode(carry) if carry else None
        summand, augend = l1.val if l1 else 0, l2.val if l2 else 0
        sum = summand + augend + carry
        carry = sum // 10
        head = ListNode(sum % 10)
        head.next = addRecur(l1.next if l1 else None, l2.next if l2 else None, carry)
        return head
    return addRecur(l1, l2)
# Runtime: 67 ms, faster than 93.31% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14 MB, less than 41.03% of Python3 online submissions for Add Two Numbers.
