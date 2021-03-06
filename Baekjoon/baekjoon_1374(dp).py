import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

answer = 0
N, M, G, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
seed = [[i, j] for i in range(N) for j in range(M) if graph[i][j] == 2]


def isValid(i, j):
    if 0 <= i < N and 0 <= j < M:
        return True
    else:
        return False

def bfs(ngraph, red, green):
    ans = 0
    queue = deque()
    visited = [[0] * M for _ in range(N)]
    for i, j in red:
        queue.append([i, j])
        ngraph[i][j] = 3
        visited[i][j] = 1

    for i, j in green:
        queue.append([i, j])
        ngraph[i][j] = 4
        visited[i][j] = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:


        for i in range(len(queue)):
            x, y = queue.popleft()
            if ngraph[x][y] == 5: continue
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if isValid(nx, ny) and not visited[nx][ny] and ngraph[nx][ny] >= 1:
                    if ngraph[nx][ny] == 1 or ngraph[nx][ny] == 2:
                        ngraph[nx][ny] = ngraph[x][y]
                        queue.append([nx, ny])

                    else:
                        if ngraph[nx][ny] != ngraph[x][y] and ngraph[nx][ny] != 5:
                            ngraph[nx][ny] = 5
                            ans += 1

        for i in range(len(queue)):
            x, y = queue[i]
            visited[x][y] = 1

    return ans

z = 0
for p1 in combinations(seed, G+R):
    for p2 in combinations(range(G+R), G):
        red = []
        green = []
        ngraph = deepcopy(graph)
        for i in range(G+R):
            if i in p2:
                red.append(p1[i])
            else:
                green.append(p1[i])
        z += 1
        answer = max(answer, bfs(ngraph, red, green))

print(z)
print(answer)