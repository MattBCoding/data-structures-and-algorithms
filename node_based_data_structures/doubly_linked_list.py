"""
One variant form of a linked-list is the doubly linked-list.
A doubly-linked-list is like a lined-list except that each node has two
links - one that points to the next node, and another that points to the
previous node. In addition, the doubly linked list always keeps track of
both the first and last nodes in the list, instead of just the first node.
This makes it easy to add and remove nodes from either end of the list.
Which makes them a good choice for implementing a Queue.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    def __init__(self, first_node, last_node):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, data):
        new_node = Node(data)
        # if the list is empty, make this the first node:
        if self.first_node is None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

    def remove_from_front(self):
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        return removed_node


class Queue(DoublyLinkedList):
    def __init__(self):
        super().__init__(None, None)

    def enqueue(self, data):
        self.insert_at_end(data)

    def dequeue(self):
        removed_node = self.remove_from_front()
        return removed_node.data
