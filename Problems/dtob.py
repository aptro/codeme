def dtob(n, numdigits):
    assert type(n)==int and type(numdigits)==int and n>=0 and 2**numdigits > n
    bstr=''
    while n>0:
        bstr=str(n%2)+bstr
        n=n//2
    while numdigits-len(bstr)>0:
        bstr='0'+bstr
    return bstr    
import random
        