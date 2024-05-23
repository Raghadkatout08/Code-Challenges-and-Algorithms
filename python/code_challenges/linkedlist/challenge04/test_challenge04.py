from challenge04 import LinkedList 

def test_reverse_list():

    # Test Case 1: [1, 2, 3, 4, 5, 6, 7] -> [7, 6, 5, 4, 3, 2, 1]
    ll1 = LinkedList()
    ll1.push_list(7)
    ll1.push_list(6)
    ll1.push_list(5)
    ll1.push_list(4)
    ll1.push_list(3)
    ll1.push_list(2)
    ll1.push_list(1)
    ll1.reverse()

    actual1 = []
    current1 = ll1.head 
    while current1 is not None:
        actual1.append(current1.value)
        current1 = current1.next
    expect1 = [7, 6, 5, 4, 3, 2, 1]

    assert actual1 == expect1 , f"Expected: {expect1}, Actual: {actual1}"

    # Test Case 2: [1, 2] -> [2, 1]
    ll2 = LinkedList()
    ll2.push_list(2)
    ll2.push_list(1)
    ll2.reverse()

    actual2 = []
    current2 = ll2.head 
    while current2 is not None:
        actual2.append(current2.value)
        current2 = current2.next
    expect2 = [2, 1]

    assert actual2 == expect2 , f"Expected: {expect2}, Actual: {actual2}"

    # Test Case 3: [1] -> [2]
    ll3 = LinkedList()
    ll3.push_list(1)
    ll3.reverse()

    actual3 = []
    current3 = ll3.head 
    while current3 is not None:
        actual3.append(current3.value)
        current3 = current3.next
    expect3 = [1]

    assert actual3 == expect3 , f"Expected: {expect3}, Actual: {actual3}"


    # Test Case 4: [] -> []
    ll4 = LinkedList()
    ll4.reverse()

    actual4 = []
    current4 = ll4.head 
    while current4 is not None:
        actual4.append(current4.value)
        current4 = current4.next
    expect4 = []

    assert actual4 == expect4 , f"Expected: {expect4}, Actual: {actual4}"