# Write here the code challenge solution
def delete_node(head, target):
    current = head
    previous = None

    while current is not None:
        if current.value == target:
            if previous is not None:
                previous.next = current.next
            else: 
                head = current.next

            return head
        
        previous = current 
        current = current.next 

    return head 