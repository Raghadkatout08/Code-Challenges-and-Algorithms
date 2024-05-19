# Write your test here
from challenge02 import Node, MiddleNode

def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head 

    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def linked_list(head):
    values = []
    current = head 
    while current:
        values.append(current.value)
        current = current.next 
    return values

def test_middle_node():
    # Test case 1: List with 5 nodes
    head1 = create_linked_list([1, 2, 3, 4, 5])
    middle1 = MiddleNode(head1)
    actual1 = middle1.value
    expected1 = 3
    assert actual1 == expected1, f"Test case 1 failed: Actual={actual1}, Expected={expected1}"

    # Test case 2: List with 6 nodes
    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    middle2 = MiddleNode(head2)
    actual2 = middle2.value
    expected2 = 4
    assert actual2 == expected2, f"Test case 2 failed: Actual={actual2}, Expected={expected2}"

    # Test case 3: List with 1 node
    head3 = create_linked_list([1])
    middle3 = MiddleNode(head3)
    actual3 = middle3.value
    expected3 = 1
    assert actual3 == expected3, f"Test case 3 failed: Actual={actual3}, Expected={expected3}"

    # Test case 4: List with 2 nodes
    head4 = create_linked_list([1, 2])
    middle4 = MiddleNode(head4)
    actual4 = middle4.value
    expected4 = 2
    assert actual4 == expected4, f"Test case 4 failed: Actual={actual4}, Expected={expected4}"

    # Test case 5: List with 100 nodes
    head5 = create_linked_list(list(range(1, 101)))
    middle5 = MiddleNode(head5)
    assert middle5.value == 51  # Middle node for list with 100 nodes should be the 50th node

    # Test case 6: List with 101 nodes
    head6 = create_linked_list(list(range(1, 102)))
    middle6 = MiddleNode(head6)
    assert middle6 is None  # Middle node for list with more than 100 nodes should be None

    # Test case 7: List with 7 nodes (two middle nodes)
    head7 = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    middle7 = MiddleNode(head7)
    actual7 = middle7.value
    expected7 = 4
    assert actual7 == expected7, f"Test case 7 failed: Actual={actual7}, Expected={expected7}"

if __name__ == "__main__":
    test_middle_node()
    print("All test cases passed!")