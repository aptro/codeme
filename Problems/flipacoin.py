import random, pylab

def flipPlot(minexp, maxexp):
    ratio=[]
    diffs=[]
    xaxis=[]
    for i in range(minexp, maxexp+1):
        xaxis.append(2**i)
        numhead=0
        for k in range(2**i):
            if random.random()<0.5:
                numhead+=1
        numtail=2**i-numhead
        diffs.append(abs(numhead-numtail))
        ratio.append(numhead/float(numtail))
    pylab.title("diff in num head to tail")
    pylab.xlabel("num trials")
    pylab.ylabel("diff in num head to tail")
    pylab.plot(xaxis, diffs)
    pylab.plot(xaxis, diffs,'bo')
    pylab.figure()
    pylab.title("ratio")
    pylab.xlabel("num trials")
    pylab.ylabel("head to tail ratio")
    pylab.plot(xaxis, ratio)
    pylab.plot(xaxis, ratio, 'ro')
    pylab.figure()
    pylab.title("difference between heads and tails")
    pylab.xlabel("number of flips")
    pylab.ylabel("abs(#heads-#tails)")
    pylab.plot(xaxis, diffs,'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.title("head to tail ratio")
    pylab.xlabel("number of flip")
    pylab.ylabel("head/tail")
    pylab.plot(xaxis, ratio, 'bo')
    pylab.semilogx()

random.seed(0)
flipPlot(4,20)
pylab.show()
            
                
            