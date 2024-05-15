# Write your test here
from Node import Node
from challenge01 import delete_node

def test_delete_node():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    head = delete_node(head, 3)

    node = head
    expected_values = [1, 2, 4]
    index = 0
    while node:
        assert node.value == expected_values[index]
        node = node.next
        index += 1


    assert node is None