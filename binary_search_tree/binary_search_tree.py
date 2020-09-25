"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
from collections import deque

class Node: 
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_val(self):
        return self.value

    def get_next_node(self):
        return self.next_node 

    def set_next_node(self, new_next):
        self.next_node = new_next

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def pop(self):
        # self.storage = self.storage - 1
        if len(self.storage) == 0:
            return None
        return self.storage.pop()

    def push(self, value):
        # self.storage = self.storage + 1
        return self.storage.append(value)

# Linked List method
        
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



class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
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

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    # Insert the given value into the tree
    def insert(self, value):

        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            
            elif value >= self.value:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)


    def contains(self, target):

        if target == self.value: 
            return True
        else:
            if target < self.value:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)
            elif target >= self.value:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):

        if self.right is None:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

        
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Left Root Right

        # Recursive
        if self.left:
            self.left.in_order_print()
        print(self.value)   
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):

        q = Queue()
        q.enqueue(self)
        while len(q) != 0:
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
            print(current.value)
        
        # Queue FIFO
        # Create a Queue to keep track of nodes
        # insert self onto beginning of Queue

        # while something still in Queue
            # add left and right if exist to the queue
            # print and remove first node

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):

        s = Stack()
        s.push(self)
        while s.size != 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.push(current.left)
            if current.right:
                s.push(current.right)

        # stack FIFO
        # create a stack to keep track of nodes we are processing
        # push 'self' into stack
        
        # while something still in the stack (not done processing all nodes)
            # use existing 'for_each' as a reference for traversal logic
            # push weh nwe START, pop when a node is DONE
            # and don't forget to call 'print()'
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  

