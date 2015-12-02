def mean(L):
    return sum(L)/float(len(L))
    
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5
    
def variance(L):
    mu = mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)
a=[[0,1,2,3,4,5,6,7,8]

 ,[5,10,10,10,15]

 ,[0,1,2,4,6,8]

,[6,7,11,12,13,15]

,[9,0,0,3,3,3,6,6]]


for i in a:
    print mean(i)
print '........'    
for i in a:    
    print variance(i)