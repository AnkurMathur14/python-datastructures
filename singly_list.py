"""
Singly linked list implementation
"""

from node import Node


class SinglyList:
    def __init__(self, elements=None):
        self.head = None
        self.tail = None
        if elements:
            self.create_list(elements)

    def __len__(self):
        return self.size()

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return "({})".format(self.__class__.__name__)

    def __str__(self):
        if self.empty():
            return "The list is empty."

        elements = []
        curr = self.head
        SinglyList.__print_recursive(curr, elements)
        return " -> ".join(elements)

    @staticmethod
    def __search(node, value):
        if not node:
            return False
        if node.data == value:
            return True
        return SinglyList.__search(node.next, value)

    def search(self, value):
        return SinglyList.__search(self.head, value)

    @staticmethod
    def __print_recursive(node, elements):
        if not node:
            return None
        elements.append(str(node.data))
        SinglyList.__print_recursive(node.next, elements)

    @staticmethod
    def __size_recursive(node):
        """
        Method to return size of the list
        :return: size
        """
        if not node:
            return 0
        return 1 + SinglyList.__size_recursive(node.next)

    def size(self):
        """
        Method to return size of the list
        :return: size
        """
        return self.__size_recursive(self.head)

    def empty(self):
        """
        Method to check if the list is empty or not
        :return: True if empty else False
        """
        return True if not self.head else False

    def create_list(self, elements):
        """
        Method to create list from multiple data values
        :param elements: List of data
        :return: None
        """
        for data in elements:
            self.insert_end(data)

    def insert_begin(self, data):
        """
        Method to insert data at the beginning of the list
        :param data: Data to insert
        :return: None
        """
        new_node = Node(data)
        new_node.next = self.head
        if self.empty():
            self.tail = new_node
        self.head = new_node
        return None

    def insert_end(self, data):
        """
        Method to insert data at the end of the list
        :param data: Data to insert
        :return: None
        """
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return None

    def insert_after(self, data, value):
        """
        Method to insert data after the the given data value
        :param data: Data to insert
        :param value: Data value whose successor is to be inserted
        :return: None
        """
        new_node = Node(data)
        curr = self.head
        while curr:
            if curr.data == value:
                if curr == self.tail:
                    self.insert_end(data)
                else:
                    new_node.next = curr.next
                    curr.next = new_node
                break
            curr = curr.next
        else:
            print("Given value does not exists")
        return None

    def insert_before(self, data, value):
        """
        Method to insert data after the given data value
        :param data: Data to insert
        :param value: Data value whose predecessor is to be inserted
        :return: None
        """
        if self.empty():
            print("Given value does not exists.")
            return None

        if self.head.data == value:
            return self.insert_begin(data)

        new_node = Node(data)
        curr = self.head
        while curr.next:
            if curr.next.data == value:
                new_node.next = curr.next
                curr.next = new_node
                break
            curr = curr.next
        else:
            print("Given value does not exists.")
        return None

    def remove_begin(self):
        """
        Method to remove data from the beginning of the list
        :return: Data to be removed
        """
        if self.empty():
            return None

        to_delete = self.head
        if self.head == self.tail:
            self.tail = None
            self.head = None
        else:
            self.head = to_delete.next
        data = to_delete.data
        del to_delete
        return data

    def remove_end(self):
        """
        Method to remove data from the end of the list
        :return: Data to be removed
        """
        # If the list is empty
        if self.empty():
            return None

        # If there is only one element in the list
        if not self.head.next:
            to_delete = self.head
            self.head = None
            self.tail = None
            data = to_delete.data
            del to_delete
            return data

        curr = self.head
        while curr.next != self.tail:
            curr = curr.next

        to_delete = self.tail
        curr.next = None
        self.tail = curr
        data = to_delete.data
        del to_delete
        return data

    def remove_before(self, value):
        """
        Method to remove data before the given data value
        :param value: Data value whose predecessor is to be deleted
        :return: The data to be deleted
        """
        if self.empty():
            return None

        if self.head.data == value:
            print("Given value found but there is no node to delete before this value node")
            return None

        if self.head.next and self.head.next.data == value:
            return self.remove_begin()

        curr = self.head
        while curr.next.next:
            if curr.next.next.data == value:
                if curr.next.next == self.tail:
                    return self.remove_end()
                to_delete = curr.next
                curr.next = to_delete.next
                data = to_delete.data
                del to_delete
                return data
            curr = curr.next
        else:
            print("Given value does not exists.")
        return None

    def remove_after(self, value):
        """
        Method to remove data after the given data value
        :param value: Data value whose successor is to be deleted
        :return: The data to be deleted
        """
        if self.empty():
            print("List is empty")
            return None

        curr = self.head
        while curr:
            if curr.data == value:
                if curr == self.tail:
                    print("Given value found but there is no node to delete after this value node")
                    return None
                to_delete = curr.next
                data = to_delete.data
                curr.next = to_delete.next
                if to_delete == self.tail:
                    self.tail = curr
                del to_delete
                return data
            curr = curr.next
        else:
            print("Given value does not exists.")
        return None

    def reverse(self):
        """
        Method to reverse the list
        :return: None
        """
        if self.empty():
            return None

        pcurr = self.head
        pprev = None
        self.tail = self.head

        while pcurr:
            pnext = pcurr.next
            pcurr.next = pprev
            pprev = pcurr
            pcurr = pnext
        self.head = pprev

    @staticmethod
    def merge_two_lists(list1, list2):
        """
        Method too merge two list into one sorted list
        :param list1: First list
        :param list2: Second list
        :return: sorted list
        """

        if not list1 and not list2:
            return None

        if list1 and not list2:
            return list1

        if not list1 and list2:
            return list2

        head = None
        if list1.data <= list2.data:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        cur = head
        while list1 and list2:
            if list1.data <= list2.data:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return head

    @staticmethod
    def mid_node(node):
        if not node:
            return node

        slow = node
        fast = node

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    @staticmethod
    def merge_sort(node):

        # If there is less than 2 nodes
        if not node or not node.next:
            return node

        mid = SinglyList.mid_node(node)
        right_half = mid.next
        mid.next = None
        left_half = node

        left = SinglyList.merge_sort(left_half)
        right = SinglyList.merge_sort(right_half)

        sorted_list = SinglyList.merge_two_lists(left, right)
        return sorted_list

    def sort(self):
        self.head = SinglyList.merge_sort(self.head)
