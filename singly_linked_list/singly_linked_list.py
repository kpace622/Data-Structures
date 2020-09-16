class Node: 
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def get_val(self):
        return self.value

    def get_next_node(self):
        return self.next_node 

    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        else:
          oldHead = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.get_next_node
        return oldHead

    def remove_tail(self):
      # Empty list? return None
       
      # list with 1 element remove item and update head and tail to be None

      # list with 2 or more elements update tail
      pass

    def contains(self, value):
      # loop through list until next pointer is None 
      current = self.head
      while current is not None:
          if current.get_val() == value:
              return True
      return False
          # if we find 'value'
              # return True

      # return False
      pass

    def get_max(self):
      pass
