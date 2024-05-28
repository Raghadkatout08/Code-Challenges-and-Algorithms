from challenge05 import LinkedList 

def test_insert_node1():
    # test case 1
    ll = LinkedList()
    ll.push_list(5)
    ll.push_list(4)
    ll.push_list(2)
    ll.push_list(1)    
    ll.insert_node(2, 3)

    expected_output = "1 -> 2 -> 3 -> 4 -> 5 -> None"
    actual_output = ll.print_list()

    assert actual_output == expected_output

# **************************************

def test_insert_node2():
    # test case 2
    ll = LinkedList()
    ll.push_list(2)
    ll.push_list(1)    
    ll.insert_node(2, 3)

    expected_output = "1 -> 2 -> 3 -> None"
    actual_output = ll.print_list()

    assert actual_output == expected_output

# **************************************

def test_insert_node3():
    #test case 3
    ll = LinkedList()
    ll.push_list(1)    
    ll.insert_node(1, 2)

    expected_output = "1 -> 2 -> None"
    actual_output = ll.print_list()

    assert actual_output == expected_output

# **************************************

def test_insert_node4():
    # test case 4
    ll = LinkedList()   
    ll.insert_node(10, 1)

    expected_output = "None"
    actual_output = ll.print_list()

    assert actual_output == expected_output