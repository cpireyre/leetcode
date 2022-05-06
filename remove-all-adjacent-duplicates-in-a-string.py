from itertools import groupby


def removeDuplicates(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
# Runtime: 107 ms, faster than 55.27% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.9 MB, less than 47.44% of Python3 online submissions for Remove All Adjacent Duplicates In String.

s = "abbaca"
print(removeDuplicates(s))  # "ca"
s = "azxxzy"
print(removeDuplicates(s))  # "ay"
