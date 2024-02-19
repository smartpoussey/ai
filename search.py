from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'

'''
def create_graph_from_input():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))
    
    for _ in range(vertices):
        node, *neighbors = input(f"Enter the neighbors of vertex {_ + 1} (e.g., A B C): ").split()
        graph[node] = neighbors
    
    return graph

graph = create_graph_from_input()
start_node = input("Enter the starting node for BFS traversal: ")
'''

print("DFS traversal starting from", start_node, ":")
dfs(graph, start_node)

print()

print("BFS traversal starting from", start_node, ":")
bfs(graph, start_node)
