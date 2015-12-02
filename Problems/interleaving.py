#dynamic programming
def isInterleaved(A, B, C):
    a= len(A)
    b =len(B)
    memo = [[False] * b ] * a
    if ((a+b) != len(C)):
        return False
    for i in range(a):
        for j in range(b):
            if( i == 0 and j == 0):
                memo[i][j] = True
            elif(i == 0 and B[j] == C[i+j-1]):
                memo[i][j] = memo[i][j-1]
            elif (j==0 and A[i-1]==C[i-1]):
                memo[i][j] = memo[i-1][j]
            elif(A[i-1]==C[i+j-1] and B[j-1]!=C[i+j-1]):
                memo[i][j] = memo[i-1][j]
            elif (A[i-1]!=C[i+j-1] and B[j-1]==C[i+j-1]):
                memo[i][j] = memo[i][j-1]
            elif (A[i-1]==C[i+j-1] and B[j-1]==C[i+j-1]):
                memo[i][j]=(memo[i-1][j] or memo[i][j-1]) 
    return memo[a-1][b-1]
            