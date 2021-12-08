import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
T = [[0, 0]] + [[*map(int, input().split())] for _ in range(N)]
dp = [0] * (N+2)

for i in range(N, -1, -1):
    if i+T[i][0] > N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+T[i][0]]+T[i][1])

print(max(dp))