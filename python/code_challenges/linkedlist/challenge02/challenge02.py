class Node:
    def __init__(self, value=0, next=None):
        self.value = value 
        self.next = next
def MiddleNode(head):
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
'''
def print_linked_list(node):
    result = []
    while node:
        result.append(str(node.value))
        node = node.next
    print(" -> ".join(result))
# Example usage:
if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    middle_node = MiddleNode(head)

    print_linked_list(middle_node)

output : (.venv) ➜  challenge02 git:(11-find_middle_node) ✗ python3 challenge02.py  
3 -> 4 -> 5
'''