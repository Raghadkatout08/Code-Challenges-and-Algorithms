'''
Delete Middle Node
This code implements a function to delete the middle element from a stack. It defines a Node class to create nodes
in the stack and a Stack class to represent the stack data structure. The delete_middle function calculates the
middle index of the stack, traverses to the middle element, and removes it from the stack.
'''

class Node:
    def __init__(self, value, next= None):
        ''' Initialize a Node with a value and a next pointer.'''
        self.value = value
        self.next = next 

class Stack:
    def __init__(self):
        '''Initialize an empty Stack.'''
        self.top = None
        
    def push(self, new_value):
        '''Push a new value onto the top of the stack.'''
        new_node = Node(new_value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        '''Remove and return the value at the top of the stack.'''
        if self.is_empty():
            return None
        
        popped = self.top
        self.top = self.top.next
        return popped.value
    
    def peek(self):
        '''Return the value at the top of the stack without removing it.'''
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        '''Check if the stack is empty.'''
        return self.top is None
    
    def __str__(self):
        '''Return a string representation of the stack.'''
        stack_str = ""
        current = self.top
        while current:
            stack_str += str(current.value) + " "
            current = current.next
        return stack_str.strip()

def delete_middle(stack):
    '''Delete the middle element from the stack.'''
    if stack.is_empty():
        return stack
    length = 0 
    current = stack.top
    while current:
        length += 1
        current = current.next
    middle_index = length // 2 
    current = stack.top
    prev = None 
    for _ in range(middle_index):
        prev = current
        current = current.next 

    if prev:
        prev.next = current.next

    else:
        stack.top = current.next
    
    return stack

# usage 

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Original stack:", stack)  # [5, 4, 3 ,2 ,1]

delete_middle(stack)

print("Modified stack:", stack) # [5, 4, 2 ,1]