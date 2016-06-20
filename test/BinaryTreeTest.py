import unittest


import queue

from binary.BinaryTree import BinaryTree
from binary.Node import Node


class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.array = []
        self.parallel_array = queue.Queue()

    def helper_return(self, text):
        self.array.append(text)
        return text

    def test_binary_tree_object_created(self):
        self.assertIsNotNone(BinaryTree())

    def test_binary_tree_set_root(self):
        root = Node()
        tree = BinaryTree()
        tree.set_root(root)
        self.assertIsNotNone(tree.get_root())

    def test_get_tree_postfix(self):
        root = Node(function=self.helper_return, args=1)
        child_left = Node(function=self.helper_return, args=2)
        child_right = Node(function=self.helper_return, args=3)
        root.add(child_left)
        root.add(child_right)
        tree = BinaryTree()
        tree.set_root(root)
        tree.postfix(parallel=False)
        self.assertItemsEqual([2, 3, 1], self.array)

    def test_get_tree_complicated_postfix(self):
        root = Node(function=self.helper_return, args=1)
        child11 = Node(function=self.helper_return, args=11)
        child111 = Node(function=self.helper_return, args=111)
        child112 = Node(function=self.helper_return, args=112)

        child12 = Node(function=self.helper_return, args=12)
        child123 = Node(function=self.helper_return, args=123)
        child1234 = Node(function=self.helper_return, args=1234)

        child123.add(child1234)
        child12.add(child123)
        child11.add(child111)
        child11.add(child112)
        root.add(child11)
        root.add(child12)

        tree = BinaryTree()
        tree.set_root(root)
        tree.postfix(parallel=False)
        self.assertItemsEqual([111, 112, 11, 1234, 123, 12, 1], self.array)


if __name__ == '__main__':
    unittest.main()
