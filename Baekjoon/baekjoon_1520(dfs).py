"""
이 문제는 DFS로 풀어보았다.
단순히 경로를 찾는데 그에 대한 경우의 수를 저장해가면서 풀면 된다.
방문했다면 더 이상의 탐색을 멈추고 해당 부분의 값을 더해주면 된다.
스택으로 구현한 DFS가 아니라, 재귀로 구현한 DFS이기에 역으로 더해가기 때문에
visited[0][0]에 총 경우의 수가 저장될 것이기에 마지막에 결국 visited[0][0] 값이 출력되기에
dfs(0, 0) 값 자체를 출력하면 된다.
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [0]
for _ in range(N):
    graph += [*map(int, input().split())]

for i in range(1, N*N):
    graph[i] += graph[i-1]

print(graph)

for _ in range(M):
    N1, M1, N2, M2 = map(int, input().split())
    X = N * (N1 - 1) + M1 - 1; Y = N * (N2 - 1) + M
    print(X,Y)
    print(graph[Y]-graph[X])