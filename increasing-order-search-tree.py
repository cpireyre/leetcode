from itertools import pairwise
def increasingBST(root):
    s = []
    def traverse(root):
        if root:
            traverse(root.left)
            s.append(root)
            traverse(root.right)
    traverse(root)
    for l, r in pairwise(s):
        l.left = None
        l.right = r
    s[-1].left, s[-1].right = None, None
    return s[0]
# Runtime: 37 ms, faster than 70.10% of Python3 online submissions for Increasing Order Search Tree.
# Memory Usage: 13.9 MB, less than 50.58% of Python3 online submissions for Increasing Order Search Tree.
