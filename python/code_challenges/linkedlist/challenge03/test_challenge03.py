# Write your test here
from challenge03 import LinkedList

def test_delete_nth_node_end():
    # Test case 1: Delete 2nd node from the end
    llist = LinkedList()
    llist.push_list(17)
    llist.push_list(33)
    llist.push_list(47)
    llist.push_list(70)
    llist.push_list(81)
    llist.push_list(22)
    llist.push_list(74)
    
    llist.deleteNodeend(2)
    
    expected_result = [74, 22, 81, 70, 47, 17]
    actual_result = []
    current = llist.head
    while current:
        actual_result.append(current.value)
        current = current.next
        
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

    # Test case 2: Delete the last node
    llist.deleteNodeend(1)
    
    expected_result = [74, 22, 81, 70, 47]
    actual_result = []
    current = llist.head
    while current:
        actual_result.append(current.value)
        current = current.next
        
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

    # Test case 3: Delete the head node
    llist.deleteNodeend(5)
    
    expected_result = [22, 81, 70, 47]
    actual_result = []
    current = llist.head
    while current:
        actual_result.append(current.value)
        current = current.next
        
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

    # Test case 4: Delete the node from a single element list
    single_node_list = LinkedList()
    single_node_list.push_list(10)
    
    single_node_list.deleteNodeend(1)
    
    assert single_node_list.head is None, "Expected list to be empty"

    # Test case 5: Delete the 1st node from the end in a two-element list
    two_node_list = LinkedList()
    two_node_list.push_list(20)
    two_node_list.push_list(30)
    
    two_node_list.deleteNodeend(1)
    
    expected_result = [30]
    actual_result = []
    current = two_node_list.head
    while current:
        actual_result.append(current.value)
        current = current.next
        
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"