from multiprocessing import Process

from Node import Node


class BinaryTree(object):
    def __init__(self, node=None):
        self.set_root(node)


    def get_root(self):
        return self.root

    def postfix(self, is_root=True, node=None, parallel=False):
        if is_root:
            node = self.get_root()
        if node is not None:
            if parallel:
                p_left = Process(target=self.postfix, args=(False, node.left))
                p_left.start()
                p_right = Process(target=self.postfix, args=(False, node.right))
                p_right.start()
                p_left.join()
                p_right.join()


            else:
                self.postfix(False, node.left, False)
                self.postfix(False, node.right, False)
            node.function(node.args)
            return 0

    def set_root(self, root):
        self.root = root



def function(number):
    print number


if __name__ == '__main__':
    root = Node(function, 1)
    node2 = Node(function, 2)
    node21 = Node(function, 21)
    node22 = Node(function, 22)

    node2.add(node21)
    node2.add(node22)

    node3 = Node(function, 3)
    node31 = Node(function, 31)
    node41 = Node(function, 41)

    node3.add(node31)
    node31.add(node41)

    root.add(node2)
    root.add(node3)

    tree = BinaryTree(root)
    tree.postfix(tree.get_root())
