"""
This code defines a Queue data structure implemented using linked lists, along with methods to manipulate the queue,
including enqueue, dequeue, display, and reverse_queue. It also includes a Node class representing individual elements
in the queue.
This code demonstrates how to reverse the order of elements in a queue using a linked list implementation.
"""
class Node:
    def __init__(self, value, next=None):
        '''Initializes a new node with the given value and next reference.'''
        self.value = value 
        self.next = next 

class Queue:
    def __init__(self):
        '''Initializes an empty queue with front and rear pointers.'''
        self.front = None 
        self.rear = None

    def is_empty(self):
        '''Checks if the queue is empty.'''
        return self.front is None 
    
    def enqueue(self, value):
        '''Adds a new element to the rear of the queue.'''
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node 

        else:
            self.rear.next = new_node 
            self.rear = new_node

    def dequeue(self):
        '''Removes and returns the element from the front of the queue.'''
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        temp = self.front 
        self.front = self.front.next 
        if self.front is None: 
            self.rear = None 
        return temp.value
    
    def display(self):
        '''Displays the elements of the queue.'''
        current = self.front 
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print(" ".join(map(str, elements)))
    
    def reverse_queue(self):
        '''Reverses the order of elements in the queue.'''
        stack = []
        while not self.is_empty():
            stack.append(self.dequeue())
        while stack:
            self.enqueue(stack.pop())
            
# Example usage:
queue = Queue()
for i in range(1, 6):
    queue.enqueue(i)

print("Original Queue: ", end="")
queue.display()

queue.reverse_queue()

print("Reversed Queue: ", end="")
queue.display()