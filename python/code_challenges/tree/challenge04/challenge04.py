class Node:
    def __init__(self, value= 0, left=None, right=None):
        """
        Initialize a node in a binary tree.

        Args:
        - value (int): The value held by the node.
        - left (Node): The left child node.
        - right (Node): The right child node.
        """
        self.value = value 
        self.left = left
        self.right = right

class Tree: 
    @staticmethod
    def max_value(root):
        """
        Find the maximum value in a binary tree using inorder traversal.

        Args:
        - root (Node): The root node of the binary tree.

        Returns:
        - int: The maximum value found in the tree.
        """
        def inorder_traversal(node):
            """
            Perform inorder traversal to find the maximum value recursively.

            Args:
            - node (Node): Current node in the traversal.

            Returns:
            - int: Maximum value found in the subtree rooted at `node`.
            """
            if not node:
                return float('-inf')
            left_max = inorder_traversal(node.left)
            right_max = inorder_traversal(node.right)

            return max(left_max, node.value, right_max)
        
        return inorder_traversal(root)
    
    @staticmethod
    def build_tree_from_list(nodes):
        """
        Build a binary tree from a list of node values using recursive helper function.

        Args:
        - nodes (list): List of node values representing the tree in level order.

        Returns:
        - Node: The root node of the constructed binary tree.
        """
        if not nodes:
            return None
        
        def build_tree_helper(index):
            """
            Recursively build the binary tree from the list of node values.

            Args:
            - index (int): Current index in the list representing the tree.

            Returns:
            - Node: The constructed node at the current index.
            """
            if index < len(nodes) and nodes[index] is not None:
                node = Node(nodes[index])
                node.left = build_tree_helper(2 * index + 1)
                node.right = build_tree_helper(2 * index + 2)
                return node
            return None
        
        return build_tree_helper(0)
    

# Example Usage
node_values1 = [1000, 500, 2000, 250, 600, 12000]
root = Tree.build_tree_from_list(node_values1)
print("Node values: " , node_values1)
print("Maximum value in the tree:", Tree.max_value(root))  # Output: 12000
print("------------------------------------------------------")
node_values2 = []
root = Tree.build_tree_from_list(node_values2)
print("Node values2: " , node_values2)
print("Maximum value in the tree2:", Tree.max_value(root))  # Output: -inf
