import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    p, d = map(int, input().split())
    arr.append([d, p])
arr.sort()

answer = 0
heap = [] 
for d, p in arr:
    if heap:
        if len(heap) < d:
            answer += p
            heappush(heap, [p, d])

        elif len(heap) == d and heap[0][0] < p:
            prev_p, _ = heappop(heap)
            answer -= prev_p

            heappush(heap, [p, d])
            answer += p

    else:
        answer += p
        heappush(heap, [p, d])
    
print(answer)