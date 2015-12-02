# A complete binary tree is a tree in which each level has all of its nodes. 
#The exception to this is the bottom level of the tree, which we fill in from left to right. 
#The method that we will use to store items in a heap relies on maintaining the heap order property. 
#The heap order property is as follows: 
#In a heap, for every node x with parent p, the key in p is smaller than or equal to the key in x. 


class BinaryHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i//2 > 0 :
            if self.heapList[i] > self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i //= 2

    def insert(self, j):
        self.heapList.append(j)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval