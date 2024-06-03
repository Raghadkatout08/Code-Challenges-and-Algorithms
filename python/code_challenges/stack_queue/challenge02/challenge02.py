"""
The problem is to determine if a string containing various types of brackets 
(parentheses, square brackets, and curly braces) has balanced brackets, 
meaning each opening bracket has a corresponding closing bracket and they are properly nested.
"""

class Node: 
    def __init__(self, value, next= None):
        """Initializes a new node with the given value and optional reference to the next node."""
        self.value = value 
        self.next = next
    
class Stack: 
    """A class representing a stack data structure using linked list."""
    def __init__(self):
        """Initializes an empty stack."""
        self.top = None 

    def push(self, new_value):
        """Pushes a new value onto the top of the stack."""
        new_node = Node(new_value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Removes and returns the value at the top of the stack."""
        if self.is_empty():
            return None
        
        popped_value = self.top.value 
        self.top = self.top.next
        return popped_value
        
    def is_empty(self):
        """Checks if the stack is empty."""
        return self.top is None
            

    

def is_valid(s):
    """Checks if the parentheses/brackets in the given string are balanced."""

    print("********************************************************************")
    print(f"Input string: {s}")
    bracket_pairs = { '(' : ')', '{' : '}', '[' : ']' }
    stack = Stack()

    for i, char in enumerate(s):
        if char in bracket_pairs.keys():
            stack.push(char)
            print(f"step {i+1}: Pushed '{char}' onto the stack")

        elif char in bracket_pairs.values():
            if stack.is_empty():
                print(f"step {i+1}: Found '{char}' but stack is empty, returning False")
                return False
            top_bracket = stack.pop()

            if bracket_pairs[top_bracket] != char:
                print(f"step {i+1}: Found '{char}' but top of stack is '{top_bracket}', returning False")
                print("\033[91m" + "Final Result: False" + "\033[0m")
                return False 
            
            print(f"step {i+1}: Popped '{top_bracket}' from the stack as it matches '{char}'")

            
    result = stack.is_empty()
    if result:
        print("\033[92m" + "Final Result: True" + "\033[0m")
    else:
        print("Final Result: False")
    return result

# Example usage:
print(is_valid("()"))   # Output: True()
print(is_valid("()[]{}"))   # Output: True
print(is_valid("[({}]"))   # Output: False
print(is_valid("[(hello)()]"))   # Output: True
print(is_valid("[{(())}]"))   # Output: True
print(is_valid("[(])"))    # Output: False
print(is_valid("([)]"))    # Output: False