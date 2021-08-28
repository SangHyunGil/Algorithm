import sys
from heapq import heappop, heappush
from collections import defaultdict, deque
answer = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
alpha = {}
for i in range(26):
    alpha[chr(ord('A')+i)] = i
    alpha[chr(ord('a')+i)] = i + 26

def isValid(i, j):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def climbing():
    heap = [[0, 0, 0]]
    up_time[0][0] = 0

    while heap:
        current_time, x, y = heappop(heap)
        if up_time[x][y] < current_time: continue

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if not isValid(nx, ny): continue
            current_height = alpha[graph[x][y]]
            next_height = alpha[graph[nx][ny]]
            if t < abs(current_height-next_height): continue

            # 원래보다 높이가 낮거나 같음
            if current_height >= next_height:
                if d >= current_time+1 and up_time[nx][ny] > current_time+1:
                    up_time[nx][ny] = current_time+1
                    heappush(heap, [up_time[nx][ny], nx, ny])
            else:
                cal_time = (current_height-next_height) ** 2
                if d >= current_time+cal_time and up_time[nx][ny] > current_time+cal_time:
                    up_time[nx][ny] = current_time+cal_time
                    heappush(heap, [up_time[nx][ny], nx, ny])

def returning():
    heap = [[0, 0, 0]]
    down_time[0][0] = 0

    while heap:
        current_time, x, y = heappop(heap)

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if not isValid(nx, ny): continue
            current_height = alpha[graph[x][y]]
            next_height = alpha[graph[nx][ny]]
            if t < abs(next_height-current_height): continue

            # 원래보다 높이가 낮거나 같음
            if next_height >= current_height:
                if d >= current_time+1 and down_time[nx][ny] > current_time+1:
                    down_time[nx][ny] = current_time+1
                    heappush(heap, [down_time[nx][ny], nx, ny])
            else:
                cal_time = (current_height-next_height) ** 2
                if d >= current_time+cal_time and down_time[nx][ny] > current_time+cal_time:
                    down_time[nx][ny] = current_time+cal_time
                    heappush(heap, [down_time[nx][ny], nx, ny])

n, m, t, d = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
up_time = [[sys.maxsize] * m for _ in range(n)]
down_time = [[sys.maxsize] * m for _ in range(n)]

climbing()
returning()

for i in range(n):
    for j in range(m):
        if up_time[i][j] + down_time[i][j] <= d:
            answer = max(answer, alpha[graph[i][j]])
    
print(answer)