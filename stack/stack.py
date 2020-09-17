"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from Node import Node
        
class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        # self.storage = ?

    def __len__(self):
        return self.size

    def push(self, val):
        newNode = Node(val)
        if(self.head == None): 
            self.head = newNode
            self.tail = newNode
            self.size = self.size +1
        else:
            oldHead = self.head
            self.head = newNode
            self.head.next_node = oldHead
            self.size = self.size +1

    def pop(self):
        if not self.head:
            return None
        oldNode = self.head.value
        if(self.head == self.tail):
            self.tail = None
        self.head = self.head.next_node
        self.size = self.size - 1
        return oldNode

