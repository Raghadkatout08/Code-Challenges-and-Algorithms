from challenge03 import Stack, delete_middle 


def test_delete_middle_empty_stack():
    '''
        Test case for an empty stack.
        Verifies that deleting the middle element from an empty stack returns an empty stack.
    '''
    stack = Stack()
    assert delete_middle(stack).is_empty()

def test_delete_middle_odd_length_stack():
    '''
        Test case for a stack with an odd number of elements.
        Verifies that deleting the middle element from a stack with 5 elements 
        results in a stack with the middle element removed.
    '''
    stack = Stack()
    for i in range(5):
        stack.push(i)
    delete_middle(stack)
    assert str(stack) == "4 3 1 0"

def test_delete_middle_even_length_stack():
    '''
        Test case for a stack with an even number of elements.
        Verifies that deleting the middle element from a stack with 6 elements 
        results in a stack with the middle element removed.
    '''
    stack = Stack()
    for i in range(6):
        stack.push(i)
    delete_middle(stack)
    assert str(stack) == "5 4 3 1 0"

def test_delete_middle_singleton_stack():
    '''
        Test case for a stack with a single element.
        Verifies that deleting the middle element from a stack with 1 element 
        results in an empty stack.
    '''
    stack = Stack()
    stack.push(1)
    delete_middle(stack)
    assert stack.is_empty()

def test_delete_middle_two_element_stack():
    '''
        Test case for a stack with two elements.
        Verifies that deleting the middle element from a stack with 2 elements 
        results in a stack with the first element.
    '''
    stack = Stack()
    stack.push(1)
    stack.push(2)
    delete_middle(stack)
    assert str(stack) == "2"
