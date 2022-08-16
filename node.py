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
        self.pleft = pleft
        self.pright = pright

    def __repr__(self):
        return "TreeNode(data, pleft, pright)"

    def __str__(self):
        return "{} {}".format(self.data, self.pleft, self.pright)

