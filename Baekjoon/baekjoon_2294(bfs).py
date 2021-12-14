"""
이 문제는 BFS로 풀어보았다.
DP로 동전의 최소 개수를 저장해가며 구할 수 있지만
너비 탐색을 진행하면서 해당 가치에 도달되는 순간 종료함으로써 최소 개수를 구할 수 있다.
만약 찾을 수 없는 경우 -1을 반환함으로써 처리해주면 된다.
"""
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def isValid(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else:
        return False

def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        
        if isValid(nx, ny) and graph[x][y] > graph[nx][ny]:
            visited[x][y] += dfs(nx, ny)

    print(x, y, visited[x][y])
    return visited[x][y]

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
dfs(0, 0)
for v in visited:
    print(v)