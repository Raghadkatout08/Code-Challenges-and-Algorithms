class Node:
    def __init__(self, value=0, left=None, right=None):
        """
        Initialize a node in the binary tree.

        :param value: The value of the node.
        :param left: The left child of the node.
        :param right: The right child of the node.
        """
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        """
        Initialize a binary tree with the given root node.

        :param root: The root node of the binary tree.
        """
        self.root = root

    def max_tree_height(self, node):
        """
        Compute the maximum height of the binary tree.

        :param node: The current node in the tree.
        :return: The maximum height of the tree.
        """
        if node is None:
            return -1
        left_height = self.max_tree_height(node.left)
        right_height = self.max_tree_height(node.right)
        return max(left_height, right_height) + 1

    def print_tree_structure(self):
        """
        Print the binary tree's structure in level-order traversal.
        """
        if self.root is None:
            print("The tree is empty.")
            return
        
        queue = [self.root]
        values = []
        
        while queue:
            node = queue.pop(0)
            values.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        print("Tree structure:", values)

# Example usage:
if __name__ == "__main__":
    #          10
    #        /    \
    #      20      30
    #     /  \    /  \
    #   40   28  27   50
    #  /
    # 29
    
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(28)
    root.right.left = Node(27)
    root.right.right = Node(50)
    root.left.left.left = Node(29)
    
    tree = Tree(root)
    
    tree.print_tree_structure()  # Output: Tree structure: [10, 20, 30, 40, 28, 27, 50, 29]
    
    height = tree.max_tree_height(tree.root)
    print("Height of the tree:", height)  # Output: Height of the tree: 3