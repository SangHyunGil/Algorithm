"""
이 문제에 대해 bfs로 접근하였다.
이 문제는 아래로 순차적으로 내려가며 점수를 계속 누적해주면 되는 문제이다.
처음에 단순 각각의 점수에 대해 bfs를 타며 전달해주었는데 이 부분을 간과했다.
N과 M은 100,000의 범위를 지니고 있다.
M이 칭찬의 개수인데 100,000만번의 최악에 for문을 돈다고 가정하고
N이 10만일 때, 순차적으로 -1, 1, 2, 3, 4 ... 이어져있는 구조라고 생각한다면
bfs 또한 간선의 개수만큼 즉 100,000만번을 돌게 된다.
그렇다면 O(100,000 * 100,000)의 복잡도를 지니게 되는데 이는 절대 2초안에 들어올 수 없다.
이를 달리 생각해보자.
단순히 누적합을 해야하는 "시작 부분"에만 점수를 기입하고 최종적으로 
마지막에만 누적을 진행하면 된다는 것이다.
이를 구현하면 다음과 같다.
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    queue = deque([n])

    while queue:
        x = queue.popleft()

        for nx in graph[x]:
            if nx != -1:
                ans[nx] += ans[x]
                queue.append(nx)

N, M = map(int, input().split())
ans = [0] * N
employee = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for i in range(N):
    if employee[i] != -1:
        graph[employee[i]-1].append(i)

for _ in range(M):
    a, b = map(int, input().split())
    ans[a-1] += b

bfs(employee.index(-1))
print(*ans)