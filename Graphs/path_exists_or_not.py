# define the graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
    'F': []
}

def path_exists_or_not(graph, start, end):
    # mark vertices as false i.e. not visited
    visited = [False] * len(graph)
    # making an empty list for bfs
    queue = []

    # mark given node as visited and add it in the queue
    visited.append(start)
    queue.append(start)

    while queue:
        # removing the front vertex or the vertex at 0th index and printing its value
        v = queue.pop(0)
        # if v is the end node then the path exists
        if v == end:
            return True

        # get all adjacent nodes of the removed vertex v from the graph
        # if the node is unvisited add it to the queue and mark it visited
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    # if the end node couldn't be reached there exists no path
    return False

print()
print("The given graph is:")
print()
for k,v in graph.items():
    print(k,":",v)
print()
start = input("Enter the starting node to be checked for a path: ")
end = input("Enter the end node to be checked for a path for: ")
print(path_exists_or_not(graph,start,end),"there exists a path between",start,"and",end,"nodes")
print()