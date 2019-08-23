from collections import defaultdict
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

def build_graph(prerequisites):

    graph = {}
    for a, b in prerequisites:
        print(a, b)
        graph[a] = [b]
    return graph


def DFS(graph, start_node):
	stack = list()
	visited = list()
	stack.append(start_node)

	while stack:

		node = stack.pop()
		if node in visited:
			return False
		elif node not in visited:

			visited.append(node)
			print(visited)
			#print('ddd', graph[node])
			stack.extend(graph[node])
		
	return True


graph = build_graph([[1,0],[0,3],[3,4]])
print(graph)
DFS(graph, 1)