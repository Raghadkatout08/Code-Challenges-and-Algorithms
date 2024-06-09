'''
    Test module for the Queue data structure implementation in challenge04.py.
'''

import pytest
from challenge04 import Node, Queue

@pytest.fixture
def empty_queue():
    """
        Fixture to create an empty Queue instance.
    """
    return Queue()

@pytest.fixture
def filled_queue():
    """
        Fixture to create a Queue instance with elements [1, 2, 3, 4, 5].
    """
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)
    return q

def test_enqueue(empty_queue):
    """
        Test case to verify enqueue operation.
    """
    assert empty_queue.is_empty() == True
    empty_queue.enqueue(1)
    assert empty_queue.is_empty() == False

def test_dequeue(filled_queue):
    """
        Test case to verify dequeue operation.
    """
    assert filled_queue.is_empty() == False
    assert filled_queue.dequeue() == 1
    assert filled_queue.dequeue() == 2
    assert filled_queue.dequeue() == 3
    assert filled_queue.is_empty() == False
    assert filled_queue.dequeue() == 4
    assert filled_queue.dequeue() == 5
    assert filled_queue.is_empty() == True

def test_reverse(filled_queue):
    """
        Test case to verify dequeue operation.
    """
    assert filled_queue.is_empty() == False
    filled_queue.reverse_queue()
    assert filled_queue.dequeue() == 5
    assert filled_queue.dequeue() == 4
    assert filled_queue.dequeue() == 3
    assert filled_queue.dequeue() == 2
    assert filled_queue.dequeue() == 1
    assert filled_queue.is_empty() == True
