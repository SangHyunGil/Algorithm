"""
bfs에 시뮬레이션이 첨가된 문제이다.
크게 보면 두 가지로 나뉜다.
1. 고객을 찾는다.
2. 고객의 집으로 간다.
이 두 가지를 따로 bfs로 나누어 풀었는데 주의할 점이 존재한다.
고객의 위치와 택시의 위치가 동일할 수 있어 처음에 이 부분을 고려하여 풀면 된다.
"""
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def isValid(i, j):
    if 0 <= i < N and 0 <= j < N:
        return True
    else:
        return False

def findCustomer(i, j, remain):
    queue = deque([[i, j]])
    visited = [[0] * N for _ in range(N)]

    for idx, c in enumerate(customer):
        if i == c[0] and j == c[1]:
            return idx, remain

    while queue:
        for i in range(len(queue)):
            x, y = queue.popleft()

            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]

                if isValid(nx, ny) and not visited[nx][ny] and not graph[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

        idx, minCost = -1, sys.maxsize
        for i, c in enumerate(customer):
            cost = visited[c[0]][c[1]]
            if cost and cost < minCost:
                idx, minCost = i, cost
        
        if idx != -1:
            return [idx, remain-minCost]
        
    return -1, -1

def findHome(idx, remain):
    sx, sy = customer[idx][0], customer[idx][1]
    ex, ey = customer[idx][2], customer[idx][3]
    queue = deque([[sx, sy]])
    visited = [[0] * N for _ in range(N)]

    while queue:
        x, y = queue.popleft()

        if x == ex and y == ey:
            if remain-visited[x][y] >= 0:
                return x, y, remain+visited[x][y]
            else:
                return -1, -1, -1

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if isValid(nx, ny) and not visited[nx][ny] and not graph[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

    return -1, -1, -1

def solve(M, hx, hy, remain):
    while len(customer):
        c, remain = findCustomer(hx, hy, remain)
        if remain < 0:
            return -1
        hx, hy, remain = findHome(c, remain)
        if remain < 0:
            return -1
        M -= 1
        del customer[c]

    return remain
        

N, M, P = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
customer = []
for _ in range(M):
    a, b, c, d = map(int, input().split())
    customer.append([a-1, b-1, c-1, d-1])
customer.sort()
print(solve(M, tx-1, ty-1, P))