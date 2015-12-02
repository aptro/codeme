class puzzle(object):
    def __init__(self, order):
        self.label=order
        for i in range(9):
            if self.label[i]=='0': 
                   self.spot=i
                   
    def transition(self, to):
        label=self.label
        blanklocation=self.spot
        newblanklabel=str(label[to])
        newlabel=''
        for j in range(9):
            if j==to:
                newlabel+='0'
            elif j==blanklocation:
                newlabel+=newblanklabel
            else:
                newlabel+=str(label[j])
        return puzzle(newlabel)
    def __str__(self):
            return self.label
            
                 
def BFSgenerator(start, end, q=[]):
     inpath=[start]
     q.append(inpath)
     while len(q)!=0:
         path1=q.pop(0)
         lastnode=path1[-1]
         if lastnode.label==end.label:
             return path1
         for shift in shiftpos[lastnode.spot]:
             new=lastnode.transition(shift)
             if checkin(new, path1):
                 newpath=path1+[new]
                 q.append(newpath)
     return None  
def checkin(new, path):
    for i in path:
        if i==new:
            return False
    return True  
shiftpos={}
shiftpos[0]=[1, 3]
shiftpos[1]=[0, 2, 4]
shiftpos[2]=[1, 5]
shiftpos[3]=[0, 4, 6]
shiftpos[4]=[1, 3, 5, 7]
shiftpos[5]=[2, 4, 8]
shiftpos[6]=[3, 7]
shiftpos[7]=[4, 6, 8]
shiftpos[8]=[5, 7]

goal=puzzle('012345678')
test1=puzzle('123456780')

def printgrid(pzl):
    data=pzl.label
    print data[0], data[1], data[2]
    print data[3], data[4], data[5]
    print data[6], data[7], data[8]
    print ""
def printsol(path):
    for i in path:
        printgrid(i)
path=BFSgenerator(test1, goal)
printsol(path)   


                 
                                                   
                 
                 
             
             
          