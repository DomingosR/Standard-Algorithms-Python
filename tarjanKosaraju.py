from collections import defaultdict

def kosaraju(n, edges):
    # Create graph
    neighbors = defaultdict(list)
    reverseNeighbors = defaultdict(list)
    for u, v in edges:
        neighbors[u].append(v)
        reverseNeighbors[v].append(u)

    # Compute post-order for original graph
    postOrder = []
    visited = [False] * n

    def visit(u):
        if not visited[u]:
            visited[u] = True
            for v in neighbors[u]:
                visit(v)
            postOrder.append(u)

    for u in range(n):
        visit(u)

    # Do recursion on reversed graph to compute components
    components = []
    visited = [False] * n

    # Auxiliary function to get individual SCC on reversed graph
    def getSCC(u, currentComponent):
        currentComponent.append(u)
        visited[u] = True

        for v in reverseNeighbors[u]:
            if not visited[v]:
                currentComponent = getSCC(v, currentComponent)

        return currentComponent

    while postOrder:
        u = postOrder.pop()
        if not visited[u]:
            component = getSCC(u, [])
            components.append(component)
    
    return components

def tarjan(n, edges):
    # Create graph
    neighbors = defaultdict(list)
    for u, v in edges:
        neighbors[u].append(v)
    
    # Variables to control algorithm
    currentId = [0]                    # Id of current vertex being explored
    components = []                    # List of vertices in each connected component
    id = [-1] * n                      # Initially, ids are not assigned (so -1 indicates vertex has not been visited)
    lowLink = [-1] * n                 # Initially, low-link vertex has not been computed
    stack = []                         # Initially, stack is empty
    
    def visit(u):
        stack.append(u)
        id[u] = lowLink[u] = currentId[0]
        currentId[0] += 1
        
        # Visit all neighbors, minimizing lowLink on callback if vertex is on the stack
        for v in neighbors[u]:
            if id[v] == -1:
                visit(v)
            if v in stack:
                lowLink[u] = min(lowLink[u], lowLink[v])
                
        # Check if found a connected component, process it
        if id[u] == lowLink[u]:
            component = []
            while True:
                v = stack.pop()
                lowLink[v] = id[u]
                component.append(v)
                if v == u:
                    break
            components.append(component)

    for u in range(n):
        if id[u] == -1:
            visit(u)
    
    return components
    
# Code tester
edges = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5], [5, 6], [6, 3]]
n = 7


edges2 = [[0, 1], [1, 2], [2, 3], [3, 0], [2, 4], [4, 5], [5, 6], [6, 4], [6, 7]]
n2 = 8

print(kosaraju(n, edges))
print(tarjan(n, edges))
print(kosaraju(n2, edges2))
print(tarjan(n2, edges2))