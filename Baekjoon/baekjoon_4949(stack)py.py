import sys
from collections import deque
input = sys.stdin.readline

def isValid(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def bfs(i, j, graph, visited, n, m):
    cnt = 1
    queue = deque([[i, j]])
    visited[i][j] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if isValid(nx, ny, n, m) and graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = 1
                queue.append([nx, ny])

    return cnt

def solve():
    answer = [0, 0]
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                answer[0] += 1
                answer[1] = max(answer[1], bfs(i, j, graph, visited, n, m))

    for a in answer:
        print(a)

solve()