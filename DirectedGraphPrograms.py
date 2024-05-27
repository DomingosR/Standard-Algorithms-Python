# Import section
from collections import defaultdict, deque

class DirectedGraph:
    # Construct graph
    def __init__(self, edges, n):
        self.edges = edges
        self.n = n
        self.neighbors = defaultdict(set)
        self.reverseNeighbors = defaultdict(set)
        self.hasCycle = -1       # This will equal 0 or 1 when either Tarjan or
                                 # Kosaraju is first run

        for v, w in edges:
            self.neighbors[v].add(w)
            self.reverseNeighbors[w].add(v)

    # Compute connected components using Tarjan's algorithm
    def tarjan(self):
        currentId = 0
        sccCount = 0
        components = []

        indices = [-1] * self.n
        lowIndex = [-1] * self.n
        onStack = [False] * self.n
        stack = []

        def visit(v):
            nonlocal stack, onStack, currentId, sccCount, components
            stack.append(v)
            onStack[v] = True
            indices[v], lowIndex[v] = currentId, currentId
            currentId += 1

            for w in self.neighbors[v]:
                if indices[w] == -1:
                    visit(w)
                if onStack[w]:
                    lowIndex[v] = min(lowIndex[w], lowIndex[v])

            if indices[v] == lowIndex[v]:
                currentComponent = []
                while True:
                    w = stack.pop()
                    onStack[w] = False
                    lowIndex[w] = indices[v]
                    currentComponent.append(w)
                    if w == v:
                        break
                components.append(currentComponent)
                sccCount += 1

        for v in range(n):
            if indices[v] == -1:
                visit(v)

        if self.hasCycle == -1:
            self.hasCycle = 0 if sccCount == self.n else 1

        return (sccCount, components)

    # Compute strongly connected components using Kosaraju's algorithm
    def kosaraju(self):
        # Auxiliary functions
        def processVertex(v):
            nonlocal stack, visited
            visited[v] = True
            for w in self.neighbors[v]:
                if not visited[w]:
                    processVertex(w)
            stack.append(v)

        def processVertexReverse(v):
            nonlocal stack, visited, currentComponent
            visited[v] = True
            for w in self.reverseNeighbors[v]:
                if not visited[w]:
                    currentComponent.append(w)
                    processVertexReverse(w)

        # First, compute stack order using direct graph        
        stack = []
        visited = [False] * self.n

        for v in range(self.n):
            if not visited[v]:
                processVertex(v)

        # Then, process vertices using reverse stack order in reversed graph
        visited = [False] * n
        components = []
        currentComponent = []
        sccCount = 0

        while stack:
            v = stack.pop()
            if not visited[v]:
                currentComponent.append(v)
                processVertexReverse(v)
            if currentComponent:
                components.append(currentComponent)
                sccCount += 1
                currentComponent = []

        if self.hasCycle == -1:
            self.hasCycle = 0 if sccCount == self.n else 1

        return (sccCount, components)
    
    # Return whether graph has a cycle
    def getHasCycle(self):
        if self.hasCycle == -1:
            self.tarjan()
        return True if self.hasCycle == 1 else False

    # Compute topological sort of graph
    def topologicalSort(self):
        if self.getHasCycle():
            return []

        sortedVertices = []
        visited = [False] * self.n

        def visit(v):
            nonlocal sortedVertices

            if not visited[v]:
                visited[v] = True
                for w in self.neighbors[v]:
                    visit(w)
                sortedVertices.append(v)

        for v in range(self.n):
            visit(v)

        return sortedVertices[::-1]            

    # Compute bridges
    def bridges(self):
        # To be implemented
        return []

# Test Code
n = 8

# Edges 1 has scycle and 3 strongly connected components
edges1 = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 4]]

# Edges 2 has no cycle and 8 strongly connected components, each a singleton
edges2 = [[0, 1], [1, 2], [0, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [4, 7]]

edges = edges2
newGraph = DirectedGraph(edges, n)
print(newGraph.tarjan())
print(newGraph.kosaraju())
print(newGraph.getHasCycle())
print(newGraph.topologicalSort())

