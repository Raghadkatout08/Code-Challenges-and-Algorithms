import pytest 
from challenge04 import Tree

@pytest.fixture
def empty_tree():
    """
    Fixture that returns None to represent an empty tree.
    """
    return None

@pytest.fixture
def single_value_tree():
    """
    Fixture that builds a tree with a single node containing value 100.
    """
    return Tree.build_tree_from_list([100])

@pytest.fixture
def two_values_tree():
    """
    Fixture that builds a tree with two nodes: 50 (root) and 100 (right child).
    """
    return Tree.build_tree_from_list([50, 100])

@pytest.fixture
def best_case_tree():
    """
    Fixture that builds a balanced binary search tree with values: 
    [50, 25, 75, 12, 37, 63, 87, 6, 18, 31, 43, 56, 68, 81, 93]
    """
    return Tree.build_tree_from_list([50, 25, 75, 12, 37, 63, 87, 6, 18, 31, 43, 56, 68, 81, 93])

@pytest.fixture
def normal_case_tree():
    """
    Fixture that builds a binary search tree with values: [50, 25, 75, 12, 37, 63, 87]
    """
    return Tree.build_tree_from_list([50, 25, 75, 12, 37, 63, 87])

@pytest.fixture
def worst_case_tree():
    """
    Fixture that builds a binary search tree with values in descending order: 
    [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    """
    return Tree.build_tree_from_list([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])


def test_max_value_empty_tree(empty_tree):
    """
    Test case for finding the maximum value in an empty tree.

    Args:
    - empty_tree: Fixture representing an empty tree.

    Asserts:
    - Checks that the maximum value in the empty tree is float('-inf').
    """
    assert Tree.max_value(empty_tree) == float('-inf')

def test_max_value_single_value_tree(single_value_tree):
    """
    Test case for finding the maximum value in a tree with a single node.

    Args:
    - single_value_tree: Fixture representing a tree with a single node (value 100).

    Asserts:
    - Checks that the maximum value in the tree is 100.
    """
    assert Tree.max_value(single_value_tree) == 100

def test_max_value_two_values_tree(two_values_tree):
    """
    Test case for finding the maximum value in a tree with two nodes.

    Args:
    - two_values_tree: Fixture representing a tree with nodes [50, 100].

    Asserts:
    - Checks that the maximum value in the tree is 100.
    """

    assert Tree.max_value(two_values_tree) == 100 

def test_max_value_best_case_tree(best_case_tree):
    """
    Test case for finding the maximum value in a best-case scenario binary search tree.

    Args:
    - best_case_tree: Fixture representing a balanced binary search tree.

    Asserts:
    - Checks that the maximum value in the tree is 93.
    """


    assert Tree.max_value(best_case_tree) == 93

def test_max_value_normal_case_tree(normal_case_tree):
    """
    Test case for finding the maximum value in a normal-case binary search tree.

    Args:
    - normal_case_tree: Fixture representing a binary search tree.

    Asserts:
    - Checks that the maximum value in the tree is 87.
    """
    assert Tree.max_value(normal_case_tree) == 87

def test_max_value_worst_case_tree(worst_case_tree):
    """
    Test case for finding the maximum value in a worst-case scenario binary search tree.

    Args:
    - worst_case_tree: Fixture representing a binary search tree with values in descending order.

    Asserts:
    - Checks that the maximum value in the tree is 100.
    """
    assert Tree.max_value(worst_case_tree) == 100

def test_build_tree_from_list_empty():
    """
    Test case for building a tree from an empty list of nodes.

    Asserts:
    - Checks that the result of building a tree from an empty list is None.
    """
    assert Tree.build_tree_from_list([]) is None