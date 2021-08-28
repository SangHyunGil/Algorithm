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

def dijkstra(sx, sy, ex, ey, limit_time):
    heap = [[0, alpha[graph[sx][sy]], sx, sy]]
    time = [[sys.maxsize] * m for _ in range(n)]
    time[sx][sy] = 0
    dist = -1
    while heap:
        current_time, height, x, y = heappop(heap)

        if x == ex and y == ey:
            dist = max(dist, height)

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if not isValid(nx, ny): continue
            current_height = alpha[graph[x][y]]
            next_height = alpha[graph[nx][ny]]
            if t < abs(current_height-next_height): continue

            # 원래보다 높이가 낮거나 같음
            if current_height >= next_height:
                if limit_time >= current_time+1 and time[nx][ny] > time[x][y]+1:
                    time[nx][ny] = time[x][y]+1
                    heappush(heap, [time[nx][ny], max(height, alpha[graph[nx][ny]]), nx, ny])
            else:
                cal_time = (current_height-next_height) ** 2
                if limit_time >= current_time + cal_time and time[nx][ny] > time[x][y]+cal_time:
                    time[nx][ny] = time[x][y]+cal_time
                    heappush(heap, [time[nx][ny], max(height, alpha[graph[nx][ny]]), nx, ny])

    return (-1, -1) if dist == -1 else (dist, time[ex][ey])

n, m, t, d = map(int, input().split())
visited = [[0] * m for _ in range(n)]; visited[0][0] = 1
graph = [list(input().strip()) for _ in range(n)]


for i in range(n):
    for j in range(m):
        
        d1, t1 = dijkstra(0, 0, i, j, d)
        if d1 != -1:
            d2, t2 = dijkstra(i, j, 0, 0, d-t1)
            if d2 != -1:
                answer = max(answer, d1, d2)

print(answer)

