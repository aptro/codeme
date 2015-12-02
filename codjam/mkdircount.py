import string
inputfile = '/home/akp/pythonera/codjam/mkdircount.in'
outputfile= open('/home/akp/pythonera/codjam/mkdircount.out','w')
infile=open(inputfile, 'r')
testcase=int(infile.readline())
for i in range(testcase):
    a,b=map(int, infile.readline().split())
    counter=0
    directorys=[]
    for j in range(1, a+b+1):
        if j<=a:
           temp=infile.readline().split('/')
           temp.pop(0)
           temp[-1]=temp[-1][:-1]
           onedir=''
           for m in range(len(temp)):
               onedir+='/'+temp[m]
               if not onedir in directorys:
                     directorys.append(onedir)
        else:       
           temp=infile.readline().split('/')
           temp.pop(0)
           temp[-1]=temp[-1][:-1]
           oonedir=''
           for k in range(len(temp)):
               oonedir+='/'+temp[k]
               if not oonedir in directorys:
                   directorys.append(oonedir)
                   counter+=1 
                            
    outputfile.write( str('Case #'+ str(i+1) +': '+str(counter)+'\n'))       
