import sys
from collections import deque
input = sys.stdin.readline

def isValid(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def bfs(i, j, graph, visited, n, m):
    queue = deque([[i, j, 1]])
    visited[i][j] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y, cnt = queue.popleft()

        if x == n-1 and y == m-1:
            return cnt

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if isValid(nx, ny, n, m) and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append([nx, ny, cnt+1])


def solve():
    n, m = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    print(bfs(0, 0, graph, visited, n, m))

solve()