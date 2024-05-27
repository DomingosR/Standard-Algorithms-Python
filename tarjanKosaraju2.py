from collections import defaultdict

def tarjan(n, edges):
    neighbors = defaultdict(list)
    id, lowLink = [-1] * n, [-1] * n
    vertexStack = []
    components = []
    currentId = [0]
    
    for u, v in edges:
        neighbors[u].append(v)
        
    def processVertex(u):
        if id[u] == -1:
            id[u] = lowLink[u] = currentId[0]
            currentId[0] += 1
            vertexStack.append(u)
            
            for v in neighbors[u]:
                processVertex(v)
                if v in vertexStack:
                    lowLink[u] = min(lowLink[u], lowLink[v])
            
            if id[u] == lowLink[u]:
                component = []
                while True:
                    v = vertexStack.pop()
                    component.append(v)
                    if v == u:
                        break
                components.append(component)
    
    for u in range(n):
        processVertex(u)
    
    return components
    
def kosaraju(n, edges):
    graph, reverseGraph = defaultdict(list), defaultdict(list)
    processed = set()
    topSort = []
    
    for u, v in edges:
        graph[u].append(v)
        reverseGraph[v].append(u)
    
    def processVertex(u):
        if u not in processed:
            processed.add(u)
            for v in graph[u]:
                processVertex(v)
            topSort.append(u)
            
    for u in range(n):
        processVertex(u)
    
    processed = set()
    components = []
    
    def getSCC(u, component):
        processed.add(u)
        component.append(u)
        for v in reverseGraph[u]:
            if v not in processed:
                component = getSCC(v, component)
        return component
    
    while topSort:
        u = topSort.pop()
        if u not in processed:
            components.append(getSCC(u, []))
    
    return components
    

# Tester code
n = 8
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [1, 4], [4, 5], [5, 6], [6, 4], [6, 7]]
print(tarjan(n, edges))
print(kosaraju(n, edges))