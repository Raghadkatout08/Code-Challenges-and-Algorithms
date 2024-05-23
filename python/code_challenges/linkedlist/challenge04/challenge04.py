""" Given a singly linked list, write a function to reverse it in place. """

class Node: 
    def __init__(self, value, next_node= None):
        """
            Node in a single linked list.
                - value: Value stored in the node.
                - next_node: Reference to the next node in the list.
        """
        self.value = value 
        self.next = next_node

class LinkedList:
        
    """ Initialize an empty Linked List """
    def __init__(self):
        self.head = None

    """
        Push a new value onto the front of the list.
            - new_value: Value to be added to the list.
    """
    def push_list(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head 
        self.head = new_node

    """
        Reverse the linked list in place.
    """
    def reverse(self):
        prev = None 
        current = self.head 
        while current is not None:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node 
        self.head = prev 

    """
        Print the values of all nodes in the linked list.
        return: None
    """
    def print_list(self):
        current = self.head 
        while current is not None: 
            print(current.value, end=' -> ')
            current = current.next
        print("None")


ll = LinkedList()
ll.push_list(7)
ll.push_list(6)
ll.push_list(5)
ll.push_list(4)
ll.push_list(3)
ll.push_list(2)
ll.push_list(1)

print("Original List: " , end= ' ') 
ll.print_list()

ll.reverse()

print("Reversed List: " , end= ' ') 
ll.print_list()