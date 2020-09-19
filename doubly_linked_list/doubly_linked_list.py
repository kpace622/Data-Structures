"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        if self.prev:
            if self.next is None:
                self.tail = self.prev
            else:
                self.next.prev = self.prev
        if self.next:
            if self.prev is None:
                self.head = self.next
            else:
                self.prev.next = self.next

    def get_value(self):
        return self.value
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return
        
        oldHead = self.head.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return oldHead
        else:
            oldHead = self.head.get_value()
            self.head = self.head.next
            return oldHead

        self.length -= 1
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return
        
        oldTail = self.tail.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1 
            return oldTail
        else:
            self.tail.prev.next = None 
            self.tail.prev = self.tail
            self.length -= 1
            return oldTail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete() # updating prev and/or next pointers
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

        self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        max_num = current.get_value()
        while current is not None:
            if current.get_value() > max_num:
                max_num = current.get_value()
            current = current.next
        return max_num
