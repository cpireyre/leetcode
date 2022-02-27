from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def widthOfBinaryTree(root):
        if not root: return 0
        Q = deque([(root, 0, 0)])
        S = dict()
        while Q:
            v, depth, pos = Q.pop()
            if depth not in S:
                S[depth] = [pos]
            else:
                S[depth].append(pos)
            if v.left:
                Q.append((v.left, depth + 1, pos - 1))
            if v.right:
                Q.append((v.right, depth + 1, pos + 1))
        print(S)
        return max(max(d) - min(d) for d in S.values())

def fromArray(ns,depth=0):
    if depth >= len(ns):
        return None
    curr = TreeNode(ns[depth])
    curr.left = fromArray(ns, 2*depth + 1)
    curr.right = fromArray(ns, 2*depth + 2)
    return curr

# root = fromArray([1,3,2])
# root = fromArray([1,3,2,5])
# root = fromArray([1,3,2,5,None,None,9,6,None,None,7])
root = fromArray([1,3,2,5,None,None,9,6,None,None,7])
print(widthOfBinaryTree(root))
