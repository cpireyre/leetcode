# stole this from forum, tried to clean it up but got other thigns to do
def removeDuplicates(s, k):
    stack = []    

    for c in s:                            
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])            

    return ''.join(c * cnt for c, cnt in stack)
# Runtime: 245 ms, faster than 18.41% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
# Memory Usage: 18.7 MB, less than 69.77% of Python3 online submissions for Remove All Adjacent Duplicates in String II.


s = "deeedbbcccbdaa"
k = 3
print(removeDuplicates(s, k)) # "aa"
