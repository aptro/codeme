def isCyclic(s1, s2):
    ls1= len(s1)
    ls2= len(s2)
    if (ls1 != ls2):
        return False
    s3 = s1 + s1
    if (s2 in s3):
        return True
        