import heapq

def prims(graph, start):
    # Initialize variables
    visited = set()
    min_heap = []
    minimum_spanning_tree = []

    # Add the start node to the visited set
    visited.add(start)

    # Add the edges of the start node to the minimum heap
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    # Process until all nodes are visited
    while min_heap:
        # Pop the minimum weight edge from the heap
        weight, u, v = heapq.heappop(min_heap)

        # If the destination node is already visited, skip it
        if v in visited:
            continue

        # Add the edge to the minimum spanning tree
        minimum_spanning_tree.append((u, v, weight))

        # Add the destination node to the visited set
        visited.add(v)

        # Add the edges of the destination node to the minimum heap
        for neighbor, weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, v, neighbor))

    return minimum_spanning_tree


# Define the graph
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 1)],
    'C': [('A', 3), ('B', 4), ('D', 5)],
    'D': [('B', 1), ('C', 5)]
}

# Specify the start node
start_node = 'A'

# Run Prim's algorithm
minimum_spanning_tree = prims(graph, start_node)

# Print the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    u, v, weight = edge
    print(f"{u} --({weight})-- {v}")
