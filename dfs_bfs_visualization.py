# This script visualizes DFS and BFS traversal of a binary tree created from a heap

# Standard library modules
import uuid
import heapq
from collections import deque

# Installation required
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Additional parameter to save node color
        self.id = str(uuid.uuid4()) # Node unique identifier


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Visualize tree as a figure with custom title
def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

# Converts heap to tree
def build_heap_tree(heap, index=0):
    # Stop recursive execution
    if index >= len(heap):
        return None
    
    # Create tree node from current heap element
    node = Node(heap[index])

    # Calculates child element indices
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    # Recursively build left and right subtrees
    node.left = build_heap_tree(heap, left_index)
    node.right = build_heap_tree(heap, right_index)

    return node

# This function generates a unique color for each step of the traversal
def generate_colors(step, total_steps):
    if total_steps <= 1:
        return "#1296F0"
    
    start_color = (0, 30, 90)       # very dark blue
    end_color = (220, 245, 255)     # very light blue

    ratio = step / (total_steps - 1)

    r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
    g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
    b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)

    return f"#{r:02X}{g:02X}{b:02X}"

# This function assigns different colors to tree nodes according to traversal order
def color_nodes_by_order(nodes):
    total_nodes = len(nodes)

    for index, node in enumerate(nodes):
        node.color = generate_colors(index, total_nodes)


# Implement DFS traversal
# The function returns a list of nodes in the order they are traversed
def dfs_traversal(root):
    # If tree is empty, return empty list
    if root is None:
        return []
    
    # Initialize stack and visited nodes list
    visited_nodes = []
    stack = [root]

    # Pop node from stack, visit it and push children to stack (if any)
    # Loop until stack is empty
    while stack:
        node = stack.pop()
        visited_nodes.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited_nodes

# Implement BFS traversal
# The function returns a list of nodes in the order they are traversed
def bfs_traversal(root):
    # If tree is empty, return empty list
    if root is None:
        return []
    
    # Initialize double ended queue (deque) and visited nodes list
    visited_nodes = []
    queue = deque([root])

    # Pop node from deque, visit it and append children to deque (if any)
    # Loop until deque is empty
    while queue:
        node = queue.popleft()
        visited_nodes.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited_nodes


# Main function creates tree from heap and visualizes it
def main():
    # Create a heap
    values = [17, 3, 25, 1, 9, 14, 30, 6, 8, 20, 11, 5]
    heapq.heapify(values)

    # Execute DFS traversal and build a colored tree
    dfs_root = build_heap_tree(values)
    dfs_nodes = dfs_traversal(dfs_root)
    color_nodes_by_order(dfs_nodes)
    draw_tree(dfs_root, "DFS traversal")

    # Execute BFS traversal and build a colored tree
    bfs_root = build_heap_tree(values)
    bfs_nodes = bfs_traversal(bfs_root)
    color_nodes_by_order(bfs_nodes)
    draw_tree(bfs_root, "BFS traversal")

    # Show both figures simultaneously
    plt.show()

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()
