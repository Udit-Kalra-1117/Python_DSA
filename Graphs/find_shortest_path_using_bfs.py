graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}

def find_shortest_path(graph, start, end):
    queue = [start]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                new_path = list(path)  # Create a new list to avoid modifying the original path
                new_path.append(neighbor)
                queue.append(new_path)
    return None

s = input("Enter the starting node to find the shortest path from: ")
e = input("Enter the ending node to find the shortest path to: ")
shortest_path = find_shortest_path(graph, s, e)

if shortest_path:
    print("The shortest path from", s, "to", e, "is:", shortest_path)
else:
    print("No path found between", s, "and", e)
