inputfile = '/home/akp/pythonera/codjam/A-small-practice-1.in'
outputfile= open('/home/akp/pythonera/codjam/A-small-practice-1.out','w')
infile=open(inputfile, 'r')
testcase=infile.readline()
for i in range(int(testcase)):
    whorule =infile.readline()
    whoruled=whorule.strip()[-1]
    if whoruled == 'y':
            k = 'nobody'
    elif whoruled in 'aeiou':
            k = 'a queen'
    else:
        k= 'a king'    
    outputfile.write(" Case #%d: %s is ruled by %s." % (i + 1,whorule, k)+'\n')

    