import sys, time
from collections import defaultdict, deque
input = sys.stdin.readline

def inverse(a, b):
    graph[a][b] = 1
    graph[b][a] = 0
    indegree[b] += 1
    indegree[a] -= 1

def topology_sort():
    queue = deque([])
    visited = [0] * (n+1)
    answer = []
    for i in range(1, n+1):
        if not indegree[i]:
            queue.append(i)

    while queue:
        if len(queue) > 1:
            return "?"

        x = queue.popleft()
        answer.append(str(x))

        for i in range(1, n+1):
            if graph[x][i]:
                if not visited[i]:
                    indegree[i] -= 1

                    if indegree[i] == 0:
                        queue.append(i)
                
                else:
                    return "IMPOSSIBLE"

    return answer

for i in range(int(input())):
    n = int(input())
    graph = [[0] * (n+1) for _ in range(n+1)]
    indegree = [0] * (n+1)
    info = [0] + list(map(int, input().split()))
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            graph[info[i]][info[j]] = 1
            indegree[info[j]] += 1
    
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if graph[a][b]:
            inverse(b, a)
        else:
            inverse(a, b)
 
    answer = topology_sort()
    if answer == "?":
        print(answer)
    else:
        if len(answer) == n:
            print(" ".join(answer))
        else:
            print("IMPOSSIBLE")
    