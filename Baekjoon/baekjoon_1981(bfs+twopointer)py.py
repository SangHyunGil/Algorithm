import sys, time
from collections import deque
input = sys.stdin.readline

def isValid(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    else:
        return False

def bfs(left, right):
    queue = deque([[0, 0]])
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == n-1:
            return True
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if isValid(nx, ny) and not visited[nx][ny] and left <= graph[nx][ny] <= right:
                visited[nx][ny] = 1
                queue.append([nx, ny])

    return False

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
mx = max(map(max, graph))

answer = sys.maxsize
left, right = 0, 0
while left <= right <= mx:
    if left <= graph[0][0] <= right and bfs(left, right):
        answer = min(answer, right-left)
        left += 1
    else:
        right +=1

print(answer)