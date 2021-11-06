import sys
from collections import deque

def isValid(i):
    if 0 < i <= 1000000000:
        return True
    else:
        return False

def bfs(i, n):
    queue = deque([i])
    visited = [sys.maxsize] * 1000000001
    visited[0] = 0

    while queue:
        x = queue.popleft()
        print(x, visited[:10])
        if x == n:
            return visited[n]

        nx = x+1
        if isValid(nx) and visited[nx] >= visited[x]+1:
            visited[nx] = visited[x]+1
            queue.append(nx)

        nx = 2*x
        if isValid(nx) and visited[nx] >= visited[x]:
            visited[nx] = visited[x]
            queue.append(nx)

def solution(n):
    ans = bfs(0, n)
    return ans

solution(5)