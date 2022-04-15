class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def prettyprint(self, level=0, indent="    "):
        print(level*indent + str(self.val))
        if self.left:
            self.left.prettyprint(level+1, indent)
        if self.right:
            self.right.prettyprint(level+1, indent)

def fromArray(ns,depth=0):
    if depth >= len(ns):
        return None
    curr = TreeNode(ns[depth])
    curr.left = fromArray(ns, 2*depth + 1)
    curr.right = fromArray(ns, 2*depth + 2)
    return curr

def trimBST(root, low, high):
    if not root:
        return None
    if root.val < low:
        return trimBST(root.right, low, high)
    if root.val > high:
        return trimBST(root.left, low, high)
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)
    return root
# Runtime: 65 ms, faster than 60.80% of Python3 online submissions for Trim a Binary Search Tree.
# Memory Usage: 18.2 MB, less than 11.70% of Python3 online submissions for Trim a Binary Search Tree.
