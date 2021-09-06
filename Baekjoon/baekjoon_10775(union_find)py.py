import sys, time
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def find(u):
    if u != parent[u]: parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u = find(u)
    v = find(v)

    if u > v:
        parent[u] = v
    else:
        parent[v] = u

answer = 0
G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
rank = [0 for i in range(G+1)]
closed = False
for _ in range(P):
    g = int(input())
    g_parent = find(g)
    if not g_parent: 
        closed = True

    if not closed:
        union(g_parent, g_parent-1)
        answer += 1

print(answer)