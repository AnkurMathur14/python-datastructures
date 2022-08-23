"""
Implementation of doubly linked list
"""
from node import DoublyNode


class DoublyList:
    def __init__(self, elements=None):
        self.head = None
        self.tail = None
        if elements:
            self.create_list(elements)

    def __repr__(self):
        return "({})".format(self.__class__.__name__)

    def __str__(self):
        if self.empty():
            return "The list is empty."

        elements = []
        curr = self.head
        DoublyList.__print_recursive(curr, elements)
        return " -> ".join(elements)

    def __len__(self):
        return self.size()

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def empty(self):
        """
        Method to check if the list is empty
        :return: True if empty else False
        """
        if not self.head:
            return True
        return False

    @staticmethod
    def __size(node):
        if not node:
            return 0
        return 1 + DoublyList.__size(node.next)

    def size(self):
        """
        Method to get size if the list
        :return: Size of the list
        """
        return DoublyList.__size(self.head)

    @staticmethod
    def __print_recursive(node, elements):
        if not node:
            return None
        elements.append(str(node.data))
        DoublyList.__print_recursive(node.next, elements)

    def create_list(self, elements):
        """
        Method to create list from list of elements
        :param elements: List of elements
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
        new_node = DoublyNode(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return None

    def insert_end(self, data):
        """
        Method to insert data at the end of the list
        :param data: Data to insert
        :return: None
        """
        new_node = DoublyNode(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return None

    def insert_after(self, data, value):
        """
        Method to insert data after the the given data value
        :param data: Data to insert
        :param value: Data value whose successor is to be inserted
        :return: None
        """
        new_node = DoublyNode(data)
        curr = self.head
        while curr:
            if curr.data == value:
                if curr == self.tail:
                    self.insert_end(data)
                else:
                    new_node.next = curr.next
                    new_node.prev = curr
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
            print("Given value does not exists")
            return None

        new_node = DoublyNode(data)
        curr = self.head
        while curr:
            if curr.data == value:
                if curr == self.head:
                    self.insert_begin(data)
                else:
                    curr.prev.next = new_node
                    new_node.next = curr
                    new_node.prev = curr.prev
                    curr.prev = new_node
                break
            curr = curr.next
        else:
            print("Given value does not exists")
        return None

    def remove_begin(self):
        """
        Method to remove data from the beginning of the list
        :return: Data to be removed
        """
        if self.empty():
            print("List is empty")
            return None

        to_del = self.head
        self.head = to_del.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        data = to_del.data
        del to_del
        return data

    def remove_end(self):
        """
        Method to remove data from the end of the list
        :return: Data to be removed
        """
        # If the list is empty
        if self.empty():
            print("List is empty")
            return None

        to_del = self.tail

        # If there is only one node
        if to_del == self.head:
            return self.remove_begin()

        self.tail.prev.next = None
        self.tail = self.tail.prev
        data = to_del.data
        del to_del
        return data

    def remove_before(self, value):
        """
        Method to remove data before the given data value
        :param value: Data value whose predecessor is to be deleted
        :return: The data to be deleted
        """
        if self.empty():
            print("List is empty")
            return None

        curr = self.head
        while curr:
            if curr.data == value:

                # Matched with first node
                if curr == self.head:
                    print("Given value found but there is no node to delete before this value node")
                    return None

                # Matched with second node
                if not curr.prev.prev:
                    return self.remove_begin()

                to_del = curr.prev
                to_del.prev.next = curr
                curr.prev = to_del.prev
                data = to_del.data
                del to_del
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

                # Matched with the tail  node
                if curr == self.tail:
                    print("Given value found but there is no node to delete after this value node")
                    return None

                to_del = curr.next

                # Node to be deleted is tail node
                if to_del == self.tail:
                    return self.remove_end()

                curr.next = to_del.next
                to_del.next.prev = curr
                data = to_del.data
                del to_del
                return data
            curr = curr.next
        else:
            print("Given value does not exists.")
        return None

    def reverse(self):
        """
        Method to reverse the list
        :return None
        """
        if self.empty():
            return None

        pcurr = self.head
        pprev = None
        self.tail = self.head

        while pcurr:
            pnext = pcurr.next
            pcurr.next = pprev
            pcurr.prev = pnext
            pprev = pcurr
            pcurr = pnext
        self.head = pprev

    @staticmethod
    def __mid_node(node):
        if not node:
            return None

        slow = node
        fast = node

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def mid_node(self):
        return DoublyList.__mid_node(self.head)

    @staticmethod
    def __merge_two_lists(list1, list2):
        if not (list1 or list2):
            return None
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2

        head = None
        if list1.data < list2.data:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        curr = head

        while list1 and list2:
            if list1.data < list2.data:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return head

    @staticmethod
    def __merge_sort(node):
        # If empty or single node
        if not node or not node.next:
            return node

        mid = DoublyList.__mid_node(node)
        right_half = mid.next
        mid.next = None
        left_half = node

        left = DoublyList.__merge_sort(left_half)
        right = DoublyList.__merge_sort(right_half)
        sorted_list = DoublyList.__merge_two_lists(left, right)
        return sorted_list

    def sort(self):
        self.head = DoublyList.__merge_sort(self.head)

    @staticmethod
    def __search(node, value):
        if not node:
            return False
        if node.data == value:
            return True
        return DoublyList.__search(node.next, value)

    def search(self, value):
        return DoublyList.__search(self.head, value)

