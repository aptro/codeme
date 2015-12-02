import string
inputfile = '/home/akp/pythonera/codjam/in2.in'
outputfile= open('/home/akp/pythonera/codjam/out2.out','w')
infile=open(inputfile, 'r')

testcase=infile.readline()
for j in range(int(testcase)):
    (c,f,x)=(infile.readline().split())
    (c,f,x)=(round(float(c),7),round(float(f),7),round(float(x),7))
    
    
    i=1
    t1=x/2
    t2=c/2+x/(2+f*i)
    while t2<t1:
        i+=1
        t1=t2
        t2=t2+c/(2+f*(i-1))-x/(2+f*(i-1))+x/(2+f*i)  
    outputfile.write( str('Case #'+ str(j+1) +': '+str(round(t1,7))+'\n'))