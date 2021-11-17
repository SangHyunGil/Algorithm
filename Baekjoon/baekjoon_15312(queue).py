import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dp = [[0, 1]]
for i in range(1, N):
    dp.append([dp[i-1][1], dp[i-1][0]+dp[i-1][1]])

print(dp[N-1][0], dp[N-1][1])

