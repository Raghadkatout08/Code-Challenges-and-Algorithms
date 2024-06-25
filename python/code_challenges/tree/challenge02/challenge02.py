class Node:
    """
    A class used to represent a node in a binary tree.

    Attributes
    ----------
    value : int
        The value stored in the node.
    left : Node, optional
        A reference to the left child node (default is None).
    right : Node, optional
        A reference to the right child node (default is None).

    Methods
    -------
    __init__(self, value, left=None, right=None)
        Initializes the node with a value and optional left and right children.
    """
    
    def __init__(self, value, left= None, right= None):
        '''Initializes the node with a value and optional left and right children'''
        self.value = value 
        self.left = left 
        self.right= right 

class Tree:
    '''A class used to represent a binary tree.'''
    def isSameTree(self, p, q):
        '''Determines if two binary trees are the same using breadth-first traversal.'''
        if not p and not q:
            return True 
        if not p or not q:
            return False
        
        queue1 = [p]
        queue2 = [q]

        while queue1 and queue2:
            node1 = queue1.pop(0)
            node2 = queue2.pop(0)

            if node1.value != node2.value:
                return False
        
            left1, right1 = node1.left, node1.right 
            left2, right2 = node2.left, node2.right 

            if(left1 and not left2) or (not left1 and left2):
                return False 
            if(right1 and not right2) or (not right2 and right2):
                return False
        
            if left1: 
                queue1.append(left1)
            if  right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)
        return not queue1 and not queue2

# Example Usage 
tree = Tree()

# Test Case 1: Trees are the same
# Tree p: [1, 2, 3]
p1 = Node(1)
p1.left = Node(2)
p1.right = Node(3)

# Tree q: [1, 2, 3]
q1 = Node(1)
q1.left = Node(2)
q1.right = Node(3)

print(tree.isSameTree(p1, q1)) #output: True


# Test Case 2: Trees are different
# Tree p: [1, 2]
p2 = Node(1)
p2.left = Node(2)

# Tree q: [1, None, 2]
q2 = Node(1)
q2.right = Node(2)

print(tree.isSameTree(p2, q2)) #output:  False


# Test Case 3: Trees are different
# Tree p: [1, 2, 1]
p3 = Node(1)
p3.left = Node(2)
p3.right = Node(1)

# Tree q: [1, 1, 2]
q3 = Node(1)
q3.left = Node(1)
q3.right = Node(2)

print(tree.isSameTree(p3, q3))  # Output: False