# Write here the code challenge solution

''' Given the head of a linked list, remove the nth node from the end of the list and return its head. '''

class Node: 
    def __init__(self, value, next_node= None):
        """
        Initializes a new node.
        
        Args:
        value (int): The value of the node.
        next_node (Node, optional): The next node in the list. Defaults to None.
        """
        self.value = value 
        self.next = next_node

class LinkedList: 
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def push_list(self, new_value):
        """
        Add a new node with the given value to the beginning of the linked list.
        Constraints:
            1 <= new_value <= 100
        Args:
        new_value (int): The value of the new node to be added.
        """

        
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

        '''
            push_list(17), the list is [17].
            push_list(33), the list becomes [33, 17].
            llist.push_list(47), the list becomes [47, 33, 17].
        '''

    def deleteNodeend(self, n):
        """
        Delete the nth node from the end of the linked list.

        Constraints:
            1 <= n <= sz
            1 <= sz <= 30

        Args:
        n (int): The position of the node to be deleted from the end.
        """

        def length():
            """
            Calculates the length of the linked list.
            
            Returns:
            int: The number of nodes in the linked list.
            """
            temp = self.head
            count = 0 
            while temp is not None:
                count+=1 
                temp = temp.next
            return count
        
        list_length = length()
        
        # Determine the position from the beginning

        node_from_beginning = list_length - n

        if node_from_beginning == 0:
            self.head = self.head.next 
            return
        
        prev = None
        current = self.head 

        for _ in range(node_from_beginning):
            prev = current
            current = current.next

        #delete the node 
        prev.next = current.next

    def printList(self):
        """
        Print the values of all nodes in the linked list.
        """
        tmp_head = self.head 
        while tmp_head is not None: 
            print(tmp_head.value, end=' ')
            tmp_head = tmp_head.next
        print()

llist = LinkedList()
llist.push_list(17)
llist.push_list(33)
llist.push_list(47)
llist.push_list(70)
llist.push_list(81)
llist.push_list(22)
llist.push_list(74)
print("Linked List before deletion:  ", end=' ')
llist.printList()


llist.deleteNodeend(2)
print("Linked List After deletion :  ", end= ' ')
llist.printList()