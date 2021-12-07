import sys
from collections import deque
input = sys.stdin.readline

def isValid(i):
    if 0 <= i < n:
        return True
    else:
        return False

def bfs():
    queue = deque([[0, 0]])
    visited[0] = 1

    while queue:
        x, cnt = queue.popleft()

        if x == n-1:
            return cnt

        for k in range(1, graph[x]+1):
            nx = x+k

            if isValid(nx) and not visited[nx]:
                visited[nx] = 1
                queue.append([nx, cnt+1])
    return -1

n = int(input())
visited = [0] * n
graph = [*map(int, input().split())]
print(bfs())