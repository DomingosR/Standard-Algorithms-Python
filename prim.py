from collections import defaultdict
from heapq import *

def prim(n, edges):
    neighbors = defaultdict(list)
    visited = set()
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
        neighbors[u].append([v, dist])
        neighbors[v].append([u, dist])

    for v, dist in neighbors[0]:
        heappush(edgeHeap, (0, v, dist))
    
    visited.add(0)

    while edgeHeap and edgesLeft:
        u, v, dist = heappop(edgeHeap)
        if union(u, v):
            if v not in visited:
                for w, dist2 in neighbors[v]:
                    heappush(edgeHeap, (v, w, dist2))
            visited.add(v)
            minTree.append((u, v, dist))
            edgesLeft -= 1
    
    return minTree


    
 
n = 5
edges = [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [2, 4, 7], [3, 4, 9]]
print(prim(n, edges))