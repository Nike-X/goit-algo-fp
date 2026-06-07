# This script visualizes binary heap as tree

# Standard library modules
import uuid
import heapq

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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

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

# Main function creates tree from heap and visualizes it
def main():
    # Create a heap
    values = [17, 3, 25, 1, 9, 14, 30, 6, 8, 20, 11, 5]
    heapq.heapify(values)

    print("Heap tree:")
    print(values)

    # Create a tree from the heap
    heap_root = build_heap_tree(values)

    # Check that heap is not empty and visualize it
    if heap_root:
        draw_tree(heap_root)
    else:
        print("Heap is empty.")

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()
