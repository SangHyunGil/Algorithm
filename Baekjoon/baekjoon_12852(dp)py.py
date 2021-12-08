import sys
from collections import deque
input = sys.stdin.readline

def bfs(N):
    queue = deque([[N]])
    visited = [0] * (N+1)
    visited[N] = 1

    while queue:
        x = queue.popleft()

        if x[-1] == 1:
            print(len(x)-1)
            print(*x)
            return

        if not visited[x[-1]-1]:
            queue.append(x+[x[-1]-1])

        if not x[-1] % 2 and not visited[x[-1]//2]:
            queue.append(x+[x[-1]//2])

        if not x[-1] % 3 and not visited[x[-1]//3]:
            queue.append(x+[x[-1]//3])

N = int(input())
bfs(N)