# O(n) space but oh well
def recoverTree(root):
    nodes, vals = [], []
    def traverse(root):
        if root:
            traverse(root.left)
            nonlocal nodes
            nonlocal vals
            nodes.append(root)
            vals.append(root.val)
            traverse(root.right)
    traverse(root)
    tmp = 0
    for n, v in zip(nodes, sorted(vals)):
        if n.val != v:
            n.val = v
            tmp += 1
        if tmp == 2:
            return root
# Runtime: 78 ms, faster than 80.62% of Python3 online submissions for Recover Binary Search Tree.
# Memory Usage: 14.3 MB, less than 28.16% of Python3 online submissions for Recover Binary Search Tree.
