class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
def cloneGraph(node):
    if not node: return None
    Q = deque([node])
    S = dict()
    while Q:
        curr = Q.pop()
        if curr.val not in S: # creating the new node if we haven't before
            S[curr.val] = Node(curr.val)
        for u in curr.neighbors: # list all the candidate new nodes
            if u.val not in S: # store in S but don't overwrite
                S[u.val] = Node(u.val) # allocate new memory
                Q.append(u) # enqueue next 1
            S[curr.val].neighbors.append(S[u.val]) # add neighbor to adjacency list
    return S[node.val] # technically always 1 but whatever
# Runtime: 52 ms, faster than 53.28% of Python3 online submissions for Clone Graph.
# Memory Usage: 14.4 MB, less than 91.72% of Python3 online submissions for Clone Graph.
