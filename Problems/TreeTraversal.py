from algorithms.BinaryTree import BinaryTree

#Building Binary Tree
tree= BinaryTree("1")
tree.insertLeft("4")
tree.insertRight("7")
tree.insertLeft("2")
tree.insertRight("3")
tree.getRightNode().insertLeft("6")
tree.getLeftNode().insertRight("5")


#preorder
def preorder(tree):
    if tree:
        print(tree.getRoot())
        preorder(tree.getLeftNode())
        preorder(tree.getRightNode())

#inorder
def inorder(tree):
    if tree:
        inorder(tree.getLeftNode())
        print (tree.getRoot())
        inorder(tree.getRightNode())

#postorder
def postorder(tree):
    if tree:
        postorder(tree.getLeftNode())
        postorder(tree.getRightNode())
        print (tree.getRoot())

#BSF(O(n))
def print_level(tree, level):
    if tree==0:
        return
    if level == 1:
        print tree.getRoot()
    elif (level>1):
        if tree.getLeftNode():
           print_level(tree.getLeftNode(), level-1)
        if tree.getRightNode():
           print_level(tree.getRightNode(), level-1)
        
    
    