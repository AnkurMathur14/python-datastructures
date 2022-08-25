"""
Node classes for different data structures
"""


class Node:
    """
    Class for a list Node
    """
    def __init__(self, data, pnext=None):
        self.data = data
        self.next = pnext

    def __repr__(self):
        return "Node(data, pnext)"

    def __str__(self):
        return "{} {}".format(self.data, self.next)


class DoublyNode:
    """
    Class for a doubly list node
    """
    def __init__(self, data, pnext=None, pprev=None):
        self.data = data
        self.next = pnext
        self.prev = pprev

    def __repr__(self):
        return "DoublyNode(data, pnext, pprev)"

    def __str__(self):
        return "{} {}".format(self.data, self.next, self.prev)


class TreeNode(Node):
    """
    Class for a tree node
    """
    def __init__(self, data, pleft=None, pright=None):
        self.data = data
        self.left = pleft
        self.right = pright

    def __repr__(self):
        return "TreeNode(data, left, right)"

    def __str__(self):
        return "{} {}".format(self.data, self.left, self.right)


class TrieNode:
    def __init__(self):
        self.is_terminated = False
        self.children = [None] * 26

    def __repr__(self):
        return "{}".format(TrieNode.__class__.__name__)

    def __str__(self):
        return "{} {}".format(self.children, self.is_terminated)

    def __del__(self):
        for child in self.children:
            del child
