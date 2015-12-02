from algorithms.BinaryTree import BinaryTree
from Problems.TreeTraversal import postorder
import operator


def buildParseTree(exp):
    listExp = exp.split()
    bTree = BinaryTree('')
    stack = []
    stack.append(bTree)
    cTree = bTree

    for i in listExp:
        if i == '(':
            cTree.insertLeft('')
            stack.append(cTree)
            cTree = cTree.getLeftNode()

        elif i in "0123456789":
            cTree.setroot(int(i))
            cTree= stack.pop()

        elif i in ["+", "-", "*", "/"]:
            cTree.setroot(i)
            cTree.insertRight('')
            stack.append(cTree)
            cTree =cTree.getRightNode()

        elif i == ")":
            cTree = stack.pop()
        else:
            raise ValueError("Error")

    return bTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftNode()
    rightC = parseTree.getRightNode()

    if leftC and rightC:
        fn = opers[parseTree.getRoot()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRoot()

if __name__ == "__main__":
    pt =buildParseTree("( ( 4 + 5 ) * 6 )")
    print evaluate(pt)
    postorder(pt)







