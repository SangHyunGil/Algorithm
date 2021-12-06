import sys, copy
from collections import deque
input = sys.stdin.readline

def isValid(i, j):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def bfs(i, j):
    queue = deque([[i, j]])
    visited[i][j] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if isValid(nx, ny) and not visited[nx][ny] and graph[nx][ny] >= k:
                visited[nx][ny] = 1
                queue.append([nx, ny])

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append([])
    temp = [*map(int, input().split())]
    for j in range(0, m*3, 3):
        graph[i].append(sum(temp[j:j+3])//3)

k = int(input())

cnt = 0
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] >= k:
            bfs(i, j)
            cnt += 1

print(cnt)
