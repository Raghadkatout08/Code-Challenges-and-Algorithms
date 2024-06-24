class Node:
    def __init__(self, value, left= None, right= None):
        '''Node class represents each node in a binary tree.'''
        self.value = value 
        self.left = left 
        self.right = right 

class Tree:
    '''Tree class represents a binary tree. ''' 
    def __init__(self):
        self.root = None

    def buildTree(self, preorder, inorder):
        '''Constructs a binary tree from given preorder and inorder traversals recursively.'''
        if not preorder or not inorder:
            return None 
    
        root_value = preorder[0]
        root = Node(root_value)

        root_index_inorder = inorder.index(root_value)

        root.left = self.buildTree(preorder[1:1 + root_index_inorder], inorder[:root_index_inorder])
        root.right = self.buildTree(preorder[1 + root_index_inorder:], inorder[root_index_inorder+1:])

        return root 
    
    def levelOrderTraversal(self, root):
        '''Performs level-order traversal of the binary tree.'''
        if not root: 
            return []
        
        queue = [root]
        result = []

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None: 
            result.pop()
        return result
    
# Example usage:

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

tree = Tree()
tree.root = tree.buildTree(preorder, inorder)

inorder_result = tree.levelOrderTraversal(tree.root)
print(f'Input: Preorder: {preorder} / Inorder: {inorder} \nOutput: {inorder_result}')