# Start with the tree whose root node is smaller... wait.
# It's not possible to just merge them is it, see the 1->8 and 8->1 example
# Traverse the two BSTs simultaneously in a start-and-stop pattern
# depending on which tree has the biggest value.
# Like you would do to merge two sorted lists in O(n) time, except it's trees
# Definition for a binary tree node.

# So turns out BSTs can't be merged in one pass;
# therefore the only way is to do 2 in order traversals,
# get 2 sorted lists, and merge them in O(n1 + n2)

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, val):
        if self.val >= val:
            if self.left:
                self.left.add(val)
            else:
                self.left = TreeNode(val)
        if self.val < val:
            if self.right:
                self.right.add(val)
            else:
                self.right = TreeNode(val)

T1 = TreeNode(2)
T1.add(1)
T1.add(4)
T2 = TreeNode(1)
T2.add(0)
T2.add(3)

def mergeSortedLists(L1, L2):
    ret, i, j, len1, len2 = [], 0, 0, len(L1), len(L2)
    while i < len1 and j < len2:
        if L1[i] <= L2[j]:
            ret.append(L1[i])
            i += 1
        else:
            ret.append(L2[j])
            j += 1
    while i < len1:
        ret.append(L1[i])
        i += 1
    while j < len2:
        ret.append(L2[j])
        j += 1
    return ret
    
def getAllElements(root1: TreeNode, root2: TreeNode) -> List[int]:

    def treemap(tree, func):
        if tree.left:
            treemap(tree.left, func)
        func(tree.val)
        if tree.right:
            treemap(tree.right, func)

    def tree2List(T: TreeNode):
        ret = []
        treemap(T, lambda val: ret.append(val))
        return ret

    return mergeSortedLists(tree2List(root1), tree2List(root2))

print(getAllElements(T1, T2))
