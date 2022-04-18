# this is not good code lol
def kthSmallest(root, k):
    ret = []
    def traverse(root):
        if root and len(ret) < k:
            traverse(root.left)
            if len(ret) < k:
                ret.append(root.val)
            traverse(root.right)
    traverse(root)
    return ret[-1]
# but it performs:
# Runtime: 54 ms, faster than 83.85% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 18 MB, less than 90.88% of Python3 online submissions for Kth Smallest Element in a BST.
