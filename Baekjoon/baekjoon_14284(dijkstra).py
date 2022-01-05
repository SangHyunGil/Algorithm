import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(S, T):
    heap = [[0, S]]
    dist = [sys.maxsize] * N

    while heap:
        cost, x = heappop(heap)

        if dist[x] < cost: continue

        for ncost, nx in graph[x]:
            if dist[nx] > ncost + cost:
                dist[nx] = ncost + cost
                heappush(heap, [ncost + cost, nx])

    return dist[T]

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append([c, b-1])
    graph[b-1].append([c, a-1])
S, T = map(int, input().split())

print(dijkstra(S-1, T-1))