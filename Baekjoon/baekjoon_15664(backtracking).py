import sys
input = sys.stdin.readline

def backtracking(t, idx):
  if len(t) == m:
    answer.add(t)
    return
  
  for i in range(idx, n):
    if not visited[i]:
      visited[i] = 1
      backtracking(t + (arr[i],), i+1)
      visited[i] = 0

answer = set()
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * n
backtracking(tuple(), 0)
for ans in sorted(answer):
  print(*ans)