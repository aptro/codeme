"""def countCC(M):
    row= len(M)
    col= len(M[0])
    visited = [[False]*col]*row
    count = 0
    for i in range(0,row):
        for j in range(0,col):
            if (M[i][j]==1 and  visited[i][j]==False):
                dfs(M, i, j ,visited)
                print (i,j)
                count =count+1           
    return count

def isSafe(M, row, col, visited):
    Row= len(M)
    Col= len(M[0])  
    return (row < Row) and (row >= 0) and (col <Col) and (col >= 0) and (M[row][col] == 1) and (visited[row][col] == False) 

def dfs(M, row, col, visited):
    rowNbr =[-1, -1, -1,  0, 0,  1, 1, 1]   
    colNbr=  [-1,  0,  1, -1, 1, -1, 0, 1]
    visited[row][col] = True
    
    for i in range(4):
        if(isSafe(M, row + rowNbr[i], col + colNbr[i], visited)):
                        dfs(M, row + rowNbr[i], col + colNbr[i],visited)     
             
    
a=[  [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
"""    
def recursion(a,i,j):
    if i>=0 and i<len(a) and j>=0 and j<len(a[i]):
        if a[i][j] ==1:
            a[i][j] =2
            recursion(a,i,j+1)
            recursion(a,i,j-1)
            recursion(a,i+1,j)
            recursion(a,i-1,j)
            recursion(a,i-1,j-1)
            recursion(a,i-1,j+1)
            recursion(a,i+1,j-1)
            recursion(a,i+1,j+1)
        
            
def findingIslands(a):
    count =0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] ==1:
                count = count+1
                recursion(a,i,j)
    print "Number of Islands:" +str(count)
def main():
    array =[[1,0,1],
            [1,1,1],
            [0,0,1]]
    findingIslands(array)
if __name__ == '__main__':
    main()