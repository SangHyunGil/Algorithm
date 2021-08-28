import sys
input = sys.stdin.readline

answer = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
alpha = {}
for i in range(26):
    alpha[chr(ord('A')+i)] = i
    alpha[chr(ord('a')+i)] = i + 26

n, m, t, d = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
adj = [[sys.maxsize] * (n*m) for _ in range(n*m)]

# Edge 세팅
for i in range(n):
    for j in range(m):
        for k in range(4):
            ni, nj = i+dx[k], j+dy[k]
            if not (0 <= ni < n and 0 <= nj < m): continue
            current_height = alpha[graph[i][j]]
            next_height = alpha[graph[ni][nj]]
            if t < abs(current_height-next_height): continue
            
            if current_height >= next_height:
                adj[i*m+j][ni*m+nj]=1
            else:
                time = (current_height-next_height)**2
                adj[i*m+j][ni*m+nj]=time

# Floyd
for k in range(n*m):
    for i in range(n*m):
        for j in range(n*m):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

# 정답 도출
answer = 0
for i in range(n*m):
    if adj[0][i] + adj[i][0] <= d:
        answer = max(answer, alpha[graph[i//m][i%m]])

print(answer)