import sys, heapq
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
jewel = []
for _ in range(n):
    heapq.heappush(jewel, list(map(int, input().split())))

bag = []
for _ in range(m):
    bag.append(int(input()))
bag.sort()

answer = 0
heap = []
for b in bag:
   
    while jewel and jewel[0][0] <= b: 
        w, cost = heapq.heappop(jewel)
        heapq.heappush(heap, [-cost, w])

    if heap:
        answer -= heapq.heappop(heap)[0]
    elif not jewel:
        break

print(answer)