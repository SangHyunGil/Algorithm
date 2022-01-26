"""
dfs를 통해 5개의 깊이가 존재하는지만 확인하면 된다.
시간초과가 날 수 있으니 visited를 매번 생성하여 접근하지말고
한번만 생성 후 이용해야하며 도중에 정답이라면 중단한다.
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, depth):
  global answer
  if depth >= 5:
    answer = 1
    return 

  for nx in graph[x]:
    if not visited[nx]:
      visited[nx] = 1
      dfs(nx, depth+1)
      visited[nx] = 0

answer = 0
n, m = map(int, input().split())

visited = [0] * n
graph = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n):
  visited[i] = 1
  dfs(i, 1)
  visited[i] = 0
  
  if answer:
    break

print(answer)