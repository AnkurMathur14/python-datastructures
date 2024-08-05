"""
Binary search tree implementation

In-order, Pre-order, and Post-order traversals are Depth-First traversals.

For a Graph, the complexity of a Depth First Traversal is O(n + m), where n is the number of nodes, and m is the number of edges.

Since a Binary Tree is also a Graph, the same applies here. The complexity of each of these Depth-first traversals is O(n+m).

Since the number of edges that can originate from a node is limited to 2 in the case of a Binary Tree, the maximum number of total edges in a Binary Tree is n-1, where n is the total number of nodes.

The complexity then becomes O(n + n-1), which is O(n).

Space complexity is O(h) where h is the height of the tree.
If the tree is balanced h = logn if skewed h = n
So if balanced  S: O(logn)

"""
import sys
from node import TreeNode
from q import Queue
from stack import Stack


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
        """
        Method to check if tree is empty
        :return: True if empty else False
        """
        return True if not self.root else False

    @staticmethod
    def __print_inorder(node):
        if not node:
            return None
        BSTree.__print_inorder(node.left)
        print(node.data)
        BSTree.__print_inorder(node.right)

    def print_inorder(self):
        """
        Method to print tree elements in in-order
        :return: None
        """
        BSTree.__print_inorder(self.root)

    @staticmethod
    def __print_postorder(node):
        if not node:
            return None

        BSTree.__print_postorder(node.left)
        BSTree.__print_postorder(node.right)
        print(node.data)

    def print_postorder(self):
        """
        Method to print tree elements in post order
        :return: None
        """
        BSTree.__print_postorder(self.root)

    @staticmethod
    def __print_preorder(node):
        if not node:
            return None

        print(node.data)
        BSTree.__print_preorder(node.left)
        BSTree.__print_preorder(node.right)

    def print_preorder(self):
        """
        Method to print tree elements in pre order
        :return: None
        """
        BSTree.__print_preorder(self.root)

    def print_preorder_iterative(self):
        """
        Method to print tree elements in pre order
        :return: None
        """
        if self.empty():
            print("Tree is empty")
            return None

        s = Stack()
        s.push(self.root)
        while not s.empty():
            node = s.pop()
            print(node.data, end= " ")
            if node.right:
                s.push(node.right)
            if node.left:
                s.push(node.left)

    def print_inorder_iterative(self):
        """
        Method to print tree elements in in-order
        :return: None
        """
        if self.empty():
            print("Tree is empty")
            return None

        s = Stack()
        curr = self.root
        print()
        while not s.empty() or curr:
            if curr:
                s.push(curr)
                curr = curr.left
            else:
                curr = s.pop()
                print(curr.data, end=" ")
                curr = curr.right

    def print_post_order_iterative(self):
        """
        Method to print tree elements in post order
        :return: None
        """
        if self.empty():
            print("Tree is empty")
            return None

        s1 = Stack()
        s2 = Stack()

        s1.push(self.root)
        while not s1.empty():
            node = s1.pop()
            s2.push(node)
            if node.left:
                s1.push(node.left)
            if node.right:
                s1.push(node.right)

        print()
        while not s2.empty():
            node = s2.pop()
            print(node.data, end=" ")

    def print_levelorder(self):
        """
        Method to print tree elements level wise
        :return: None
        """
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

    def print_level_order_reverse(self):
        """
        Method to print tree elements in reversed level order
        Bottom up
        :return: None
        """
        if self.empty():
            print("Tree is empty")
            return None

        s = Stack()
        q = Queue()
        q.push(self.root)
        while not q.empty():
            node = q.pop()
            s.push(node)
            if node.left:
                q.push(node.left)
            if node.right:
                q.push(node.right)

        print()
        while not s.empty():
            node = s.pop()
            print(node.data, end=" ")

    def print_level_order_spiral(self):
        """
        Method to print tree elements in spiral level order
        :return: None
        """
        if self.empty():
            print("Tree is empty")
            return None

        print()
        q = Queue()
        s = []
        q.push(self.root)
        reverse = True
        while not q.empty():
            n = q.size()
            s.clear()
            while n > 0:
                node = q.pop()
                if reverse:
                    s.append(node.data)
                else:
                    print(node.data, end=" ")
                if node.left:
                    q.push(node.left)
                if node.right:
                    q.push(node.right)
                n -= 1
            if reverse:
                while s:
                    d = s[-1]
                    s.pop()
                    print(d, end=" ")
            reverse = not reverse

    def print_left_view(self):
        """
        Method to print left view of the tree
        :return: None
        """
        if self.empty():
            return None
        q = Queue()
        q.push(self.root)
        while not q.empty():
            n = q.size()
            for i in range(n):
                curr = q.pop()
                if i == 0:
                    print(curr.data)
                if curr.left:
                    q.push(curr.left)
                if curr.right:
                    q.push(curr.right)

    def print_right_view(self):
        """
        Method to print right view of the tree
        :return: None
        """
        if self.empty():
            return None
        q = Queue()
        q.push(self.root)
        while not q.empty():
            n = q.size()
            for i in range(n):
                curr = q.pop()
                if i == 0:
                    print(curr.data)
                if curr.right:
                    q.push(curr.right)
                if curr.left:
                    q.push(curr.left)

    def print_levels(self):
        """
        Method to print nodes at all the levels one by one
        :return: None
        """
        if self.empty():
            return None
        q = Queue()
        q.push(self.root)
        level = 0
        while not q.empty():
            n = q.size()
            print("Level {}: ".format(level), end=" ")
            for i in range(n):
                curr = q.pop()
                print(curr.data, end=" ")
                if curr.left:
                    q.push(curr.left)
                if curr.right:
                    q.push(curr.right)
            level += 1
            print()

    @staticmethod
    def __print_at_kth_level(node, k):
        if not node:
            return None
        if k == 0:
            print(node.data, end=" ")
        BSTree.__print_at_kth_level(node.left, k - 1)
        BSTree.__print_at_kth_level(node.right, k - 1)

    def print_at_kth_level(self, k):
        """
        Method to print all the values at the given level k
        :param k: Level to be printed (0 for root level)
        :return: None
        """
        print("Level {}: ".format(k), end=" ")
        BSTree.__print_at_kth_level(self.root, k)

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
        """
        Method to insert a new value in the tress
        :param value: Value to insert
        :return: None
        """
        new_node = TreeNode(value)
        if self.empty():
            self.root = new_node
            return None

        curr = self.root
        while curr:
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
        """
        Method to remove given value from the tree
        :param value: Value to remove
        :return: None
        """
        self.root = BSTree.__remove(self.root, value)

    def create_tree(self, values):
        """
        Method to form a BST from set of values
        :param values: Values to insert
        :return: None
        """
        for value in values:
            # self.insert(value)
            self.insert_recursive(value)

    @staticmethod
    def __height(node):
        if not node:
            return 0

        return 1 + max(BSTree.__height(node.left), BSTree.__height(node.right))

    def height(self):
        """
        Method to calculate the height of the tree
        :return: Height of the tree
        """
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
        """
        Method to check the existence of the given element in the tree
        :param value: value to search
        :return: True if value found else False
        """
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
        """
        Method to find the minimum value in the tree
        :return: Min value
        """
        return BSTree.__min_value(self.root)

    @staticmethod
    def __max_value(node):
        if not node:
            return None
        if not node.right:
            return node.data
        return BSTree.__max_value(node.right)

    def max_value(self):
        """
        Method to find the maximum value in the tree
        :return: Max value
        """
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
        """
        Method to count the number of leaf nodes present in the tree
        :return: Count of leaf nodes
        """
        return BSTree.__count_leaf(self.root)

    @staticmethod
    def __sum_of_data(node):
        if not node:
            return 0

        return node.data + BSTree.__sum_of_data(node.left) + BSTree.__sum_of_data(node.right)

    def sum_of_data(self):
        """
        Method to calculate sum of oll the nodes of the tree
        :return: Sum of all nodes
        """
        return BSTree.__sum_of_data(self.root)

    @staticmethod
    def __height(node):
        if not node:
            return 0

        return 1 + max(BSTree.__height(node.left), BSTree.__height(node.right))

    def height(self):
        """
        Method to calculate the height of the tree
        :return: Height
        """
        return BSTree.__height(self.root)

    @staticmethod
    def __distance_from_root(root, value):
        """
        Method to find of distance of 'node' from 'root'
        :param root: Root node
        :param value: Node value for whoch the distance is to be calculated
        :return: Distance
        """
        if not root:
            return 0
        if root.data == value:
            return 0
        if value < root.data:
            return 1 + BSTree.__distance_from_root(root.left, value)
        return 1 + BSTree.__distance_from_root(root.right, value)

    @staticmethod
    def __distance_between_nodes(node, val1, val2):
        if not node:
            return 0
        # if both nodes lie in left tree
        if val1 < node.data and val2 < node.data:
            return BSTree.__distance_between_nodes(node.left, val1, val2)
        # if both nodes lie in right tree
        elif val1 > node.data and val2 > node.data:
            return BSTree.__distance_between_nodes(node.right, val1, val2)
        # if both nodes lie on either side of tree (i.e root is LCA for both of the nodes)
        return BSTree.__distance_from_root(node, val1) + BSTree.__distance_from_root(node, val2)

    def distance_between_nodes(self, val1, val2):
        return BSTree.__distance_between_nodes(self.root, val1, val2)

    @staticmethod
    def __invert_tree(node):
        if not node:
            return None
        node.left, node.right = node.right, node.left
        BSTree.__invert_tree(node.left)
        BSTree.__invert_tree(node.right)

    def invert_tree(self):
        """
        Method to invert the BST
        i.e make the tree as the mirror image of the original Tree
        :return: None
        """
        BSTree.__invert_tree(self.root)

    @staticmethod
    def __same_tree(tree1, tree2):
        if not (tree1 or tree2):
            return True
        if tree1 and not tree2:
            return False
        if not tree1 and tree2:
            return False
        if tree1.data != tree2.data:
            return False
        return BSTree.__same_tree(tree1.left, tree2.left) and BSTree.__same_tree(tree1.right, tree2.right)

    def same_tree(self, other_tree):
        """
        Method to check if the give tree is same as the current tree
        :param other_tree: root of the other tree
        :return: True if same else False
        """
        return BSTree.__same_tree(self.root, other_tree)

    @staticmethod
    def __sub_tree(tree1, tree2):
        if not (tree1 or tree2):
            return True
        if tree1 and not tree2:
            return True
        if not tree1 and tree2:
            return False

        if BSTree.__same_tree(tree1, tree2):
            return True
        return BSTree.__sub_tree(tree1.left, tree2) or BSTree.__sub_tree(tree1.right, tree2)

    def sub_tree(self, other_tree):
        """
        Method to check if the given tree is a subtree of the current tree
        :param other_tree:
        :return: True if subtree else False
        """
        return BSTree.__sub_tree(self.root, other_tree)

    @staticmethod
    def __symmetrical_tree(tree1, tree2):
        if not (tree1 or tree2):
            return True
        if tree1 and not tree2:
            return False
        if not tree1 and tree2:
            return False
        if tree1.data != tree2.data:
            return False
        return BSTree.__symmetrical_tree(tree1.left, tree2.right) and BSTree.__symmetrical_tree(tree1.right, tree2.left)

    def symmetrical_tree(self):
        """
        Method to check if the current tree is a valid symmetrical tree
        i.e Mirror image of tree is same as the original tree.
        :return: True if symmetrical else False
        """
        return BSTree.__symmetrical_tree(self.root.left, self.root.right)

    @staticmethod
    def __bst(node, prev):
        if not node:
            return True

        if not BSTree.__bst(node.left, prev):
            return False
        if prev and prev >= node.data:
            return False
        prev = node.data
        return BSTree.__bst(node.right, prev)

    def bst(self):
        """
        Method to check if the current tree is a valid BST
        :return: True if valid BST else False
        """
        return BSTree.__bst(self.root, None)

    @staticmethod
    def __lowest_common_ansestor(node, val1, val2):
        if not node:
            return None
        if val1 <= node.data and val2 >= node.data:
            return node
        if val1 < node.data and val2 < node.data:
            return BSTree.__lowest_common_ansestor(node.left, val1, val2)
        elif val1 > node.data and val2 > node.data:
            return BSTree.__lowest_common_ansestor(node.right, val1, val2)

    def lowest_common_ansestor(self, val1, val2):
        return BSTree.__lowest_common_ansestor(self.root, val1, val2)

    def lowest_common_ansestor2(self, val1, val2):
        if self.empty():
            return None
        max_val = max(val1, val2)
        min_val = min(val1, val2)
        curr = self.root
        while curr:
            if max_val < curr.data:
                curr = curr.left
            elif min_val > curr.data:
                curr = curr.right
            else:
                return curr.data
        return None

    @staticmethod
    def __max_path_sum(node):

        if not node:
            return -sys.maxsize
        if not node.left and not node.right:
            return node.data
        return node.data + max(BSTree.__max_path_sum(node.left), BSTree.__max_path_sum(node.right))

    def max_path_sum(self):
        if self.empty():
            return 0
        return BSTree.__max_path_sum(self.root)
