# This script implements Dijkstra algorithm using binary heap

import heapq

# Dijkstra's algorithm works correctly for graphs with non-negative edge weights
def dijkstra(graph: dict, start):
    # Check that start vertex is in graph
    if start not in graph:
        raise ValueError("Start vertex is not in the graph")

    # Create a dictionary of the shortest distances for each vertex
    # Set 0 for the start vertex and infinity for all other vertices
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    # Create heap and add start vertex
    priority_queue = [(0, start)]

    # While the heap is not empty, process the vertex with the smallest known distance
    # and try to improve distances to its neighbors
    while priority_queue:
        # Pop the queue entry with the smallest known distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip outdated queue entries
        if current_distance > distances[current_vertex]:
            continue

        # Calculate new possible distances to the neighbors through the current vertex
        for neighbor, weight in graph[current_vertex].items():
            new_distance = current_distance + weight

            # If the new distance is shorter, update it in the distances dictionary
            # and add the neighbor to the heap
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances

# Main function to define graph and start vertex
def main():
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5, "E": 10},
        "C": {"A": 2, "B": 1, "D": 8, "E": 7},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"B": 10, "C": 7, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3}
    }

    start_vertex = "A"
    distances = dijkstra(graph, start_vertex)

    # Print shortest distance from start to each other vertex
    print(f"Shortest distances from {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()