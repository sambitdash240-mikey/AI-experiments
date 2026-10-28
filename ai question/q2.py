def dfs(graph, node, visited):
    if node not in visited:
      print(node, end=" ")
      visited.add(node)

      for neighbor in graph[node]:
        dfs(graph, neighbor, visited)


graph = {}

n = int(input("Enter NO. of vertices: "))

for i in range(n):
  vertex = input(f"Enter vertex {i+1}: ")
  neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").split()
  graph[vertex] = neighbors


start = input("Enter starting vertex: ")

visited = set()

print("DFS Traversal:")
dfs(graph, start, visited)