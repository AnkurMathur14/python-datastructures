"""
Implementation of stack data struction
Last in first out
"""

from node import Node


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        """
        Method to insert a new element into stack
        :param data:
        :return: None
        """
        new_node = Node(data)
        if self.empty():
            new_node.next = None
        else:
            new_node.next = self.head
        self.head = new_node
        return None

    def pop(self):
        """
        Method to return poped value
        :return: value if stack is not empty else None
        """
        if self.empty():
            return None
        to_delete = self.head
        self.head = to_delete.next
        data = to_delete.data
        del to_delete
        return data

    def size(self):
        """
        Method to return the size of stack
        :return: Number of elements present in stack
        """
        size = 0
        curr = self.head
        while curr:
            size += 1
            curr = curr.next
        return size

    def empty(self):
        """
        Method to check if stack is empty or not
        :return: True if empty else False
        """
        return True if not self.head else False

    def top(self):
        """
        Method to return the top element of stack
        :return: top element if not empty else None
        """
        return self.head.data if not self.empty() else None

    def print(self):
        """
        Method to print stack
        :return: None
        """
        curr = self.head
        while curr:
            print("|    {}  |".format(curr.data))
            curr = curr.next
        return None
