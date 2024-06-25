import pytest
from challenge02 import Node, Tree

@pytest.fixture

def tree():
    """
    Fixture to create a Tree instance.
    
    Returns
    -------
    Tree
        An instance of the Tree class.
    """
    return Tree()

def test_same_trees(tree):
    '''Test case for trees that are structurally identical and have the same node values.'''
    # Tree p: [1, 2, 3]
    p1 = Node(1)
    p1.left = Node(2)
    p1.right = Node(3)

    # Tree q: [1, 2, 3]
    q1 = Node(1)
    q1.left = Node(2)
    q1.right = Node(3)
    
    assert tree.isSameTree(p1, q1) == True

def test_different_trees_structure(tree):
    '''Test case for trees that have different structures.'''
    # Tree p: [1, 2]
    p2 = Node(1)
    p2.left = Node(2)

    # Tree q: [1, None, 2]
    q2 = Node(1)
    q2.right = Node(2)

    assert tree.isSameTree(p2, q2) == False

def test_different_trees_values(tree):
    '''Test case for trees that have different node values.'''
    # Tree p: [1, 2, 1]
    p3 = Node(1)
    p3.left = Node(2)
    p3.right = Node(1)

    # Tree q: [1, 1, 2]
    q3 = Node(1)
    q3.left = Node(1)
    q3.right = Node(2)

    assert tree.isSameTree(p3, q3) == False

def test_empty_trees(tree):
    '''Test case for both trees being empty.'''
    # Both trees are empty
    assert tree.isSameTree(None, None) == True

def test_one_empty_tree(tree):
    '''Test case for one tree being empty and the other not.'''
    # Tree p: [1, 2, 3]
    p4 = Node(1)
    p4.left = Node(2)
    p4.right = Node(3)

    # Tree q: None
    q4 = None

    assert tree.isSameTree(p4, q4) == False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            