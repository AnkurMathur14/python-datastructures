"""
Circular list implementation
"""

from node import Node


class CircularList:
    def __init__(self, elements=None):
        self.head = None
        if elements:
            self.create_list(elements)

    def __repr__(self):
        return "CircularList()"

    def __str__(self):
        if self.empty():
            return "The list is empty."

        elements = []
        self.print(elements)
        return " -> ".join(elements)

    def __len__(self):
        return self.size()

    def __iter__(self):
        current = self.head
        yield current.data
        current = current.next
        while current != self.head:
            yield current.data
            current = current.next

    def empty(self):
        """
        Method to check if the list is empty or not
        :return: True if empty else False
        """
        if not self.head:
            return True
        return False

    def size(self):
        """
        Method to return size of the list
        :return: size
        """
        if self.empty():
            return 0

        curr = self.head
        curr = curr.next
        count = 1
        while curr != self.head:
            count += 1
            curr = curr.next
        return count

    def print(self, elements):
        if self.empty():
            print("List is empty")
            return None

        curr = self.head
        elements.append(str(curr.data))
        curr = curr.next
        while curr != self.head:
            elements.append(str(curr.data))
            curr = curr.next

    def create_list(self, elements):
        """
        Method to create list from multiple data values
        :param elements: List of data
        :return: None
        """
        for element in elements:
            self.insert_end(element)

    def insert_begin(self, data):
        """
        Method to insert data at the beginning of the list
        :param data: Data to insert
        :return: None
        """
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            # Reach to the tail (i.e. one prev to head)
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, data):
        """
        Method to insert data at the end of the list
        :param data: Data to insert
        :return: None
        """
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def remove_begin(self):
        """
        Method to remove data from the beginning of the list
        :return: Data to be removed
        """
        if self.empty():
            print("List is empty")
            return None

        to_delete = self.head
        # If there is only one node
        if to_delete.next == to_delete:
            self.head = None
            data = to_delete.data
            del to_delete
            return data

        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        to_delete = curr.next
        curr.next = to_delete.next
        self.head = to_delete.next
        data = to_delete.data
        del to_delete
        return data

    def remove_end(self):
        """
        Method to remove data from the end of the list
        :return: Data to be removed
        """
        if self.empty():
            print("List is empty")
            return None

        # If there is only one node
        if self.head.next == self.head:
            return self.remove_begin()

        curr = self.head
        while curr.next and curr.next.next != self.head:
            curr = curr.next
        to_delete = curr.next
        curr.next = to_delete.next
        data = to_delete.data
        del to_delete
        return data

    def search(self, value):
        """
        Method to check the existance of given value
        :param value: Value to check
        :return: True if exists else False
        """
        if self.empty():
            return False
        curr = self.head
        if curr.data == value:
            return True
        curr = curr.next
        while curr != self.head:
            if curr.data == value:
                return True
            curr = curr.next
        return False

