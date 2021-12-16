"""
전형적인 DP이다.
여기서 많이 간과한 부분이 존재했는데, 단순 위에서 올 수 있는 것이 아니라 왼쪽에서도 올 수 있다.
올수 있는 방향은 왼쪽, 왼쪽 상단, 상단, 오른쪽 상단이다.
하지만, 범위가 맞는지 확인해줘야 하기에 이 부분에 대한 메소드를 하나 구성하였다.
"""

import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

dx = [1, 0 ,-1, 0]
dy = [0, 1, 0, -1]

def isValid(x, y):
    if 0 <= x < N+2 and 0 <= y < M+2:
        return True
    else:
        return False

def melt(x, y):
    cnt = 0
    for i in range (4):
        nx, ny = x+dx[i], y+dy[i]
        if isValid(nx, ny) and graph[nx][ny] == '.':
            cnt += 1

    return '.' if cnt >= 3 else 'X'

N, M = map(int, input().split())
graph = [['.']*(M+2)]
graph += [['.']+list(input().rstrip())+['.'] for _ in range(N)]
graph += [['.']*(M+2)]
ngraph = deepcopy(graph)

minmax_x = [sys.maxsize, -sys.maxsize]
minmax_y = [sys.maxsize, -sys.maxsize]
for i in range(N+2):
    for j in range(M+2):
        if graph[i][j] == 'X':
            ngraph[i][j] = melt(i, j)
            if ngraph[i][j] == 'X':
                minmax_x[0] = min(minmax_x[0], i); minmax_x[1] = max(minmax_x[1], i)
                minmax_y[0] = min(minmax_y[0], j); minmax_y[1] = max(minmax_y[1], j)

for i in range(minmax_x[0], minmax_x[1]+1):
    for j in range(minmax_y[0], minmax_y[1]+1):
        print(ngraph[i][j], end="")
    print()