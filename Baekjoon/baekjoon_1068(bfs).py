"""
루트 노트가 0에서 시작한다는 점을 간과하면 안된다.
그리고 꼭 이진 트리가 아니라는 점을 주의하자.
이 부분 때문에 시간을 좀 잡아먹었다.
이런 부분을 제외하고 단순 bfs로 탐색하여 삭제 노드를 제외하고 리프노드를 탐색하면 된다.
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(t):
    cnt = 0
    queue = deque([t])
    while queue:
        x = queue.popleft()

        child = 0
        for nx in graph[x]:
            if nx != m:
                child += 1
                queue.append(nx)

        if not child:
            cnt += 1

    return cnt

n = int(input())
tree = list(map(int, input().split()))
m = int(input())

start = 0
graph = [[] for _ in range(n)]
for idx, t in enumerate(tree):
    if t != -1:
        graph[t].append(idx)
    else:
        start = idx

if start == m:    
    print(0)
else:
    print(bfs(start))