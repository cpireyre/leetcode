# bit of help from the Leetcode forum to get the syntax right
# (I didn't know yield from)
def traverse(root):
    if root:
        yield from traverse(root.left)
        yield root.val
        yield from traverse(root.right)
            
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iter = traverse(root)
        self.nxt = next(self.iter, None)

    def next(self) -> int:
        nxt, self.nxt = self.nxt, next(self.iter, None)
        return nxt

    def hasNext(self) -> bool:
        return self.nxt != None
# Runtime: 86 ms, faster than 66.06% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 20.6 MB, less than 7.09% of Python3 online submissions for Binary Search Tree Iterator.
