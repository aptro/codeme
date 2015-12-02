import string
inputfile = '/home/akp/pythonera/codjam/in1.in'
outputfile= open('/home/akp/pythonera/codjam/out1.in','w')
infile=open(inputfile, 'r')

testcase=infile.readline()
print testcase
for i in range(int(testcase)):
    input1= int(infile.readline())
    cardset1=[]
    for j in range(4):
        cardset1.append([int(x) for x in infile.readline().split()])
    input2=int(infile.readline())
    cardset2=[]
    for j in range(4):
        cardset2.append([int(x) for x in infile.readline().split()])
    guess1=cardset1[input1-1]
    guess2=cardset2[input2-1]
   
    m= list(set(guess1) & set(guess2))
    if m==[]:
        outputfile.write( str('Case #'+ str(i+1) +': '+'Volunteer cheated!'+'\n'))
    if len(m)==1:
        outputfile.write( str('Case #'+ str(i+1) +': '+str(m[0])+'\n'))
    if len(m)>1:
        outputfile.write(str('Case #'+ str(i+1) +': '+'Bad magician!'+'\n'))
                  
            
            
              