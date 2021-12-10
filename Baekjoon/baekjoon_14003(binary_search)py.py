import sys
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
T = [*map(int, input().split())]
DP = [-sys.maxsize]
TRACE = [0] * N

for i in range(N):
    if DP[-1] < T[i]:
        DP.append(T[i])
        TRACE[i] = len(DP)-1
    else:
        idx = bisect_left(DP, T[i])
        DP[idx] = T[i]
        TRACE[i] = idx

ANS = deque([])
length = len(DP)-1
for i in range(N-1, -1, -1):
    if TRACE[i] == length:
        ANS.appendleft(T[i])
        length -= 1

print(len(DP)-1)
print(*ANS)