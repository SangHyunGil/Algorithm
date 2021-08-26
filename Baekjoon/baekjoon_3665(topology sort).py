import sys, heapq
from collections import deque
input = sys.stdin.readline

def dijkstra(graph, s): # find shortest path
    dist = [sys.maxsize] * len(graph)
    heap = [[0, s]]
    dist[s] = 0

    while heap:
        cost, x = heapq.heappop(heap)

        if dist[x] < cost: continue

        for nx in graph[x]:
            if dist[nx] > graph[x][nx] + cost:
                dist[nx] = graph[x][nx] + cost
                heapq.heappush(heap, [graph[x][nx]+cost, nx])

    return dist
    
def bfs(e): # remove shortest path
    queue = deque([e])
    route = []
    while queue:
        x = queue.popleft()
        if x == s: continue

        for _, nx in reverse[x]:
            if dist[nx] + graph[nx][x] == dist[x] and [nx, x] not in route:
                route.append([nx, x])
                queue.append(nx)

    for i, j in route:
        del graph[i][j]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    s, e = map(int, input().split())
    
    graph = [dict() for _ in range(n)]
    reverse = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        reverse[b].append([c, a])

    
    dist = dijkstra(graph, s)
    bfs(e)

    dist = dijkstra(graph, s)
    print(dist[e] if dist[e] != sys.maxsize else -1)