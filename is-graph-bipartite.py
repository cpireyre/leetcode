from collections import deque, defaultdict


def isBipartite(G):
    V = set(range(len(G)))

    def BFS(source):
        Q = deque([(source, None)])
        S = {source}
        green, red = set(), set()
        while Q:
            u, parent = Q.popleft()
            N = {v for v in G[u] if v not in S}
            S.update(N)
            Q.extend(((n, u) for n in N))
            nonlocal V
            V -= S
            color = red if parent in green else green
            color.add(u)
            # print(u, parent)
            # print(color)
            # print(G[u])
            if any(w in color for w in G[u]):
                return False
        return True

    while V:
        source = V.pop()
        if not BFS(source):
            return False
    return True
# Runtime: 199 ms, faster than 71.41% of Python3 online submissions for Is Graph Bipartite?.
# Memory Usage: 14.6 MB, less than 37.58% of Python3 online submissions for Is Graph Bipartite?.


graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(isBipartite(graph))  # True
graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(isBipartite(graph))  # False
