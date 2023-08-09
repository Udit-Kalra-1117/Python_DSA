# Graph of nodes
graph = {
    0: [2],
    1: [2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}

def dfs(node, graph, visited, component):
    component.append(node)  # Store answer
    visited[node] = True  # Mark visited

    # Traverse to each adjacent node of a node
    for child in graph[node]:
        if not visited[child]:  # Check whether the node is visited or not
            dfs(child, graph, visited, component)  # Call the dfs recursively


node = int(input("Enter the node from which the dfs is to be done (available nodes are 0, 1, 2, 3 and 4): "))  # Starting node
visited = [False]*len(graph)  # Make all nodes to False initially
component = []
dfs(node, graph, visited, component) # Traverse to each node of a graph
print("DFS from node",node,"is:",component)
print()