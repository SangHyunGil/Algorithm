"""
단순히 다익스트라를 적용하는 것이나 조금 다른 점이 존재한다.
골목 비용의 최대값을 찾아야하기에 이러한 부분에 대한 추가 조건이 있다.
단순 브루트 포스로 찾을 수 있는 82번에 비해 83은 이분 탐색을 이용해 찾는다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start, end, k):
  heap = [[0, start-1]]
  dist = [sys.maxsize for _ in range(n)]

  while heap:
    cost, x = heappop(heap)
    if dist[x] < cost: continue
    if x == end-1 and dist[x] <= c:
      return 1

    for nc, nx in graph[x]:
      ncost = cost + nc

      if nc <= k and dist[nx] > ncost:
        dist[nx] = ncost
        heappush(heap, [ncost, nx])
  
  return dist[end-1] <= c


ans = sys.maxsize
n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n)]

left, right = 0, 0
for _ in range(m):
  x, y, k = map(int, input().split())
  graph[x-1].append([k, y-1])
  graph[y-1].append([k, x-1])
  right = max(right, k)

while left <= right:
  mid = (left + right) // 2
  if dijkstra(a, b, mid):
    ans = min(ans, mid)
    right = mid - 1
  else:
    left = mid + 1

print(ans if ans != sys.maxsize else -1)