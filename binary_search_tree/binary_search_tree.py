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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # if new_node value is less than the root value
        if value < self.value:
            # find out if there is already a value in left
            if self.left is None:
                # then go left
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        # if greater than...also the test (test file on line 22) asserts that a duplicate should be inserted on the right
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if root value equals the target, return true
        if self.value == target:
            return True
        # if value is greater than target,
        if self.value > target:
            #if there is a value on the right,
            if self.right:
                # then dismiss the right and recursively check down left
                return self.left.contains(target)
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
        #if there is no value, then return false
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if there is no right, the max value is the root value
        if self.right is None:
            return self.value
        # if there are items on the right,
        else:
            # get the max value of the items on the right
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # if self.left is None and self.right is None:
        #     return fn(self.value)
        # if self.left and not self.right:
        #     return fn(self.value), self.left.for_each(fn)
        # if self.right and not self.left:
        #     return fn(self.value), self.right.for_each(fn)
        # if self.left and self.right:
        #     return fn(self.value), self.left.for_each(fn), self.right.for_each(fn)

        #in BSTNode, value is not optional (it's not value=None on line 15), so value always exists
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        #lowest number is to the left of the tree
        #base case
        if node is None:
            return
        #recursive case
        else:
            
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
  
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #make pointer variable that updates at the beginning of each loop while you're iterating through
        q = []
        q.append(node)

        # #While loop that checks size of queue
        while len(q) > 0:
            #pop method returns the item that was popped
            node = q.pop(0)
            print(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    #not recursive, but iterative
        # #start queue with root node
        
         


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #stack
        #start stack with root node

        #while loop, while stack is not empty
            #use a pointer
        s = []
        s.append(node)

        # #While loop that checks size of queue
        while len(s) > 0:
            #pop method returns the item that was popped
            node = s.pop(-1)
            print(node.value)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BSTNode(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.bft_print(bst)