"""
LRU cache implementation
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoublyList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.empty():
            return "The list is empty."

        elements = []
        curr = self.head
        DoublyList.__print_recursive(curr, elements)
        return " -> ".join(elements)

    @staticmethod
    def __print_recursive(node, elements):
        if not node:
            return None
        elements.append(str(node.key))
        DoublyList.__print_recursive(node.next, elements)

    def empty(self):
        if not self.head:
            return True
        return False

    def insert_head(self, new_node):
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

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
        node = to_del
        del to_del
        return node

    def remove_end(self):
        if self.empty():
            return None

        to_del = self.tail

        # If there is only one node
        if to_del == self.head:
            return self.remove_begin()

        self.tail.prev.next = None
        self.tail = self.tail.prev
        node = to_del
        del to_del
        return node

    def remove_node(self, node):
        if not node:
            return None

        if node == self.tail:
            return self.remove_end()

        if node == self.head:
            return self.remove_begin()

        node_next = node.next
        node_prev = node.prev
        if node_prev:
            node_prev.next = node_next
        if node_next:
            node_next.prev = node_prev

        to_delete = node
        del to_delete
        return node


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lru_cache = dict()
        self.lru_list = DoublyList()
        self.cache_size = 0

    def __repr__(self):
        return "{}()".format(LRUCache.__class__.__name__)

    def __str__(self):
        return self.lru_list.__str__()

    def __iter__(self):
        self.lru_list.__iter__()

    def evict_least_recent(self):
        oldest_entry = self.lru_list.remove_end()
        self.lru_cache.pop(oldest_entry.key)

    def update_most_recent(self, node):
        self.lru_list.remove_node(node)
        self.lru_list.insert_head(node)

    def put(self, key, value):

        # If key is not present in the cache, then insert a new entry
        if key not in self.lru_cache:
            # if cache is already full
            if self.cache_size == self.capacity:
                self.evict_least_recent()
            # If cache is not full
            else:
                self.cache_size += 1

            new_node = Node(key, value)
            self.lru_cache[key] = new_node

        # If key already present in the cache, then overwrite its value
        else:
            self.lru_cache[key].value = value
        self.update_most_recent(self.lru_cache[key])
        return None

    def get(self, key):
        if key in self.lru_cache:
            self.update_most_recent(self.lru_cache[key])
            return self.lru_cache[key].value
        return -1
