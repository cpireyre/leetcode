from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS ver
def maxDepth(root: Optional[TreeNode]) -> int:
    maxDepth, q = 0, [root]
    if not root: return 0
    while q:
        maxDepth += 1
        _next = []
        for node in q:
            if node.left: _next.append(node.left)
            if node.right: _next.append(node.right)
        q = _next
    return maxDepth
#Runtime: 63 ms, faster than 37.30% of Python3 online submissions for Maximum Depth of Binary Tree.
#Memory Usage: 15.4 MB, less than 86.50% of Python3 online submissions for Maximum Depth of Binary Tree.

# DFS one liner
def maxDepth(root: Optional[TreeNode]) -> int:
    return 0 if not root else max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
    # return 0 if not root else (l if (l := 1 + self.maxDepth(root.left)) > (r := 1 + self.maxDepth(root.right)) else r)
    # turns out assignments in returns are even worse than overhead of recursively calling max()
# Runtime: 55 ms, faster than 50.62% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.3 MB, less than 31.05% of Python3 online submissions for Maximum Depth of Binary Tree.
