class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        
root=Node(4)
root.left=Node(8)
root.left.left=Node(5)
root.left.left.left=Node(6)
root.left.right=Node(11)
root.left.right.right=Node(25)
root.right=Node(12)
root.right.left=Node(39)
root.right.right=Node(2)


#Preoder Traversal Node Left Right

def Preorder_traversal(root):
    print(root.value)
    if root.left!=None:
        Preorder_traversal(root.left)
    if root.right!=None:
        Preorder_traversal(root.right)

#Left Right Node

def Postorder_traversal(root):
    if root.left!=None:
        Postorder_traversal(root.left)
    if root.right!=None:
        Postorder_traversal(root.right)
    print(root.value)

#Inorder Left Node Right

def Inorder_traversal(root):
    if root.left!=None:
        Inorder_traversal(root.left)
    print(root.value)
    if root.right!=None:
        Inorder_traversal(root.right)

#Preorder_traversal(root)
#Postorder_traversal(root)
Inorder_traversal(root)