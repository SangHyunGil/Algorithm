"""
행렬을 통해 그래프를 추출한다.
그래프를 bfs로 탐색하면서 이어져있는 네트워크들을 확인한다.
네트워크의 개수를 더해 리턴한다.
"""

from collections import deque

def bfs(graph, visited, i):
    queue = deque([i])
    
    while queue:
        x = queue.popleft()
        
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = 1
                queue.append(nx)
    
    return 1
    
def solution(n, computers):
    answer = 0
    
    graph = [[] for _ in range(n)]
    visited = [0] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                graph[i].append(j)
                
    for i in range(n):
        if not visited[i]:
            answer += bfs(graph, visited, i)
            
    return answer