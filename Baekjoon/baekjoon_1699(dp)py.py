import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
for i in range(1, N+1):
  dp[i] = i
#logic
for i in range(2, N+1):
  for j in range(1,  int((i**(1/2)))+1):
    if dp[i] > dp[i - j*j] + 1:
      dp[i] = dp[i - j*j] + 1
print(dp[N]) 