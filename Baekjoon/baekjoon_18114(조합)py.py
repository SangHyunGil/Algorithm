import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    queue = deque([n])

    while queue:
        x = queue.popleft()

        for nx in graph[x]:
            if nx != -1:
                ans[nx] += ans[x]
                queue.append(nx)

N, M = map(int, input().split())
ans = [0] * N
employee = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for i in range(N):
    if employee[i] != -1:
        graph[employee[i]-1].append(i)

for _ in range(M):
    a, b = map(int, input().split())
    ans[a-1] += b

bfs(employee.index(-1))

print(*ans)