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

#using array
class StackArray:
    def __init(self):
        self.size = 0
        self.storage = list()
        self.maxSize = 10
        self.top = 0
    
    def __len__(self):
        return self.top
    
    def push(self, value):
        if self.top >= self.maxSize:
            return ("stack full")
        else:
            self.storage.append(value)
            self.top += 1
            return True
    
    def pop(self):
        if self.top <= 0:
            return ("stack empty")
        else:
            item = self.storage.pop()
            self.top -= 1
            return item
        

# Using linked list
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.value
    def set_next(self, new_next):
        self.next_node = new_next
class StackLinkedList:
    def __init__(self):
        self.size = 0
        self.storage = list()
        self.head = None
        self.tail = None

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        new_node = Node(value, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            
        

    def pop(self):
        if self.head is None:
            return None
        if self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()

        value = self.head.get_value()
        self.head = self.head.get_next()
        return value
        
