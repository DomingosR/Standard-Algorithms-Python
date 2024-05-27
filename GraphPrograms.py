# Import section
from collections import defaultdict, deque

class Graph:
    # Construct graph
    def __init__(self, edges, n):
        self.edges = edges
        self.n = n
        self.largeVal = 10 ** 9 + 7
        self.neighbors = defaultdict(set)

        for v, w in edges:
            self.neighbors[v].add(w)
            self.neighbors[w].add(v)

    # Compute connected components
    def connectedComponents(self):
        visited = [0] * self.n
        components = []

        for v in range(self.n):
            if not visited[v]:
                visited[v] = 1
                component = []
                vertexQueue = deque()
                component.append(v)
                vertexQueue.appendleft(v)

                while vertexQueue:
                    w1 = vertexQueue.pop()
                    for w2 in self.neighbors[w1]:
                        if w2 not in component:
                            visited[w2] = 1
                            component.append(w2)
                            vertexQueue.appendleft(w2)
                
                components.append(component)

        return components

    # Computing shortest cycle length
    def shortestCycleLen(self):
        shortestCycleLen = self.largeVal

        for v in range(n):
            dist = [self.largeVal] * n
            predecessor = [-1] * n 
            dist[v] = 0

            vertexQueue = deque()
            vertexQueue.appendleft(v)

            while vertexQueue:
                w1 = vertexQueue.pop()
                for w2 in self.neighbors[w1]:
                    if dist[w2] == self.largeVal:
                        dist[w2] = dist[w1] + 1
                        predecessor[w2] = w1
                        vertexQueue.appendleft(w2)
                    elif predecessor[w2] != w1 and predecessor[w1] != w2:
                        shortestCycleLen = min(dist[w2] + dist[w1] + 1, shortestCycleLen)
                
        return -1 if shortestCycleLen == self.largeVal else shortestCycleLen
    
    # Computing shortest cycle path
    def shortestCyclePath(self):
        shortestCycleLen = self.largeVal
        shortestCyclePath = []

        for v in range(n):
            dist = [self.largeVal] * n
            predecessor = [-1] * n 
            dist[v] = 0

            vertexQueue = deque()
            vertexQueue.appendleft(v)

            while vertexQueue:
                w1 = vertexQueue.pop()
                for w2 in self.neighbors[w1]:
                    if dist[w2] == self.largeVal:
                        dist[w2] = dist[w1] + 1
                        predecessor[w2] = w1
                        vertexQueue.appendleft(w2)
                    elif predecessor[w2] != w1 and predecessor[w1] != w2:
                        if dist[w2] + dist[w1] + 1 < shortestCycleLen:
                            shortestCycleLen = dist[w2] + dist[w1] + 1
                            # Construct shortest cycle path
                            currV = w2
                            shortestCyclePath = [currV]
                            while currV != v:
                                currV = predecessor[currV]
                                shortestCyclePath.append(currV)
                            shortestCyclePath = shortestCyclePath[::-1]
                            currV = w1
                            shortestCyclePath.append(currV)
                            while currV != v:
                                currV = predecessor[currV]
                                shortestCyclePath.append(currV)

        return shortestCyclePath

    # Determine if graph is cyclic using union-find
    def isCyclic(self):
        UFRoot = list(range(self.n))

        def find(v):
            while v != UFRoot[v]:
                v = UFRoot[v]
            return v
        
        def union(v, w):
            v = UFRoot[v]
            w = UFRoot[w]
            if v != w:
                UFRoot[w] = v
                return True
            return False

        for v, w in self.edges:
            if not union(v, w):
                return True
        
        return False

# Test Code
n = 8

# Edges1 has a cycle of length 3 and another of length 4, and two connected components
edges1 = [[0, 1], [1, 2], [0, 2], [2, 3], [4, 5], [5, 6], [6, 7], [4, 7]]

# Edges2 has no cycle and one connected components
edges2 = [[0, 1], [0, 2], [2, 3], [2, 4], [4, 5], [5, 6], [6, 7]]

edges = edges2
newGraph = Graph(edges, n)
print(newGraph.connectedComponents())
print(newGraph.shortestCycleLen())
print(newGraph.shortestCyclePath())
print(newGraph.isCyclic())