import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
T = [*map(int, input().split())]
DP = [-sys.maxsize]

for i in range(N):
    if DP[-1] < T[i]:
        DP.append(T[i])

    else:
        idx = bisect_left(DP, T[i])
        DP[idx] = T[i]

print(len(DP)-1)

