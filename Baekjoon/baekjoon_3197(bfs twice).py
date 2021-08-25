import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def isValid(i, j):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def findSwan(graph, visited):
    swans = []
    edge_ice = set()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'L':
                graph[i][j] = '.'
                swans.append((i, j))

            if graph[i][j] == '.':
                for k in range(4):
                    ni, nj = i+dx[k], j+dy[k]
                    if isValid(ni, nj) and graph[ni][nj] == 'X':
                        visited[ni][nj] = 1
                        edge_ice.add((ni, nj))

    return swans[0], swans[1], list(edge_ice)

def checkMeltingTime(edge_ice):
    queue = deque(edge_ice)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if isValid(nx, ny) and not time[nx][ny] and graph[nx][ny] == 'X':
                time[nx][ny] = time[x][y] + 1
                queue.append([nx, ny])

def check(mid):
    queue = deque([swan1])
    visited = [[0] * m for _ in range(n)]
    visited[swan1[0]][swan1[1]] = 1

    while queue:
        x, y = queue.popleft()

        if x == swan2[0] and y == swan2[1]:
            return True

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if isValid(nx, ny) and not visited[nx][ny] and time[nx][ny] <= mid:
                visited[nx][ny] = 1
                queue.append([nx, ny])

    return False


n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
time = [[0] * m for _ in range(n)]
swan1, swan2, edge_ice = findSwan(graph, time)

checkMeltingTime(edge_ice)


left, right = 0, 15
answer = sys.maxsize
while left <= right:
    mid = (left+right)//2
    if check(mid):
        answer = min(mid, answer)
        right = mid-1
    else:
        left = mid+1

print(answer)