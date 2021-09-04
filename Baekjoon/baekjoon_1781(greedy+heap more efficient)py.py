import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def init():
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    return n, sorted(arr)

def solve():
    n, arr = init()
    heap = []

    for dead, cup in arr:
        heappush(heap, cup)

        if len(heap) > dead:
            heappop(heap)

    print(sum(heap))

solve()