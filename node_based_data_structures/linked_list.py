"""
Linked List - a node based data structure
each node has a value and a pointer to the next node, the pointer creates 
the link between the nodes. The last node points to None.
The first node is known as the head and the last node is known as the tail.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def read(self, index):
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            # we keep following the links of each node until we get to the
            # index we want:
            current_node = current_node.next_node
            current_index += 1
            if current_node is None:
                return None

        return current_node.data

    def index_of(self, value):
        current_node = self.first_node
        current_index = 0
        while current_node is not None:
            if current_node.data == value:
                return current_index
            current_node = current_node.next_node
            current_index += 1

        return None

    def insert_at_index(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        current_node = self.first_node
        current_index = 0
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete_at_index(self, index):
        if index == 0:
            self.first_node = self.first_node.next_node
            return

        current_node = self.first_node
        current_index = 0
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        current_node.next_node = current_node.next_node.next_node


# Testing:
node1 = Node("once")
node2 = Node("upon")
node3 = Node("a")
node4 = Node("time")

node1.next_node = node2
node2.next_node = node3
node3.next_node = node4
node4.next_node = None

my_list = LinkedList(node1)

print(my_list.read(2))
print(my_list.index_of("a"))
my_list.insert_at_index(4, "in")
print(my_list.read(4))
my_list.delete_at_index(4)
print(my_list.read(4))
