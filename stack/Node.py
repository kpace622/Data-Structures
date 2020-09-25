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
          oldHead = self.head.get_val()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.get_next_node()
        return oldHead

    def remove_tail(self):
        if self.head is None:
            return None
        current = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return current.get_val()
        else: 
            previous = current
            while current.next_node is not None:
                previous = current
                current = current.next_node
            self.tail = previous
            self.tail.set_next_node(None)

            if self.head == self.tail:
                self.tail = None
                self.head = None
                return current.get_val()
            return current.get_val()

    def contains(self, value):
      current = self.head
      while current is not None:
          if current.get_val() == value:
              return True
      return False

    def get_max(self):
        current = self.head
        max_num = current.get_val()
        while current is not None:
            if current > max_num:
                max_num = current
            current = current.next_node
        return max_num
