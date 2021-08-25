import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def findSwan():
    swans = deque([])
    water = deque([])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'L':
                graph[i][j] = '.'
                swans.append([i, j])

            if graph[i][j] == '.' or graph[i][j] == 'L':
                water_visited[i][j] = 1
                water.append([i, j])

    return water, swans[0], swans[1]

def isValid(i, j):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def check(swan):
    nswan = deque([])
    swan_visited[swan[0][0]][swan[0][1]] = 1

    while swan:
        x, y = swan.popleft()

        if x == another[0] and y == another[1]:
            return True

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if isValid(nx, ny) and not swan_visited[nx][ny]:
                swan_visited[nx][ny] = 1
                if graph[nx][ny] == '.':
                    swan.append([nx, ny])
                else:
                    nswan.append([nx, ny])
                    
    return nswan

def melt(water):
    nwater = deque([])
    
    while water:
        x, y = water.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if isValid(nx, ny) and not water_visited[nx][ny]:
                water_visited[nx][ny] = 1
                if graph[nx][ny] == '.':
                    water.append([nx, ny])
                else:
                    graph[nx][ny] = '.'
                    nwater.append([nx, ny])
                    
    return nwater


n, m = map(int, input().split())
water_visited = [[0] * m for _ in range(n)]
swan_visited = [[0] * m for _ in range(n)]
graph = [list(input().strip()) for _ in range(n)]
water, swan, another = findSwan()
swan = deque([swan])

cnt = 0
while True:
    swan = check(swan)
    if swan == True:
        print(cnt)
        break

    water = melt(water)
    cnt += 1