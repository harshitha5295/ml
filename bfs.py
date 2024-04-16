import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def create_graph():
    graph = {}
    while True:
        node = int(input("Enter node (or type -1 to finish): "))
        if node == -1:
            break
        connections = input(f"Enter connections for node {node} (comma-separated, or type 'none' if no connections): ")
        if connections.lower() == 'none':
            graph[node] = []
        else:
            connections = list(map(int, connections.split(',')))
            graph[node] = connections
    return graph

if _name_ == '_main_':
    user_graph = create_graph()
    root_node = int(input("Enter the root node for BFS traversal: "))
    print("Following is Breadth First Traversal: ")
    bfs(user_graph, root_node)
