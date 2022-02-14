from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
