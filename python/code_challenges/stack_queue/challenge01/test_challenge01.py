from challenge01 import MyQueue

def test_My_Queue():
    """Test cases for the MyQueue class."""
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    myQueue.push(3)

    # Test push operation
    assert myQueue.stack1 == [1, 2, 3]

    # Test peek operation
    assert myQueue.peek() == 1
    assert myQueue.stack1 == [] # Stack1 should be empty after peeking
    
    # Test pop operation
    assert myQueue.pop() == 1
    assert myQueue.stack2 == [3, 2]

    # Test Empty operation 
    assert not myQueue.empty() #Expected = False

    # pop remaining elements 
    assert myQueue.pop() == 2
    assert myQueue.pop() == 3

    # Test Empty operation after popping all elements
    assert myQueue.empty() #Expected = True