from collections import defaultdict
from heapq import *

def dijkstra(n, edges, initialVertex):
    # Preliminaries
    largeNum = (10 ** 9) * (n - 1) + 1 
    minDist = [largeNum] * n
    minDist[initialVertex] = 0

    distHeap = []
    distHeap.append((0, initialVertex))

    # Create graph
    neighbors = defaultdict(dict)
    for u, v, dist in edges:
        neighbors[u][v] = dist
    
    # Main algorithm
    while distHeap:
        currentDist, u = heappop(distHeap)
        for v, nextDist in neighbors[u].items():
            if minDist[v] > currentDist + nextDist:
                minDist[v] = currentDist + nextDist
                heappush(distHeap, (currentDist + nextDist, v))
    
    return minDist
    
# Code tester
edges = [[0, 1, 4], [1, 2, 2], [2, 3, 5], [3, 0, 1], [2, 4, 3], [4, 5, 2], [5, 6, 7], [6, 4, 4], [6, 7, 3], [7, 4, 3]]
n = 8
print(dijkstra(n, edges, 3))