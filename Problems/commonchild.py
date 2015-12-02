
from collections import defaultdict

def lcs(s1, s2):
    prev = defaultdict(int)
    
    for i in range(len(s1)):
        cur = defaultdict(int)
        for j in range(len(s2)):
            cur[j] = prev[j - 1] + 1 if s1[i] == s2[j] else max(cur[j - 1], prev[j])
            print cur
        prev = cur
        print prev
    return prev[len(s2)-1]
                
def main():
    s, t = "ASDFG", "DSFGH"
    print lcs(s, t)

main()