import sys
from collections import deque
input = sys.stdin.readline

dp = [float(input().rstrip()) for _ in range(int(input()))]

for i in range(1, len(dp)):
    dp[i] = max(dp[i], dp[i-1]*dp[i])

print("{:.3f}".format(max(dp)))