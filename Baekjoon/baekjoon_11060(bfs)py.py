import sys
from collections import deque
input = sys.stdin.readline

dp = [[0, 0, 0] for _ in range(100001)]
dp[0] = [1, 0, 0]
dp[1] = [0, 1, 0]
dp[2] = [1, 1, 1]

for i in range(3, 100001):
    for j in range(3):
        for k in range(3):
            if k != j:
                dp[i][j] += dp[i-j-1][k]
        dp[i][j] %= 1000000009

for i in range(int(input())):
    n = int(input())
    print(sum(dp[n-1]) % 1000000009)