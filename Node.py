class Node(object):
    def __init__(self, function=None, args=None):
        self.left = None
        self.right = None
        self.function = function
        self.args = args

    def add(self, new_node):
        if self.left is None:
            self.left = new_node
        elif self.right is None:
            self.right = new_node
        else:
            raise Exception("Only two child for each node")


    def postfix(self, node):
        if node is not None:
            self.postfix(node.left)
            self.postfix(node.right)
            node.function(node.args)