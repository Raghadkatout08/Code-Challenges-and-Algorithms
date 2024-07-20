from challenge01 import TreeNode, has_pair_with_sum

def build_tree_from_list(values):
    """
    Build a binary tree from a list representation.
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

def test_case_1():
    """
    Test case 1: Check for pairs summing to 9 in the tree [5, 3, 6, 2, 4, None, 7].
    """
    root = build_tree_from_list([5, 3, 6, 2, 4, None, 7])
    assert has_pair_with_sum(root, 9) == True

def test_case_2():
    """
    Test case 2: Check for pairs summing to 17 in the tree [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13].
    """
    root = build_tree_from_list([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
    assert has_pair_with_sum(root, 17) == True

def test_case_3():
    """
    Test case 3: Check for pairs summing to 28 in the tree [5, 3, 6, 2, 4, None, 7].
    """
    root = build_tree_from_list([5, 3, 6, 2, 4, None, 7])
    assert has_pair_with_sum(root, 28) == False

def test_case_4():
    """
    Test case 4: Check for pairs summing to 5 in an empty tree.
    """
    root = build_tree_from_list([])
    assert has_pair_with_sum(root, 5) == False
