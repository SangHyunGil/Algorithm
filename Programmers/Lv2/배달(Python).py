"""
이 문제는 그래프 탐색을 이용하여 풀 수 있는 문제이다.
문제를 푸는데 있어 다익스트라를 활용하였다.
입력받은 도로에 대해 그래프를 구성하고 해당 그래프에 대해 전체적으로 다익스트라를 돌렸다.
그리고 K 시간 이하로 들어올 수 있는 도시의 개수를 카운트했다.
"""

import sys
from heapq import heappush, heappop

def dijkstra(N, graph, K):
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

    return sum([1 if d <= K else 0 for d in dist[1:]])

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for a, b, cost in road:
        graph[a].append([cost, b])
        graph[b].append([cost, a])

    return dijkstra(N, graph, K)