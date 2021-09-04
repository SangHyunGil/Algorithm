import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def init():
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    return n, sorted(arr)

def solve():
    n, arr = init()
    answer = 0; cnt = 0; heap = []

    for dead, cup in arr:
        if cnt < dead:
            cnt += 1
            answer += cup
            heappush(heap, [cup, dead])
        else:
            if cnt-1 < dead and heap[0][0] < cup:
                answer -= heap[0][0]
                heappop(heap)
                answer += cup
                heappush(heap, [cup, dead])

    print(answer)

solve()