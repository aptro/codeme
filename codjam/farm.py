import string
inputfile = '/home/akp/pythonera/codjam/in5.in'
outputfile= open('/home/akp/pythonera/codjam/out5.out','w')
infile=open(inputfile, 'r')

testcase=infile.readline()

def flipTheFlip(groups, l):
	if l == 0: return 0

	notFlip = True
	flip = True

	nfgr = []
	fgr = []

	for outs, targs in groups:
		targ1 = [x[1:] for x in targs if x[0] == '1']
		targ0 = [x[1:] for x in targs if x[0] == '0']
		outs0 = [x[1:] for x in outs if x[0] == '0']
		outs1 = [x[1:] for x in outs if x[0] == '1']

		if len(outs0) != len(targ0): notFlip = False
		else:
			nfgr.append((outs0, targ0))
			nfgr.append((outs1, targ1))

		if len(outs1) != len(targ0): flip = False
		else:
			fgr.append((outs1, targ0))
			fgr.append((outs0, targ1))

	resp = 1000000
	if notFlip:
		resp = min(resp, flipTheFlip(nfgr, l-1))

	if flip:
		resp = min(resp, 1 + flipTheFlip(fgr, l-1))
	
	return resp
for t in xrange(int(testcase)):
	print "Case #%d:" % (t+1),

	N, L = map(int, infile.readline().split())

	outlets = infile.readline().split()
	targets = infile.readline().split()

	flips = flipTheFlip( [(outlets, targets)], L)
	print flips if flips <= L else "NOT POSSIBLE"   