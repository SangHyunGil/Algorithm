import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def isValid(i, j):
    if 0 <= i < N and 0 <= j < M:
        return True
    else:
        return False

def bfs(i, j):
    global cnt 
    ans = 1
    cnt += 1
    visited[i][j] = cnt
    queue = deque([[i, j]])

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if isValid(nx, ny) and not visited[nx][ny] and graph[nx][ny]:
                ans += 1
                visited[nx][ny] = cnt
                queue.append([nx, ny])

    return ans

cnt = 0
answer = 0
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dic = dict()

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j]:
            dic[cnt] = bfs(i, j)

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            ans = 0
            temp = set()
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if isValid(nx, ny) and visited[nx][ny] and visited[nx][ny] not in temp:
                    ans += dic[visited[nx][ny]]
                    temp.add(visited[nx][ny])
            answer = max(answer, ans)

print(answer+1)
