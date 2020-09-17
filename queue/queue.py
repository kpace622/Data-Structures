"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from Node import Node

# Array Method

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def dequeue(self):
        # self.storage = self.storage - 1
        if len(self.storage) == 0:
            return None
        return self.storage.pop()

    def enqueue(self, value):
        # self.storage = self.storage + 1
        return self.storage.insert(0, value)


# Linked List Method

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        # self.storage = ?
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
            self.size = self.size + 1
        else:
            new_node.set_next_node(self.head)
            self.head = new_node
            self.size = self.size + 1

    def dequeue(self):
        if self.head is None:
            return None
        current = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size = self.size - 1
            return current.get_val()
        else: 
            previous = current
            while current.next_node is not None:
                previous = current
                current = current.next_node
            self.tail = previous
            self.tail.set_next_node(None)
            self.size = self.size - 1
            return current.get_val()

