"""
A Queue is a data structure that stores items in a First In First Out (FIFO) manner.
Queues are similar to stacks, but they have a different set of rules.
They are arrays with the following three rules:
- Data can be inserted only at the end of a queue
- Data can be removed only from the front of a queue
- Only the first element of a queue can be read
"""


class Queue:
    def __init__(self):
        # create an empty list
        self.items = []

    def enqueue(self, item):
        # add the item to the end of the list
        self.items.append(item)

    def dequeue(self):
        # if the queue is not empty
        if not self.is_empty():
            # remove the first item from the list
            return self.items.pop(0)

    def read(self):
        # if the queue is not empty
        if not self.is_empty():
            # return the first item in the list
            return self.items[0]

    def is_empty(self):
        # return True if the queue is empty, False otherwise
        return len(self.items) == 0

    def get_queue(self):
        # return the queue
        return self.items


# test the queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print(q.get_queue())
first_item = q.dequeue()
print(first_item)
second_item = q.dequeue()
print(second_item)
print(q.get_queue())
print(q.is_empty())
third_item = q.dequeue()
print(third_item)
print(q.is_empty())
