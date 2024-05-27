def bellmanFord(n, edges, sourceVertex):
    largeNum = 10 ** 9 + 7
    minDist = [largeNum] * n
    minDist[sourceVertex] = 0
    
    for _ in range(n):
        for u, v, dist in edges:
            if minDist[u] < largeNum and minDist[u] + dist < minDist[v]:
                minDist[v] = minDist[u] + dist
    
    for u, v, dist in edges:
            if minDist[u] < largeNum and minDist[u] + dist < minDist[v]:
                return "Graph contains negative cycle."
                
    return minDist
    
# Tester code
n = 5
edges = [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2], [1, 4, 2], [3, 2, 5], [3, 1, 1], [4, 3, -3]]
print(bellmanFord(n, edges, 0))