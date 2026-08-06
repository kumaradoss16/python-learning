from collections import deque

def bfs_shortest_path(graph, start, target):
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                print(visited)
                queue.append((neighbor, path + [neighbor]))

    return None

social_network = {
    "Alice": ["Bob", "Carol"],
    "Bob": ["Alice", "Dave"],
    "Carol": ["Alice", "Eve"],
    "Dave": ["Bob", "Eve"],
    "Eve": ["Carol", "Dave"]
}

print(bfs_shortest_path(social_network, "Alice", "Eve"))


