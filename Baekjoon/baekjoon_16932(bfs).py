"""
이 문제는 bfs를 통해 영역의 넓이를 찾는 문제 중 하나이다.
하지만 조금 다른 점이 접근이 불가능한 한 부분에 대해 접근을 가능하게 하여 최대 넓이를 찾는 문제이다.
이러한 부분에 있어 처음에는 접근이 불가능한 점에 대해 모두 bfs를 진행했는데
이렇게 진행한다면 visited를 처리하지 못해 단순 간선의 개수만큼의 복잡도를 가져야하지만
간선의 개수의 제곱만큼의 복잡도를 가져 O((NM)^2)의 복잡도를 가져 실패한다.
그래서 다른 방법으로 모든 영역의 넓이를 찾고 각 넓이를 차지하는 영역들에 번호를 매겨
불가능한 점을 기준으로 4방향을 겹치지 않게 넓이를 더해 처리하는 방식을 생각했다.
"""
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