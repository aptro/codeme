def segments(phrase):
    p=list(phrase)
    k=[]
    for i in range(len(p)):
        m=[p[i]]
        for j in range(i+1, len(p)):
            k.append(m)
            m=m+[p[j]]
    return k
      
    