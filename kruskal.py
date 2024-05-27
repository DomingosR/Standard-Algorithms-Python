from heapq import *

def kruskal(n, edges):
    edgeHeap = []
    edgesLeft = n - 1
    minTree = []

    UFParent = list(range(n))

    def find(u):
        if u != UFParent[u]:
            UFParent[u] = find(UFParent[u])
        return UFParent[u]
    
    def union(u, v):
        rootU, rootV = find(u), find(v)
        if rootU == rootV:
            return False
        UFParent[rootV] = rootU
        return True
    
    for u, v, dist in edges:
        heappush(edgeHeap, (dist, u, v))
    
    while edgeHeap and edgesLeft:
        dist, u, v = heappop(edgeHeap)
        if union(u, v):
            minTree.append((u, v, dist))
            edgesLeft -= 1
    
    return minTree

n = 5
edges = [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [2, 4, 7], [3, 4, 9]]
print(kruskal(n, edges))