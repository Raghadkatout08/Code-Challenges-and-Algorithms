class Node:
    """
        Initialize a new Node with the given value and next pointer.

        Args:
            value: The value to be stored in the node.
            next: Reference to the next node in the linked list.
    """
    def __init__(self, value, next= None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        """
            Initialize an empty LinkedList with a head pointer.
        """
        self.head = None

    def push_list(self, new_value):
        """
            Add a new node with the given value to the beginning of the linked list.

            Args:
                new_value: The value to be stored in the new node.
        """
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node


    def insert_node(self, prev_value, new_value):
        """
            Insert a new node with the given value after the node with the specified value.

            Args:
                prev_value: The value of the node after which the new node should be inserted.
                new_value: The value to be stored in the new node.
        """
        current = self.head
        while current and current.value != prev_value:
            current = current.next
        
        if current is None:
            return None
            
        new_node = Node(new_value)
        new_node.next = current.next 
        current.next = new_node
        return "Node inserted successfully"

    def print_list(self):
        """
            Print the values of the linked list.
    
            Returns:
                str: A string containing the values of the linked list.
        """
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        values.append("None")
        linked_list_string = " -> ".join(values)
        print(linked_list_string)
        return linked_list_string



# Example usage

ll = LinkedList()
ll.push_list(5)
ll.push_list(4)
ll.push_list(2)
ll.push_list(1)

print("LinkedL List Before:", end=' ')
ll.print_list()

print(f"\033[1;32m{'=' * 50}\033[0m")

ll.insert_node(2, 3)
print("Linked List After 1st Insertion: ", end=' ')
ll.print_list()
print(f"\033[1;32m{'=' * 50}\033[0m")


ll.insert_node(1, 0)
print("Linked List After 2nd Insertion: ", end=' ')
ll.print_list()
print(f"\033[1;32m{'=' * 50}\033[0m")


ll.insert_node(0, 4)
print("Linked List After 3rd Insertion: ", end=' ')
ll.print_list()
print(f"\033[1;32m{'=' * 50}\033[0m")


ll.insert_node(-1, 4)
print("Linked List After 4th Insertion: ", end=' ')
ll.print_list()
print(f"\033[1;32m{'=' * 50}\033[0m")


ll.insert_node(5, 4)
print("Linked List After 5th Insertion: ", end=' ')
ll.print_list()
