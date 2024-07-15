import pytest
from challenge03 import Tree, TreeNode, print_tree

@pytest.mark.parametrize("nums, expected_output", [
    ([-10, -3, 0, 5, 9], "[0, -10, 5, null, -3, null, 9]"),
    ([1, 3], "[1, null, 3]"),
    ([1, 2, 3, 4, 5, 6, 7], "[4, 2, 6, 1, 3, 5, 7]"),
    ([-5, -3, -1, 0, 2, 4, 6], "[0, -3, 4, -5, -1, 2, 6]"),
])

def test_sortedArrayToBST(nums, expected_output):
    tree = Tree()
    root = tree.sortedArrayToBST(nums)
    output = print_tree(root)
    assert output == expected_output, f"Expected {expected_output}, but got {output}"