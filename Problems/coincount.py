import sys
sys.setrecursionlimit(10000)

#dynamic testing fibonnaci
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def coincount(l):
    if l[2] == 0:
        return 1
    if l[2] < 0:
        return 0
    if (l[1]<=0 and l[2]>=1):
        return 0
    return coincount([l[0], l[1]-1, l[2]]) + coincount([l[0], l[1], l[2]-l[0][l[1]-1]])
    
#dynamic programming
def memory(f):
    def memf(*x):
        i=0
        arglist ={}
        if x not in arglist.values():
           i+=1
           arglist[i] = x 
           cache[i] = f(*x)
           
        return cache[i]
    cache ={}
    return memf

def memoize(f):
    # define "wrapper" function that checks cache for
    # previously computed answer, only calling f if this
    # is a new problem.
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    # initialize wrapper function's cache.  store cache as
    # attribute of function so we can look at its value.
    memf.cache = {}
    return memf
        
coincountd = memory(coincount)
fibd = memoize(fib) 
fibm = memory(fib)               