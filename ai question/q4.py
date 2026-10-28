graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}

def astar(start, goal):
    open_list = [(start, 0)]
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        # Select node with minimum f = g + h
        current = min(open_list, key=lambda x: x[1] + heuristic[x[0]])
        open_list.remove(current)
        current_node = current[0]

        if current_node == goal:
            path = [goal]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)

            path.reverse()
            return path, g_cost[goal]

        for neighbor, cost in graph[current_node]:
            new_cost = g_cost[current_node] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current_node
                open_list.append((neighbor, new_cost))

    return None, float('inf')

# Main program
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

path, cost = astar(start, goal)

if path:
    print("\nShortest Path: ", " -> ".join(path))
    print("Total Cost: ", cost)
else:
    print("\nPath not found!")