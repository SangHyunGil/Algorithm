import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, graph, visited):
    queue = deque([[i, 1]])

    while queue:
        x, cnt = queue.popleft()

        for nx in graph[x]:
            if nx == i:
                return cnt

            if not visited[nx]:
                visited[nx] = 1
                queue.append([nx, cnt+1])

    return 0

def solve():
    for _ in range(int(input())):
        answer = 0     
        n = int(input())
        visited = [0] * n
        graph = [[] for _ in range(n)]
        for i, j in enumerate(list(map(int, input().split()))):
            graph[j-1].append(i)


        for i in range(n):
            if not visited[i]:
                answer += bfs(i, graph, visited)
        print(n-answer)
solve()