from typing import *
# Inefficient recursive set ver
#def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#    S = set()
#
#    def walkTree(root):
#        if root.left: walkTree(root.left)
#        S.add(root.val)
#        if root.right: walkTree(root.right)
#
#    walkTree(root)
#    gen = (True for s in S for t in S if s + t == k and s != t)
#    return any(gen)
#Runtime: 231 ms, faster than 5.49% of Python3 online submissions for Two Sum IV - Input is a BST.
#Memory Usage: 21 MB, less than 5.22% of Python3 online submissions for Two Sum IV - Input is a BST.

# BFS queue and map ver
from collections import deque
def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    q = deque()
    q.appendleft(root)
    S = set()
    while q:
        curr = q.pop()
        print(curr.val)
        if k - curr.val in S:
            return True
        else:
            S.add(curr.val)
        if curr.left:
            q.appendleft(curr.left)
        if curr.right:
            q.appendleft(curr.right)

    return False
#Runtime: 78 ms, faster than 84.22% of Python3 online submissions for Two Sum IV - Input is a BST.
#Memory Usage: 16.3 MB, less than 95.83% of Python3 online submissions for Two Sum IV - Input is a BST.
