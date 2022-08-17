"""
Binary tree implemntation
"""

from node import TreeNode
from q import Queue


class BSTree:
    def __init__(self, elements=None):
        self.root = None
        if elements:
            self.create_tree(elements)

    def __repr__(self):
        return "BSTree()"

    def __str__(self):
        result = self.print_levelorder()
        return "\n".join(result)

    def __len__(self):
        return BSTree.__count(self.root)

    def __iter__(self):
        pass

    def empty(self):
        return True if not self.root else False

    @staticmethod
    def __print_inorder(node):
        if not node:
            return None
        BSTree.__print_inorder(node.left)
        print(node.data)
        BSTree.__print_inorder(node.right)

    def print_inorder(self):
        BSTree.__print_inorder(self.root)

    @staticmethod
    def __print_postorder(node):
        if not node:
            return None

        BSTree.__print_postorder(node.left)
        BSTree.__print_postorder(node.right)
        print(node.data)

    def print_postorder(self):
        BSTree.__print_postorder(self.root)

    @staticmethod
    def __print_preorder(node):
        if not node:
            return None

        print(node.data)
        BSTree.__print_preorder(node.left)
        BSTree.__print_preorder(node.right)

    def print_preorder(self):
        BSTree.__print_preorder(self.root)

    def print_levelorder(self):
        if self.empty():
            print("Tree is empty")
            return None

        curr = self.root
        q = Queue()
        q.push(curr)
        result = []
        while not q.empty():
            curr = q.front()
            q.pop()
            temp = f"{curr.data}: "
            if curr.left:
                temp += f"L:{curr.left.data} "
                q.push(curr.left)
            else:
                temp += f"L:None "
            if curr.right:
                temp += f"R:{curr.right.data}"
                q.push(curr.right)
            else:
                temp += f"R:None "
            result.append(temp)
        return result

    @staticmethod
    def __print_kth_level(node, k):
        if not node:
            return None

        if k == 1:
            print(node.data, end=" ")
        BSTree.__print_kth_level(node.left, k-1)
        BSTree.__print_kth_level(node.right, k-1)

    def print_kth_level(self, k):
        BSTree.__print_kth_level(self.root, k)
        print()

    @staticmethod
    def __insert_recursive(node, value):
        if not node:
            return TreeNode(value)

        if value < node.data:
            node.left = BSTree.__insert_recursive(node.left, value)
        else:
            node.right = BSTree.__insert_recursive(node.right, value)
        return node

    def insert_recursive(self, value):
        self.root = BSTree.__insert_recursive(self.root, value)

    def insert(self, value):
        new_node = TreeNode(value)
        if self.empty():
            self.root = new_node
            return None

        curr = self.root
        while True:
            if value < curr.data:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right
        return None

    @staticmethod
    def __remove(node, value):
        if not node:
            return node

        if value < node.data:
            node.left = BSTree.__remove(node.left, value)
        elif value > node.data:
            node.right = BSTree.__remove(node.right, value)
        else:
            # Node found. Standing at the node which is to be deleted

            # case1: If the node is leaf node
            if not (node.left or node.right):
                del node
                return None

            # case2: If the node only has left child
            # Assign left  tree to the parent
            if node.left and not node.right:
                temp = node.left
                node.left = None
                del node
                return temp

            # case3: If the node only has right child
            # Assign right tree to the parent
            if not node.left and node.right:
                temp = node.right
                node.right = None
                del node
                return temp

            # case4: If the node has both left and right children
            # Find max of the lest tree OR min of the right tree from the current node
            # Replace the current node's value with this min/mas value
            # Delete the node which has that min/max value.
            elif node.left and node.right:
                right_min = BSTree.__min_value(node.right)
                node.data = right_min
                node.right = BSTree.__remove(node.right, right_min)
        return node

    def remove(self, value):
        self.root = BSTree.__remove(self.root, value)

    def create_tree(self, values):
        for value in values:
            # self.insert(value)
            self.insert_recursive(value)

    @staticmethod
    def __height(node):
        if not node:
            return 0

        return 1 + BSTree.__height(node.left) + BSTree.__height(node.right)

    def height(self):
        return BSTree.__height(self.root)

    @staticmethod
    def __search(node, value):
        if not node:
            return False

        if node.data == value:
            return True

        if value < node.data:
            return BSTree.__search(node.left, value)
        else:
            return BSTree.__search(node.right, value)

    def search_recursive(self, value):
        return BSTree.__search(self.root, value)

    def search(self, value):
        if self.empty():
            return False

        curr = self.root
        while curr:
            if value < curr.data:
                curr = curr.left
            elif value > curr.data:
                curr = curr.right
            else:
                return True
        return False

    @staticmethod
    def __min_value(node):
        if not node:
            return None
        if not node.left:
            return node.data
        return BSTree.__min_value(node.left)

    def min_value(self):
        return BSTree.__min_value(self.root)

    @staticmethod
    def __max_value(node):
        if not node:
            return None
        if not node.right:
            return node.data
        return BSTree.__max_value(node.right)

    def max_value(self):
        return BSTree.__max_value(self.root)

    @staticmethod
    def __count(node):
        if not node:
            return 0

        return 1 + BSTree.__count(node.left) + BSTree.__count(node.right)

    @staticmethod
    def __count_leaf(node):
        if not node:
            return 0
        if not (node.left or node.right):
            return 1 + BSTree.__count_leaf(node.left) + BSTree.__count_leaf(node.right)

        return BSTree.__count_leaf(node.left) + BSTree.__count_leaf(node.right)

    def count_leaf(self):
        return BSTree.__count_leaf(self.root)

    @staticmethod
    def __sum_of_data(node):
        if not node:
            return 0

        return node.data + BSTree.__sum_of_data(node.left) + BSTree.__sum_of_data(node.right)

    def sum_of_data(self):
        return BSTree.__sum_of_data(self.root)

    @staticmethod
    def __height(node):
        if not node:
            return 0

        return 1 + max(BSTree.__height(node.left), BSTree.__height(node.right))

    def height(self):
        return BSTree.__height(self.root)
