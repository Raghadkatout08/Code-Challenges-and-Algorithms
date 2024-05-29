class Node:
    """
        Represents a node in a singly linked list.
    """
    def __init__(self, value=0, next=None):
        '''
            Initializes a node with the given value and next node reference.
        '''
        self.value = value 
        self.next = next

def MiddleNode(head):
    """
        Finds the middle node of a singly linked list.
        Returns:
            The middle node of the linked list. If there are two middle nodes,
            returns the second middle node.
    """
    if not head or not head.next:
        return head
    count = 0
    current = head
    while current:
        count += 1
        current = current.next 
    if count > 100:
        return None   

    runner = skipper = head 
    while skipper and skipper.next: 
        runner = runner.next 
        skipper = skipper.next.next
    if skipper and skipper.next :
        return runner.next  
    else:
        return runner

def print_linked_list(node):
    """
        Prints the values of nodes in a linked list.
    """
    result = []
    while node:
        result.append(str(node.value))
        node = node.next
    print(" -> ".join(result))


# Example usage:
if __name__ == "__main__":
    
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original linked list:", end=' ')
    print_linked_list(head)

    print("Linked list from middle node to end:", end=' ')
    middle_node = MiddleNode(head)

    print_linked_list(middle_node)