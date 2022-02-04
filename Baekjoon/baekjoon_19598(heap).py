"""
힙을 이용하여 푸는 문제이다.
최대한 많이 겹치는 부분의 최대값을 찾아 이를 출력하는 것이 답이 된다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
conference = [list(map(int, input().split())) for _ in range(n)]
conference = sorted(conference, key = lambda x : x[0])

ans = 0
heap = []
heappush(heap, conference[0][1])
for cf in conference[1:]:
  while heap and heap[0] <= cf[0]:
    heappop(heap)
  heappush(heap, cf[1])
  ans = max(ans, len(heap))

print(ans)