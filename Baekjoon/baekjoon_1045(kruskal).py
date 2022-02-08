"""
문제의 이해가 잘 되지 않아 고생했던 문제이다.
우선순위가 높은 MST를 찾는 문제인데 우선순위의 기준은 낮은 수이다.
그리고 도로의 수가 정해져있으므로 단순 MST를 넘어 더 추가해야된다.
이를 구현하기 위해 먼저 MST를 찾고 나머지 부족한 도로 부분을 순차 정렬된 부분에서 뽑기만하면된다.
"""
import sys
input = sys.stdin.readline

def find(u):
  if u != parent[u]:
    parent[u] = find(parent[u])
  return parent[u]

def union(u, v):
  u, v = find(u), find(v)

  if u > v:
    parent[u] = v
  else:
    parent[v] = u

def kruskal():
  global M
  cnt = 0
  answer = [0] * N

  for i in range(len(graph)):
    a, b = graph[i][0], graph[i][1]

    if find(a) != find(b):
      cnt += 1
      union(a, b)
      answer[a] += 1
      answer[b] += 1
    else:
      remain.append([a, b])

  if cnt == N-1:
    return answer
  else:
    return []

N, M = map(int, input().split())
graph = []
for i in range(N):
  temp = list(input().rstrip())
  for j in range(i+1, N):
    if temp[j] == 'Y':
      graph.append([i, j])

parent = [i for i in range(N)]
remain = []
result = kruskal()
if result:
  if len(remain) >= M-N+1:
    for i in range(M-N+1):
      a, b = remain[i][0], remain[i][1]
      result[a] += 1
      result[b] += 1
    print(*result)
  else:
    print(-1)
else:
  print(-1)