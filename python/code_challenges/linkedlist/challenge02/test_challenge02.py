from challenge02 import Node, MiddleNode

def create_linked_list(values):
    '''Creates a singly linked list from a list of values.'''
    if not values:
        return None
    head = Node(values[0])
    current = head 

    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def linked_list(head):
    '''Extracts the values of nodes in a linked list and returns them as a list.'''
    values = []
    current = head 
    while current:
        values.append(current.value)
        current = current.next 
    return values

def test_middle_node():
    '''Tests the MiddleNode function with various test cases.'''
    head1 = create_linked_list([1, 2, 3, 4, 5])
    middle1 = MiddleNode(head1)
    actual1 = middle1.value
    expected1 = 3
    assert actual1 == expected1

    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    middle2 = MiddleNode(head2)
    actual2 = middle2.value
    expected2 = 4
    assert actual2 == expected2

    head3 = create_linked_list([1])
    middle3 = MiddleNode(head3)
    actual3 = middle3.value
    expected3 = 1
    assert actual3 == expected3

    head4 = create_linked_list([1, 2])
    middle4 = MiddleNode(head4)
    actual4 = middle4.value
    expected4 = 2
    assert actual4 == expected4
    head5 = create_linked_list(list(range(1, 101)))
    middle5 = MiddleNode(head5)
    assert middle5.value == 51

    head6 = create_linked_list(list(range(1, 102)))
    middle6 = MiddleNode(head6)
    assert middle6 is None 

    head7 = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    middle7 = MiddleNode(head7)
    actual7 = middle7.value
    expected7 = 4
    assert actual7 == expected7