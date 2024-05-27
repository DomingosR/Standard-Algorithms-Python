from collections import defaultdict
from heapq import *

def dijkstra(n, edges, startVertex):
    # Preliminaries
    largeNum = 10 ** 9 + 7
    minDist = [largeNum] * n
    minDist[startVertex] = 0
    
    # Create graph
    neighbors = defaultdict(list)
    for u, v, dist in edges:
        neighbors[u].append((v, dist))
        
    edgeQueue = []
    heappush(edgeQueue, (0, startVertex))
    
    # Main loop
    while edgeQueue:
        dist, u = heappop(edgeQueue)
        if dist > minDist[u]:
            continue
        for v, nextDist in neighbors[u]:
            totalDist = dist + nextDist
            if totalDist < minDist[v]:
                minDist[v] = dist + nextDist
                heappush(edgeQueue, (minDist[v], v))
                
    return minDist

# Tester code
n = 8
edges = [[0, 1, 3], [1, 2, 4], [2, 3, 3], [1, 3, 5], [2, 4, 3], [1, 4, 5], [2, 5, 4], [2, 6, 4], [5, 6, 2], [3, 7, 4], [6, 7, 2]]
startVertex = 0
print(dijkstra(n, edges, startVertex))  # Expected Output: [0, 3, 7, 8, 8, 11, 11, 12]