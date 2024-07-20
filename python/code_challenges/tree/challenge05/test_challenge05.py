import pytest
from challenge05 import Node, Tree

def test_max_tree_height():
    """
    Test case for a tree with a mixed structure.
    The height of this tree is 3.
    """
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(28)
    root.right.left = Node(27)
    root.right.right = Node(50)
    root.left.left.left = Node(29)
    
    tree = Tree(root)
    assert tree.max_tree_height(tree.root) == 3


def test_max_tree_height_case2():
    """
    Test case for a balanced tree with 3 levels.
    The height of this tree is 2.
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    tree = Tree(root)
    assert tree.max_tree_height(tree.root) == 2

def test_max_tree_height_case3():
    """
    Test case for a left-skewed tree with a single branch.
    The height of this tree is 3.
    """
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.left.left = Node(4)
    
    tree = Tree(root)
    assert tree.max_tree_height(tree.root) == 3

def test_max_tree_height_empty():
    """
    Test case for an empty tree.
    The height of an empty tree is -1.
    """
    root = None
    tree = Tree(root)
    assert tree.max_tree_height(tree.root) == -1