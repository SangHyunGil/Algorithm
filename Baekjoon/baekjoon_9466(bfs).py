import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(i, path):
    global answer
    path.append(i)
    visited[i] = 1

    nxt = team[i]-1
    if visited[nxt]:
        if nxt in path:
            answer += len(path[path.index(nxt):])
        return
    else:
        dfs(nxt, path) 

for _ in range(int(input())):
    answer = 0     
    n = int(input())
    visited = [0] * n
    graph = [[] for _ in range(n)]
    team = list(map(int, input().split()))

    for i in range(n):
        if not visited[i]:
            dfs(i, [])

    print(n-answer)