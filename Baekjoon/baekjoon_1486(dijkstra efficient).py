import sys
from heapq import heappop, heappush
from collections import defaultdict, deque
answer = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
alpha = {}
for i in range(26):
    alpha[chr(ord('A')+i)] = i
    alpha[chr(ord('a')+i)] = i + 26

def isValid(i, j):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def setAdj(adj):
    for i in range(n):
        for j in range(m):
            for k in range(4):
                ni, nj = i+dx[k], j+dy[k]
                if not isValid(ni, nj): continue
                current_height = alpha[graph[i][j]]
                next_height = alpha[graph[ni][nj]]

                if t < abs(current_height-next_height): continue
                
                if current_height >= next_height:
                    adj[i*m+j][ni*m+nj]=1
                else:
                    time = (current_height-next_height)**2
                    adj[i*m+j][ni*m+nj]=time

def floyd(adj):
    for k in range(n*m):
        for i in range(n*m):
            for j in range(n*m):
                if adj[i][j] > adj[i][k] + adj[k][j]:
                    adj[i][j] = adj[i][k] + adj[k][j]
def find(adj):
    answer = 0
    for i in range(n*m):
        if adj[0][i] + adj[i][0] <= d:
            answer = max(answer, alpha[graph[i//m][i%m]])

    print(answer)

n, m, t, d = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
adj = [[0] * (n*m) for _ in range(n*m)]
setAdj(adj)
floyd(adj)
find(adj)