import unittest


from binary.Node import Node


class NodeTest(unittest.TestCase):
    def test_create_node_object(self):
        node = Node()
        self.assertIsNotNone(node)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_add_node(self):
        parent = Node()
        child_left = Node(args="left", function=self.helper_return)
        parent.add(child_left)
        self.assertIsNone(parent.right)
        self.assertIsNotNone(parent.left)
        self.assertEqual(parent.left, child_left)
        self.assertEqual("left", parent.left.function(parent.left.args))

    def helper_return(self, text):
        return text

    def test_add_node_if_exist_left(self):
        parent = Node()
        child_left = Node(args="left", function=self.helper_return)
        child_right = Node(args="right", function=self.helper_return)
        parent.add(child_left)
        parent.add(child_right)
        self.assertIsNotNone(parent.left)
        self.assertIsNotNone(parent.right)
        self.assertEqual(parent.right, child_right)
        self.assertEqual("right", parent.right.function(parent.right.args))
        self.assertEqual("left", parent.left.function(parent.left.args))

    def test_add_node_when_child_is_full(self):
        parent = Node()
        child_left = Node()
        child_right = Node()
        unexpected_child = Node()
        parent.add(child_left)
        parent.add(child_right)
        self.assertRaises(Exception, parent.add, unexpected_child)


if __name__ == '__main__':
    unittest.main()
