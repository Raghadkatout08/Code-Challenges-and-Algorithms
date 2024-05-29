from challenge01 import LinkedList

def test_delete_node():
    """
        Test the delete_node method of the LinkedList class.

        This test creates a linked list with the values [1, 2, 3, 4, 5], 
        deletes the node with value 3, and verifies that the remaining nodes 
        have the values [1, 2, 4, 5].
    """
    ll = LinkedList()
    ll.push_list(5)
    ll.push_list(4)
    ll.push_list(3)
    ll.push_list(2)
    ll.push_list(1)

    ll.delete_node(3)
    

    actual = []
    current_node = ll.head
    while current_node is not None:
        actual.append(current_node.value)
        current_node = current_node.next

    expected = [1, 2, 4, 5]

    assert expected == actual