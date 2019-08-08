def BFS(graph, start_node):
	visit = {}
	queue = []

	queue.append(start_node)

	while queue:
		node = queue.pop(0)
		if node not in visit:
			visit[node] = True
			queue.extend(graph[node])
	return visit

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['C'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
visit = BFS(graph, 'A')
print(visit.keys())
