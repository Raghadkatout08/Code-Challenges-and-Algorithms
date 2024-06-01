# Write here the code challenge solution
class Node: 
    """
        Initialize a new node with the given value and optional reference to the next node.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class MyQueue:
    def __init__(self):
        """
            Initialize an empty queue using two stacks.
        """
        self.stack1 = []
        self.stack2 = []
        self.size = 0 

    def push(self, x):
        """
            Pushes element x to the back of the queue.
        """
        self.stack1.append(x)
        self.size += 1

    def pop(self):
        """
            Removes the element from the front of the queue and returns it.
        """
        if not self.stack2:
            self._transfer_stack1_to_stack2()
        self.size -= 1
        return self.stack2.pop()

    def peek(self):
        """
            Returns the element at the front of the queue.
        """
        if not self.stack2:
            self._transfer_stack1_to_stack2()
        return self.stack2[-1]
    
    def empty(self):
        """
            Returns true if the queue is empty, false otherwise.
        """
        return self.size == 0
    
    def get_size(self):
        """
            Returns the size of the queue
        """
        return self.size
    
    def _transfer_stack1_to_stack2(self):
        """
            Transfers elements from stack1 to stack2.
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())


def print_colored(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',        
        'blue': '\033[94m',
        'yellow': '\033[93m',
        'end': '\033[0m',
    }
    print(f"{colors[color]}{text}{colors['end']}")

# Usage

if __name__ == "__main__":
    # Example usage and tests within the script
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    myQueue.push(3)

    print("Initial state:")
    print_colored(f"stack1: {myQueue.stack1}", 'blue')
    print_colored(f"stack2: {myQueue.stack2}", 'yellow')
    print(f"Size: {myQueue.get_size()}")

    # Peek operation
    peek_result = myQueue.peek()
    print("\nAfter Peek:")
    print(f"Peek Result: {peek_result}")
    print_colored(f"stack1: {myQueue.stack1}", 'blue')
    print_colored(f"stack2: {myQueue.stack2}", 'yellow')
    print(f"Size: {myQueue.get_size()}")

    # Pop operation
    pop_result = myQueue.pop()
    print("\nAfter Pop:")
    print(f"Pop Result: {pop_result}")
    print_colored(f"stack1: {myQueue.stack1}", 'blue')
    print_colored(f"stack2: {myQueue.stack2}", 'yellow')
    print(f"Size: {myQueue.get_size()}")

    # Empty check
    empty_result = myQueue.empty()
    color = 'green' if empty_result else 'red'
    print("")
    print_colored(f"Is Empty?: {empty_result}", color)
    print("")
    print_colored(f"stack1: {myQueue.stack1}", 'blue')
    print_colored(f"stack2: {myQueue.stack2}", 'yellow')
    print(f"Size: {myQueue.get_size()}")

    # Pop remaining elements
    pop_result = myQueue.pop()
    print("\nAfter Pop:")
    print(f"Pop Result: {pop_result}")
    print_colored(f"stack1: {myQueue.stack1}", 'blue')
    print_colored(f"stack2: {myQueue.stack2}", 'yellow')
    print(f"Size: {myQueue.get_size()}")

    pop_result = myQueue.pop()
    print("\nAfter Pop:")
    print(f"Pop Result: {pop_result}")
    print_colored(f"stack1: {myQueue.stack1}", 'blue')
    print_colored(f"stack2: {myQueue.stack2}", 'yellow')
    print(f"Size: {myQueue.get_size()}")

    # Final empty check
    empty_result = myQueue.empty()
    color = 'green' if empty_result else 'red'
    print("")
    print_colored(f"Is Empty after all pops?: {empty_result}", color)
    print("")
    print_colored(f"stack1: {myQueue.stack1}", 'blue')
    print_colored(f"stack2: {myQueue.stack2}", 'yellow')
    print(f"Size: {myQueue.get_size()}")

    print("")

    print("All operations completed.")