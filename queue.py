"""
Implementation of queue data structure
First in first out
"""

from node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        """
        Method to check if queue is empty or not
        :return: True if empty else False
        """
        return True if not self.head else False

    def size(self):
        """
        Method to return number of elements in the queue
        :return: size
        """
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def front(self):
        """
        Method to return front element of the queue
        :return: Front element if not empty else None
        """
        if not self.empty():
            return self.head.data
        return None

    def back(self):
        """
        Method to return back element of the queue
        :return: Back element if not empty else None
        """
        if not self.empty():
            return self.tail.data
        return None

    def push(self, data):
        """
        Method to insert an element into queue
        :param data: Data to insert
        :return: None
        """
        new_node = Node(data, None)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return None

    def pop(self):
        """
        Method to remove element from the queue
        :return: element if not empty else None
        """
        if self.empty():
            return None

        to_delete = self.head
        self.head = to_delete.next
        if not self.head:
            self.tail = None

        data = to_delete.data
        del to_delete
        return data

    def print(self):
        """
        Method to print the queue content
        :return: None
        """
        curr = self.head
        while curr:
            print("|    {}  |".format(curr.data, ret='\r'))
            curr = curr.next
        return None
