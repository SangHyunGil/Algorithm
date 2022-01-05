"""
다익스트라를 활용하여 푸는 문제 중 하나이다.
단지 문제에서 "집의 후보를 출력하라"라고 했으므로 집의 후보로부터 출발하는 것이 아니라
편의점으로부터 출발하여 집까지의 거리를 출력해야 더 쉽게 풀 수 있다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra():
    heap = [[0, s-1] for s in store]

    while heap:
        cost, x = heappop(heap)
        
        if dist[x] < cost: continue

        for ncost, nx in graph[x]:
            if dist[nx] > ncost + cost:
                dist[nx] = ncost + cost
                heappush(heap, [ncost + cost, nx])

    temp = [[dist[h-1], h-1] for h in home]
    temp.sort(key = lambda x : [x[0], x[1]])
    return temp[0][1]

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append([c, b-1])
    graph[b-1].append([c, a-1])

dist = [sys.maxsize] * N
P, Q = map(int, input().split())
home = list(map(int, input().split()))
store = list(map(int, input().split()))
print(dijkstra()+1)