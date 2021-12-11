import sys
from collections import deque
input = sys.stdin.readline

def isValid(i, j):
    if 0 <= i < N and 0 <= j < M:
        return True
    else:
        return False

def bfs(i, j, k):
    queue = deque([[i, j]])
    visited[k][i][j] = graph[i][j]

    while queue:
        x, y = queue.popleft()

        for dx, dy in d[k]:
            nx, ny = x+dx, y+dy

            if isValid(nx, ny) and visited[k][nx][ny] < visited[k][x][y]+graph[nx][ny]:
                visited[k][nx][ny] = visited[k][x][y]+graph[nx][ny]
                queue.append([nx, ny])


d = {0 : [[0, 1], [-1, 0]], 1 : [[0, -1], [-1, 0]]}

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
visited = [[[-sys.maxsize] * M for _ in range(N)] for _ in range(2)]
bfs(N-1, 0, 0)
bfs(N-1, M-1, 1)

ans = -sys.maxsize
for i in range(N):
    for j in range(M):
        ans = max(ans, visited[0][i][j]+visited[1][i][j])

print(ans)