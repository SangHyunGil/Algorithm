from collections import deque
from copy import deepcopy

def init(info, edges):
    graph = [[] for _ in range(len(info))]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        
    return graph

def solve(info, graph):
    answer = 1
    stack = [[0, set([0]), set(), 0, 0]]
    visited = [[[0] * 200 for _ in range(200)] for _ in range(17)]    
    visited[0][1][0] = 1

    while stack:
        x, sheeps, wolves, ssum, wsum = stack.pop()
        answer = max(answer, len(sheeps))
           
        for nx in graph[x]:
            nsheeps, nwolves = deepcopy(sheeps), deepcopy(wolves)
            nssum, nwsum = ssum, wsum
            if info[nx]:
                if nx not in nwolves:
                    nwsum += nx
                    nwolves.add(nx)
            else:
                if nx not in nsheeps:
                    nssum += nx
                    nsheeps.add(nx)

            if len(nsheeps) > len(nwolves) and not visited[nx][len(sheeps)+nssum][len(wolves)+nwsum]:
                visited[nx][len(sheeps)+nssum][len(wolves)+nwsum] = 1
                stack.append([nx, nsheeps, nwolves, nssum, nwsum])
    
    return answer
        
def solution(info, edges):
    answer = 0
    graph = init(info, edges)
    
    return solve(info, graph)