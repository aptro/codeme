""" There are N stations on route of a train. 
The train goes from station 0 to N-1.
The ticket cost for all pair of stations (i, j) is given where j is greater than i. 
Find the minimum cost to reach the destination.

Consider the following example:

Input: 
cost= [[0, 15, 80, 90],
              [float('inf'), 0, 40, 50],
              [float('inf'), float('inf'), 0, 70],
              [float('inf'), float('inf'), float('inf'), 0]];
             
There are 4 stations and cost[i][j] indicates cost to reach j 
from i. The entries where j < i are meaningless.

Output:
The minimum cost is 65
The minimum cost can be obtained by first going to station 1 
from 0. Then from station 1 to station 3. """
#dynamic programming

def mincost(cost):
    n= len(cost)
    dist=[float('inf')]*n
    dist[0] =0
    for i in range(n):
        for j in range(1,n):
            if dist[j] > dist[i]+cost[i][j]:
                dist[j] = dist[i]+cost[i][j]
    return dist[-1]
        