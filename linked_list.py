# This script demonstrates some operations with linked list:
# - revert list
# - sort list (merge sort was chosen)
# - merge two sorted linked lists into one

# Part 1: LinkedList class implementation
# (from learning materials)

# Define Node class. Each Node has value (data) 
# and link to the next Node (next) 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Define LinkedList class
class LinkedList:
    # Create empty LinkedList
    def __init__(self):
        self.head = None

    # Add a new Node at the LinkedList beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Add a new Node at the LinkedList end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Insert a new Node after specific Node
    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Delete existing Node
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    # Find Node with given value (data)
    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    # Print LinkedList
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Reverse LinkedList by changing links between nodes
    # After reversing, the original head becomes the last node,
    # and the original last node becomes the new head
    def reverse_list(self):
        cur = self.head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        self.head = prev

    # Wrapper for _merge_sort function
    def sort(self):
        self.head = self._merge_sort(self.head)

    # Helper function for merge sort
    def _merge_sort(self, head):
        # If list is empty or contains only head, no sort is needed
        if not head or not head.next:
            return head

        # Split initial list into two halves
        second_head = self._split(head)
        # Recursively sort both lists
        left = self._merge_sort(head)
        right = self._merge_sort(second_head)
        # Merge and return sorted half-lists
        return self._merge_sorted_nodes(left, right)
            
    # Helper function for list split
    def _split(self, head):
        # Set two pointers:
        # - fast pointer moves two nodes at a time
        # - slow pointer moves one node at a time
        # When fast pointer reaches the end of the list,
        # slow pointer will be near the middle
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next

        second = slow.next
        slow.next = None
        return second

    # Helper function for sorted lists merging
    def _merge_sorted_nodes(self, first, second):

        if not first:
            return second
        if not second:
            return first

        if first.data <= second.data:
            first.next = self._merge_sorted_nodes(first.next, second)
            return first
        else:
            second.next = self._merge_sorted_nodes(first, second.next)
            return second

# Function for sorted lists merging (wrapper over Linked List _merge_sorted_nodes helper)
def merge_sorted_lists(first_list: LinkedList, second_list: LinkedList) -> LinkedList:
    result = LinkedList()
    result.head = result._merge_sorted_nodes(first_list.head, second_list.head)

    return result

# Part 2: Main function to demonstrate LinkedList operations

def main():
    # Create and fill two similar test lists
    values = [40, 20, 30, 80, 10, 70, 50, 60]
    list_for_reverse = LinkedList()
    list_for_sort = LinkedList()

    for value in values:
        list_for_reverse.insert_at_end(value)
        list_for_sort.insert_at_end(value)

    # Print initial list
    print("Initial list:")
    list_for_reverse.print_list()

    # Revert list and print
    print("\nReverted list:")
    list_for_reverse.reverse_list()
    list_for_reverse.print_list()

    # Sort list and print
    print("\nSorted list:")
    list_for_sort.sort()
    list_for_sort.print_list()

    # Create two sorted lists
    first_values_set = [10, 20, 30, 40]
    first_sorted_list = LinkedList()
    second_values_set = [50, 60, 70, 80]
    second_sorted_list = LinkedList()

    for i in range(len(first_values_set)):
        first_sorted_list.insert_at_end(first_values_set[i])
        second_sorted_list.insert_at_end(second_values_set[i])

    # Print both sorted lists before merging
    # (they will be affected by merging operation)
    print("\nFirst sorted list:")
    first_sorted_list.print_list()
    print("\nSecond sorted list:")
    second_sorted_list.print_list()

    # Merge lists and print
    merged_list = merge_sorted_lists(first_sorted_list, second_sorted_list)

    print("\nMerged list:")
    merged_list.print_list()

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()