def removeElement(ns):
        i = 0
        while i < len(ns):
            if ns[i] == val:
                del ns[i]
            else:
                i += 1
        return len(ns)
# Runtime: 36 ms, faster than 78.28% of Python3 online submissions for Remove Element.
# Memory Usage: 13.9 MB, less than 67.23% of Python3 online submissions for Remove Element.
