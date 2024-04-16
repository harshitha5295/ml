def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

def create_graph():
    graph = {}
    while True:
        node = input("Enter node (or type 'done' to finish): ")
        if node == 'done':
            break
        connections = input(f"Enter connections for node {node} (comma-separated, or type 'none' if no connections): ")
        if connections.lower() == 'none':
            graph[node] = set()
        else:
            connections = connections.split(',')
            graph[node] = set(connections)
    return graph

user_graph = create_graph()
start_node = input("Enter the starting node for DFS traversal: ")

dfs(user_graph, start_node)
