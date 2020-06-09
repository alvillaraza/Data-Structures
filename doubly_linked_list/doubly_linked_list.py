"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        #if there is a previous item, take that previous item's next item and move it to the next-next item, so skip the middle
        if self.prev:
            self.prev.next = self.next
        #if there is a next item, take that next item's previous item to the previous-previous item, so skip the middle
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #create new_node
        new_node = ListNode(value, None, None)  #ListNode(value, prev, next)
        #check if empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            #set next (of the new_node) to current node
            new_node.next = self.head
            #set prev (of current head node) to new_node
            self.head.prev = new_node
            #set new_node to be the new head
            self.head = new_node
            #set length
            self.length = self.length + 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        #if there is only 1 element in the list, remove head and tail should be none also
        if self.head.next is None:
            #get reference to the head             
            head = self.head 
            #delete the head reference
            self.head = None 
            #there should be no tail
            self.tail = None 
            #return the value
            self.length = 0
            return head.value
        else:
            self.length -= 1
            head = self.head
            #remove the current head
            self.head = None
            #make current head's next node the new head of the list
            self.prev = None
            self.head = self.head.current_next
            #return value of removed Node
            return head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        #create new_node
        new_node = ListNode(value, None, None)
        #check if empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            #set prev of the new_node to the current old tail
            new_node.prev = self.tail
            #set the next of the current old tail to new_node
            self.tail.next = new_node
            #set new_node to be the new tail
            self.tail = new_node
            #set length
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.head and not self.tail:
           return None
        #if there is only 1 element on the list, remove head and tail should be none
        if self.head.next is None:
            #get reference to the head             
            head = self.head 
            #delete the head reference
            self.head = None 
            #there should be no tail
            self.tail = None 
            #return the value
            self.length = 0
            return head.value
        else:
            self.length -= 1
            tail = self.tail
            #remove current tail
            self.tail = None
            #make current tail's next node the new tail of the list
            self.next = None
            self.tail = self.tail.current_prev
            return tail

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.value
        # reference to our current node as we traverse the list
        current = self.head.next
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next
        return max_value
