import sys
from heapq import heappush, heappop

def dijkstra(N, graph):
    heap = [[0, 1]]
    dist = [0] + [sys.maxsize] * N
    dist[1] = 0

    while heap:
        cost, x = heappop(heap)
        if dist[x] < cost:
            continue

        for ncost, nx in graph[x]:
            if dist[nx] > ncost+cost:
                dist[nx] = ncost+cost
                heappush(heap, [ncost+cost, nx])

    print(dist)

def solution(N, road, K):
    answer = 0

    graph = [[] for _ in range((len(road)+1))]
    for a, b, cost in road:
        graph[a].append([cost, b])
        graph[b].append([cost, a])

    dijkstra(N, graph)
    return answer

solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)