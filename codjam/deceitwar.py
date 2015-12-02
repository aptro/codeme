import string
inputfile = '/home/akp/pythonera/codjam/in3.in'
outputfile= open('/home/akp/pythonera/codjam/out3.out','w')
infile=open(inputfile, 'r')
testcase=infile.readline()
for j in range(int(testcase)):
    l=int(infile.readline())
    noamid=sorted([float(x) for x in infile.readline().split()])
    kend=sorted([float(x) for x in infile.readline().split()])
    deceitwar=0
    war=0
    noami=noamid[:]
    ken=kend[:]
    for i in range(l):
        if noami[0]< ken[0]:
            noami.remove(noami[0])
            ken.remove(ken[0])
        elif noami[0]>ken[0]:
           v=len(ken)
           for b in range(1,len(ken)):
                if ken[b]>noami[0]:
                   noami.remove(noami[0])
                   ken.remove(ken[b])
                   break
           if v==len(ken):
              noami.remove(noami[0])
              ken.remove(ken[0])
              war+=1   
        
           
            
    noamik=noamid[:]
    kenk=kend[:]
    for i in range(l):
        if noamik[0]< kenk[0]:
            noamik.remove(noamik[0])
            kenk.remove(kenk[-1])
        elif noamik[0]>kenk[0]:
            noamik.remove(noamik[0])
            kenk.remove(kenk[0])
            deceitwar+=1
             
    outputfile.write( str('Case #'+ str(j+1) +': '+str(deceitwar)+' '+str(war)+'\n'))        
    