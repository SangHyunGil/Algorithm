import sys, time
from collections import deque
input = sys.stdin.readline

def findMinMax(arr, left, right):
    temp = sorted(arr)
    return min(left, temp[0]), max(right, temp[-1])

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

def go(left, mid, right):
    for i in range(left, right):
        print(i, i+mid, mid)
        if i <= graph[0][0] <= i+mid and bfs(i, i+mid):
            return True
    return False


n = int(input())
graph = []
mn, mx = sys.maxsize, -sys.maxsize
for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    mn, mx = findMinMax(arr, mn, mx)


answer = 0
left, right = 0, 200
while left <= right:
    print(left, right)
    mid = (left+right)//2
    if go(mn, mid, mx):
        answer = mid
        right = mid-1

    else:
        left = mid+1

print(answer)