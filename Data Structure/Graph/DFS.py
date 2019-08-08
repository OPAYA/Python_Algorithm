def dfs(graph, start_node):
	visit = {}
	stack = []

	stack.append(start_node)

	while stack:
		node = stack.pop()
		if node not in visit:
			visit[node] = True
			stack.extend(graph[node])
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
visit = dfs(graph, 'A')
print(visit.keys())
