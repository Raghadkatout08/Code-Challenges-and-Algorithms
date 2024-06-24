from challenge01 import Node, Tree

def test_tree_construction_normal():
    '''Test case for constructing a binary tree from preorder and inorder traversals.'''
    tree = Tree()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    tree.root = tree.buildTree(preorder, inorder)
    excepted_output = [3, 9, 20, None, None, 15, 7]

    assert tree.levelOrderTraversal(tree.root) == excepted_output
    
def test_tree_construction_empty():
    '''Test case for handling empty input lists in binary tree construction.'''
    tree = Tree()
    preorder = []
    inorder = []

    tree.root = tree.buildTree(preorder, inorder)
    expected_output = []
 
    assert tree.levelOrderTraversal(tree.root) == expected_output

def test_tree_construction_large():
    '''Test case for constructing a large binary tree from preorder and inorder traversals.'''
    tree = Tree()
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]

    tree.root = tree.buildTree(preorder, inorder)
    expected_output = [1, 2, 3, 4, 5, 6, 7]

    assert tree.levelOrderTraversal(tree.root) == expected_output

def test_tree_construction_missing_nodes():
    '''Test case for handling missing nodes in binary tree construction.'''
    tree = Tree()
    preorder = [1, 2, 4, 5, 3, 7]
    inorder = [4, 2, 5, 1, 3, 7]

    tree.root = tree.buildTree(preorder, inorder)
    expected_output = [1, 2, 3, 4, 5, None, 7]

    assert tree.levelOrderTraversal(tree.root) == expected_output