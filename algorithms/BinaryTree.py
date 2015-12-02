class BinaryTree:
    def __init__(self,key):
        self.root =key
        self.leftNode = None
        self.rightNode = None
    def insertLeft(self, leftnode):
        if (self.leftNode == None):
            self.leftNode = BinaryTree(leftnode)
        else:
            t = BinaryTree(leftnode)
            t.leftNode = self.leftNode
            self.leftNode = t
    def insertRight(self, rightnode):
        if (self.rightNode == None):
            self.rightNode = BinaryTree(rightnode)
        else:
            t = BinaryTree(rightnode)
            t.rightNode =self.rightNode
            self.rightNode = t
    def getRoot(self):
        return self.root
    def setroot(self, newroot):
        self.root = newroot
    def getLeftNode(self):
        return self.leftNode
    def getRightNode(self):
        return self.rightNode
             