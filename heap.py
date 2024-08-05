"""
Heap Implementation
"""


class Heap:
    def __init__(self, elements=None, max_heap=False):
        self.heap = []
        self.max_heap = max_heap
        if elements:
            self.heap = self.build_heap(elements)

    def comparator(self, value1, value2):
        if self.max_heap:
            return value1 > value2
        return value1 < value2

    def __str__(self):
        return " -> ".join(map(lambda x: str(x), self.heap))

    def __repr__(self):
        return "Heap()"

    def __len__(self):
        return len(self.heap)

    def empty(self):
        """
        Method to check if heap is empty
        :return: True if empty else False
        """
        if not self.heap:
            return True
        return False

    def build_heap(self, elements):
        """
        Method to build head from list of elements
        # 1. get the last parent of the heap and shift it down
        # 2. Move upwards for other parents till reach the root node (including root node).
        :param elements: elements to insert
        :return: None
        """
        num_elements = len(elements)
        last_parent_idx = (num_elements - 2)//2
        current_idx = last_parent_idx
        while current_idx >= 0:
            self.sift_down(elements, current_idx, num_elements - 1)
            current_idx -= 1
        return elements

    def push(self, data):
        """
        Method to insert a new element in heap
        :param data: element to insert
        :return: None
        """
        self.heap.append(data)
        self.sift_up(self.heap, len(self.heap) - 1, 0)

    def pop(self):
        """
        Method to remove top most element from the heap
        :return: root element
        """
        if self.empty():
            print("Heap is empty")
            return None
        n = len(self.heap) - 1
        data = self.heap[0]
        self.heap[0], self.heap[n] = self.heap[n], self.heap[0]
        self.heap.pop()
        n = len(self.heap) - 1
        self.sift_down(self.heap, 0, n)
        return data

    def sift_up(self, elements, current_idx, end_idx):
        """
        Method to heapify down
        1. compare current element with parent element.
        2. if current is smaller then swap with parent.
        3. Update the index of current element with parent.
        4. Repeat step 1, 2, 3 untill current is larger than and equal to parent or root is reached
        :param elements: elements to hepify
        :param current_idx: Start Index (i.e. index of last inserted value)
        :param end_idx: Index of root
        :return: None
        """
        parent_idx = (current_idx - 1)//2
        while parent_idx >= end_idx and self.comparator(elements[current_idx], elements[parent_idx]):
            self.heap[parent_idx], elements[current_idx] = elements[current_idx], elements[parent_idx]
            current_idx = parent_idx
            parent_idx = (current_idx - 1)//2

    def sift_down(self, elements, current_idx, end_idx):
        """
        Method to heapify up
        1. Compare the current element with its children.
        2. If current element is larger than with any of the child then swap with the smallest child.
        3. Update the index of current element with child
        4. Repeat step 1, 2, 3 until current reaches the end.
        :param elements: elements to hepify
        :param current_idx: This is last parent index
        :param end_idx: End index (i.e. last index of heap array)
        T: O(LogN) | S: O(1)
        :return: None
        """
        child_one = 2 * current_idx + 1
        while child_one <= end_idx:
            child_two = 2 * current_idx + 2
            if child_two <= end_idx and self.comparator(elements[child_two], elements[child_one]):
                idx_to_swap = child_two
            else:
                idx_to_swap = child_one
            if self.comparator(elements[idx_to_swap], elements[current_idx]):
                elements[current_idx], elements[idx_to_swap] = elements[idx_to_swap], elements[current_idx]
            else:
                break
            current_idx = idx_to_swap
            child_one = 2 * current_idx + 1

    def top(self):
        """
        Method to return top most element of the heap
        :return: root element
        T: O(1) | S: O(1)
        """
        if self.empty():
            return None
        return self.heap[0]

    def get_heap(self):
        """
        Method to return the heap array
        :return: Heap array
        """
        return self.heap
