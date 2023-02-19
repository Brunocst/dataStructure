class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def invert(node):

    if (node == None):
        return
    else:

        temp = node

        invert(node.left)
        invert(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp

def print_tree(node):

    if node == None :
        return
    
    print_tree(node.left)  
    print (node.data)
    print_tree(node.right)  

root = newNode(2)  
root.left = newNode(1)  
root.right = newNode(4)  
root.right.left = newNode(3)  
root.right.right = newNode(5)  
  
# Print inorder traversal of the input tree
print("Inorder traversal of the constructed tree is")  
print_tree(root)  
      
# Convert tree to its mirror
invert(root)  
  
# Print inorder traversal of the mirror tree
print("\nInorder traversal of the mirror treeis ")  
print_tree(root)  
    

        
