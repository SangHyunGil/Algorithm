import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

T = [*map(int, input().split())]
DP = [1 for _ in range(N)]
ROUTE = dict()

for i in range(1, N):
    for j in range(i):
        if T[j] < T[i] and DP[j]+1 > DP[i]:
            DP[i] = DP[j]+1
            ROUTE[i] = j

MAX = [0, 0]
for idx, v in enumerate(range(N)):
    if MAX[0] < DP[v]:
        MAX = [DP[v], idx]

ANS = deque([T[MAX[1]]])
idx = MAX[1]

while idx in ROUTE:
    idx = ROUTE[idx]
    ANS.appendleft(T[idx])
    
print(MAX[0])
print(*ANS)