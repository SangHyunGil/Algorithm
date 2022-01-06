"""
크루스칼 알고리즘을 활용해 풀었다.
기존과 다르게 MST를 반복적으로 만든다는 점이다.
MST를 K번 만큼 만드는데 최소 간선을 지워가면서 만든다는 것이다.
단순히 pop하고 반복하면되고 전체 그래프가 이어지지 않는 순간 종료하고 나머지를 0으로
출력하면 된다.
"""
import sys, copy
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

def kruskal(e, graph):
    answer, cnt = 0, 0
    ngraph = copy.deepcopy(graph)
    while ngraph:
        c, u, v = ngraph.pop()
        if find(u) != find(v):
            union(u, v)
            cnt += 1
            answer += c        

        if cnt == e-1:
            return answer

N, M, K = map(int, input().split())
graph = []

for i in range(M):
    a, b = map(int, input().split())
    graph.append([i+1, a-1, b-1])
graph.sort(reverse=True)

ans = [0] * K
for i in range(K):
    parent = [i for i in range(N)]
    if not (temp:=kruskal(N, graph)):
        break
    ans[i] = temp
    graph.pop()

print(*ans)