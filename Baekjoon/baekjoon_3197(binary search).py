import sys, time
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def init():
    n, m = map(int, input().split())
    graph = []; swan = []; water = set()
    parent = [0] * (n * m)
    rank = [0] * (n * m)
    for i in range(n):
        graph.append(list(input().strip()))
        for j in range(m):
            parent[m*i+j] = m*i+j
            if graph[i][j] == 'L':
                graph[i][j] = '.'
                swan.append([i, j])
            
            if graph[i][j] == '.':
                water.add((i, j))


    return n, m, graph, parent, rank, water, swan[0][0], swan[0][1], swan[1][0], swan[1][1]

def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u]) 
        return parent[u] 
    return parent[u]

def isValid(i, j):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def idx(i, j):
    return m*i+j

def union(water):
    ice = set()

    while water:
        x, y = water.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if isValid(nx, ny):
                if graph[nx][ny] == '.':
                    u = find(idx(x, y))
                    v = find(idx(nx, ny))

                    if u != v:
                        if u == v: continue

                        if rank[u] < rank[v]: parent[u] = v
                        else: parent[v] = u
                        if rank[u] == rank[v]: rank[u] += 1

                else:
                    ice.add((nx, ny))
                  
    return deque(ice)

def melt(ice):
    water = set()

    while ice:
        x, y = ice.popleft()
        graph[x][y] = '.'
        water.add((x, y))
    
    return deque(water)

n, m, graph, parent, rank, water, sx, sy, ex, ey = init()
water = deque(water)
cnt = 0
while True:
    ice = union(water)

    if find(idx(sx, sy)) == find(idx(ex, ey)):
        print(cnt)
        break
    
    water = melt(ice)
    cnt += 1