
from collections import deque

def bfs_traverse(graph, start_node):
    visited = set()
    queue = deque()

    visited.add(start_node)
    queue.append(start_node)  # Added to initialize BFS

    print("BFS Traversal Order: ", end=" ")

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

Ex_graph = {
    'K': ['L', 'P'],
    'L': ['N'],
    'P': ['M'],
    'N': [],
    'M': []
}

bfs_traverse(Ex_graph, 'K')