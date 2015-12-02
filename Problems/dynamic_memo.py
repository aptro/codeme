import random

def memorize(f):
    def memf(*X):
        if X not in memf.cache:
            memf.cache[X]=f(*X)
        return memf.cache[X]
    memf.cache={}
    return memf

#fibonacci memodynamic:

def recur_fib(n):
    if n==0 or n==1:
        return 1
    else:
        return recur_fib(n-1)+recur_fib(n-2)


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result

def recur_knapsack(items, maxWeight):
    if len(items)==0 or maxWeight<=0:
               return (0, ())
    start=items[0]
    w=start.getWeight()
    rest=items[1:]
    
    v1, t1= recur_knapsack(rest, maxWeight)
    v2, t2= recur_knapsack(rest, maxWeight-w)
    v2+=start.getValue()
    t2+=(start,)
    
    return (v2, t2) if w<=maxWeight and v2>=v1 else (v1, t1)

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items=()
    for i in range(len(vals)):
        Items+=(Item(names[i], vals[i], weights[i]),)
    return Items

def buildRandomItems(n):
    return tuple(Item(str(i), 10*random.randint(1, 10), random.randint(1,5)) for i in xrange(n))
    
test1=buildItems()    
test2=buildRandomItems(30)
    
def test_knapsack(items, maxWeight):
    mem_knapsack=memorize(recur_knapsack)
    (v, t)=mem_knapsack(items, maxWeight)
    print "total value", v
    for i in t:
        print i
                