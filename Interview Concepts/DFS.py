"""
Graph Traversal - Algorithm to visit every vertex of a graph

Explorer that continues to explore new vertices as we see them until we hit a dead end in which case
you'll retrace your steps and continue exploration.

Depth-first = Stack - LIFO
Depth = long - vertical before horizontal
1.) Pre-order - O(n)
2.) In-order - O(n)
3.) Post-order - O(n)
"""

# Pre-order tree traversal
'1.) Visit node'
'2.) Traverse left'
'3.) Traverse right'

"""
Pseudocode

preorder(node)
    if node == null then return
    visit(node)
    preorder(node.left)
    preorder(node.right)
"""

# In-order tree traversal

'1.) Traverse left'
'2.) Visit node'
'3.) Traverse right'

"""
Pseudocode

inorder(node)
    if node == null then return
    inorder(node.left)
    visit(node)
    inorder(node.right)
"""

# Post-order tree traversal

'1.) Traverse left'
'2.) Traverse right'
'3.) Visit node'

"""
Pseudocode

postorder(node)
    if node == null then return
    postorder(node.left)
    postorder(node.right)
    visit(node)
"""


from collections import deque


graph = {
    'A' : ['B', 'G'],
    'B' : ['C', 'D', 'E'],
    'C' : [],
    'D' : [],
    'E' : ['F'],
    'F' : [],
    'G' : ['H'],
    'H' : ['I'],
    'I' : []
}

def dfs(graph, node):
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=' ')

        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)


def dfs(al):
    stack = ['g']
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # for x in al[node]:
            #     stack.append(x)
            [stack.append(x) for x in al[node]]
    print(visited)