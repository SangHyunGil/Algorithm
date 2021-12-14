"""
이 문제는 DP로 풀 수 있는 문제이다.
M원을 만들 수 있는 동전의 최소 개수를 저장해가면서 구하면 
동전의 개수가 N이라고 했을때 O(NM)에 해결할 수 있다.
이에 따른 동전의 개수에 대한 점화식을 세우면 다음과 같다.
min(DP[M], DP[j-coin[i]]+1)
"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque([[0, 0]])
    visited = [0] * 10001

    while queue:
        x, cnt = queue.popleft()

        if x == M:
            return cnt

        for c in coin:
            nx = x+c

            if not visited[nx] and nx < 10001:
                visited[nx] = 1
                queue.append([nx, cnt+1])

    return -1

N, M = map(int, input().split())
coin = [int(input()) for _ in range(N)]

print(bfs())