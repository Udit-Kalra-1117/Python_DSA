# define the graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
    'F': []
}

def bfs(node):
    # mark vertices as false i.e. not visited
    visited = [False] * len(graph)
    # making an empty list for bfs
    queue = []

    # mark given node as visited and add it in the queue
    visited.append(node)
    queue.append(node)

    while queue:
        # removing the front vertex or the vertex at 0th index and printing its value
        v = queue.pop(0)
        print(v, end=" ")

        # get all adjacent nodes of the removed vertex v from the graph
        # if the node is unvisited add it to the queue and mark it visited
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print()
print("The given graph is:")
print()
for k,v in graph.items():
    print(k,":",v)
print()
value = input("Enter the node from which the BFS is to be done (available nodes are: A, B, C, D, E and F): ")
print("The BFS from",value,"is:",end=" ")
bfs(value)
print()
print()