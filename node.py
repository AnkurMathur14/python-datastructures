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

