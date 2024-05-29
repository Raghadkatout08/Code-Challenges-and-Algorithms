class Node:
    '''Represents a node in a singly linked list.'''
    def __init__(self, value, next= None): 
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        '''Initializes an empty linked list.'''
        self.head = None
    
    def push_list(self, new_value):
        '''Adds a new node with the given value to the beginning of the linked list.'''
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, target):
        '''Deletes the node with the specified value from the linked list.'''
        current = self.head
        previous = None
        found = False


        while current is not None:
            if current.value == target:
                found = True
                if previous is not None:
                    previous.next = current.next
                else: 
                    self.head = current.next
                break
        
            previous = current 
            current = current.next

        if not found:
            print(f"Node with value {target} not found in the linked list.")
    
    def print_list(self):
        '''Prints the values of nodes in the linked list.'''
        current = self.head 
        while current is not None:
            print(current.value, end=' -> ')
            current = current.next
        print("None")

#Usage 

ll = LinkedList()
ll.push_list(5)
ll.push_list(4)
ll.push_list(3)
ll.push_list(2)
ll.push_list(1)

print("Original Linked List:", end=' ')
ll.print_list()


print(f"\nDeleting node with value 3:", end=' ')
ll.delete_node(3)
ll.print_list()