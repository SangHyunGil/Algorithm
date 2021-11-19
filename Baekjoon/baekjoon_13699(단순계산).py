import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
dp = [1, 1, 2]

for i in range(3, N+1):
    temp = 0
    for j in range(i):
        temp += dp[j] * dp[i-j-1]

    dp.append(temp)

print(dp[N])