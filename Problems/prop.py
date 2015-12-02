#Python snippet
#!/usr/bin/py
# Head ends here
# Tail starts here


def relength(s):
    k = {}
    l = 0
    s=s+"1"
    m =""
    q=[]
    for i in range(len(s)-1):
        if (s[i] == s[i+1]):
            l+=1
        else:
            k[s[i]] = l+1
            l = 0
            q.append(s[i])
    for z in q:        
         if (k[z] == 1):
              m=m+str(z) 
         else:
              m=m+str(z)+str(k[z])
        
    return m        
if __name__ == '__main__':
    relength("wwweeedff")    