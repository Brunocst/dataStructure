class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:

    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node = None):

        if node is None:
            node = self.root
        
        if node.left:
            print("(", end="")
            self.simetric_traversal(node.left)
        print(node, end = " ")
        if node.right:
            self.simetric_traversal(node.right)
            print(")", end="")

    def postorder_traversal(self, node=None):

        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        if node.right:
            self.inorder_traversal(node.right)
        print(node)

    def height(self, node = None):

        if node is None:
            node = self.root
        
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        
        if hright > hleft:
            return hright+1
        
        return hleft+1
            
class BinarySearchTree(BinaryTree):

    def insert(self, data):
        parent = None
        pass

    def search():
        pass



if __name__ == "__main__":

    tree = BinaryTree(7)
    tree.root.left = 18
    tree.root.right = 14

    print(tree.root)