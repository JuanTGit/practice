graph = {
	'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['E'],
    'E': []
}


def bfs(graph, start, goal):
	visited = set()
	queue = [start]

	while queue:
		current_node = queue.pop(0)

		if current_node == goal:
			print(f'Goal node {goal} found!')
			return True
		
		if current_node not in visited:
			visited.add(current_node)
			for item in graph[current_node]:
				queue.append(item)

	return False


def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    
    if start == goal:
        print(f"Found path to {goal}")
        return

    if start not in visited:
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(graph, neighbor, goal, visited)


def dfsIterative(graph, start, goal):
	stack = [start]
	visited = set()

	while stack:
		current_node = stack.pop()

		if current_node == goal:
			print(f'Goal {goal} found!')
			return True
		
		if current_node not in visited:
			visited.add(current_node)

			for neighbor in reversed(graph[current_node]):
				if neighbor not in visited:
					stack.append(neighbor)

	return False


print(dfsIterative(graph, 'A', 'E'))