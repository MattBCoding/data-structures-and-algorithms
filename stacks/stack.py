"""
Stacks store data in the same way as arrays, but they have a different set of
rules.
Stacks are a LIFO data structure - Last In, First Out.
- Data can be inserted only at the end of a stack
- Data can be removed only from the end of a stack
- Only the last element of a stack can be read
"""


# create a stack class
class Stack:
    # initialize the stack
    def __init__(self):
        # create an empty list
        self.items = []

    # push method - adds an item to the end of the stack
    def push(self, item):
        # add the item to the end of the list
        self.items.append(item)

    # pop method - removes an item from the end of the stack
    def pop(self):
        # if the stack is not empty
        if not self.is_empty():
            # remove the last item from the list
            return self.items.pop()

    # read method - returns the last item in the stack
    def read(self):
        # if the stack is not empty
        if not self.is_empty():
            # return the last item in the list
            return self.items[-1]

    # is_empty method - returns True if the stack is empty, False otherwise
    def is_empty(self):
        # return True if the stack is empty, False otherwise
        return len(self.items) == 0

    # get_stack method - returns the stack
    def get_stack(self):
        # return the stack
        return self.items
