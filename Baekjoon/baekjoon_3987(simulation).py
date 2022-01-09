"""
구현 문제이다.
bfs를 이용해서 푸는 구현 문제인데
/ 나 \를 만나면 방향이 꺾여 이 부분에 대한 부분을 고려해야하기에
단순 방문 배열을 N*M이 아니라 4방향을 포함시켜 4*N*M으로 진행해야한다.
이러한 부분에 대한 처리를 진행하면서 최대 시간이 되는 부분을 출력하면 된다.
"""
import sys
from collections import deque
input = sys.stdin.readline

dic = {0 : "U", 1 : "R", 2 : "D", 3 : "L"}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def isValid(i, j):
    if 0 <= i < N and 0 <= j < M:
        return True
    else:
        return False

def bfs(sx, sy, k):
    queue = deque([[sx, sy, k]])
    visited = [[[0] * M for _ in range(N)] for _ in range(4)]
    visited[k][sx][sy] = 1

    while queue:
        x, y, d = queue.popleft()

        nx, ny = x+dx[d], y+dy[d]
        if not isValid(nx, ny) or graph[nx][ny] == 'C':
            return visited[d][x][y]

        nd = d
        if graph[nx][ny] == '/':
            if nd == 1 or nd == 3:
                nd = (nd-1)%4
            else:
                nd = (nd+1)%4

        elif graph[nx][ny] == '\\':
            if nd == 1 or nd == 3:
                nd = (nd+1)%4
            else:
                nd = (nd-1)%4

        if visited[nd][nx][ny]:
            return "Voyager"

        visited[nd][nx][ny] = visited[d][x][y]+1
        queue.append([nx, ny, nd])

answer = []
N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
sx, sy = map(int, input().split())

for i in range(4):
    answer.append(bfs(sx-1, sy-1, i))

d, v = -1, -1

for idx, ans in enumerate(answer):
    if ans == 'Voyager':
        d, v = dic[idx], ans
        break
    else:
        if v < ans:
            d, v = dic[idx], ans

print(d)
print(v)