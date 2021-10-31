"""
목적지까지 최단거리로 가는 경로를 묻는 문제로 전형적인 bfs 문제이다.
bfs로 경로를 탐색하고 최단 거리를 반환, 혹은 -1을 반환한다.
"""

from collections import deque

def isValid(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def bfs(i, j, maps):
    queue = deque([[i, j]])
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited[i][j] = 1
    dx = [1, 0, -1, 0]
    dy = [0 ,1 ,0 ,-1]

    while queue:
        x, y = queue.popleft()

        if x == len(maps)-1 and y == len(maps[0])-1:
            return visited[x][y]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if isValid(nx, ny, len(maps), len(maps[0])) and maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

    return -1

def solution(maps):
    answer = bfs(0, 0, maps)

    return answer