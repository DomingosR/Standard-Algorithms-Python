from collections import defaultdict

def bellmanFord(edges, n):
    destinations = defaultdict(list)
    visited = set()
    largeNum = (10 ** 9 + 7) * n + 1
    minDist = [float('inf')] * n
    sourceVertex = 0
    minDist[sourceVertex] = 0

    for _ in range(n-1):
        for u, v, w in edges:
            if minDist[u] < float('inf') and minDist[u] + w < minDist[v]:
                minDist[v] = minDist[u] + w
 
    for u, v, w in edges:
        if minDist[u] != float('inf') and minDist[u] + w < minDist[v]:
            return "Graph contains negative weight cycle"
 
    return minDist

def floydWarshall(edges, n):
    minDist = [[float('inf')] * n for _ in range(n)]

    for u, v, w in edges:
        minDist[u][v] = w
        minDist[v][u] = w

    for u in range(n):
        minDist[u][u] = 0

    for u in range(n):
        for v1 in range(n):
            for v2 in range(n):
                minDist[v1][v2] = min(minDist[v1][v2], minDist[v1][u] + minDist[u][v2])
    
    return minDist

n = 5
edges = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]

n2 = 4
edges2 = [(0, 1, -1), (1, 2, -1), (2, 3, -1), (3, 0, -1)]

n3 = 4
edges3 = [(0, 1, 3), (0, 2, 2), (1, 2, 4), (1, 3, 2)]

print(bellmanFord(edges, n))
print(bellmanFord(edges2, n2))
print(floydWarshall(edges3, n3))