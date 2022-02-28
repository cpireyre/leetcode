# boring BFS ver
def hasPathSum(root, target):
    if not root: return False
    Q = [(root, root.val)]
    while Q:
        q, sum = Q.pop()
        if not q.left and not q.right and sum == target:
            return True
        if q.left:
            Q.append((q.left, sum + q.left.val))
        if q.right:
            Q.append((q.right, sum + q.right.val))
    return False
# Runtime: 70 ms, faster than 34.22% of Python3 online submissions for Path Sum.
# Memory Usage: 15.1 MB, less than 33.24% of Python3 online submissions for Path Sum.
