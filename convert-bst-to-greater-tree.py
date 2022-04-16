def convertBST(root):

    nodes, vals = [], []

    def traverse(node):
        if node:
            traverse(node.right)
            nodes.append(node)
            vals.append(node.val)
            traverse(node.left)

    traverse(root)
    for node, total in zip(nodes, accumulate(vals, lambda a, b: a + b)):
        node.val = total

    return root
# Runtime: 92 ms, faster than 77.36% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 17.3 MB, less than 5.51% of Python3 online submissions for Convert BST to Greater Tree.
