"""
단순 최소값 2개씩을 뽑아 더해 2개씩 추가하면 되는 간단한 문제이다.
"""
import sys
from heapq import heappush, heappop, heapify
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapify(arr)

for _ in range(m):
  sumItem = 0
  for _ in range(2):
    sumItem += heappop(arr)

  for i in range(2):
    heappush(arr, sumItem)

print(sum(arr))