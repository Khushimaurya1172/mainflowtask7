def has_cycle(graph):
    visited = set()

    def dfs(v, parent):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

# User Input
n = int(input("Enter number of nodes: "))
graph = {i: [] for i in range(n)}
e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph[u].append(v)
    graph[v].append(u)

print("Graph contains cycle:", has_cycle(graph))
