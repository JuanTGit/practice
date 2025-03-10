"""
Graph Traversal - Algorithm to visit every vertex of a graph

Breadth-first = Queue - FIFO
Breadth = broad/wide - horizontal before vertically
O(V + E)
number of Vertices + number of Edges
"""

# We visit nodes at the same level before proceeding vertically

#       -A-
#  -B-       -C-
# D E   F       G
#           H       I


graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E', 'F'],
    'C' : ['G'],
    'D' : [],
    'E' : [],
    'F' : ['H'],
    'G' : ['I'],
    'H' : [],
    'I' : []
}

def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=' ')

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)