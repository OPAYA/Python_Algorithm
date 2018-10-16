vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0), (1, 3), (2, 0), (2, 4), (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]
graphs = (vertexList, edgeList)

def dfs(graph, start):
    vertexList, edgeList = graph
    #print(vertexList)
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]




    for edge in edgeList:
        #print(edge)
        adjacencyList[edge[0]].append(edge[1])
        print(adjacencyList)

    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                print('neg',neighbor)
                stack.append(neighbor)
                print('stack',stack)
        visitedVertex.append(current)
        #print(visitedVertex)
    return visitedVertex

print(dfs(graphs, 0))