import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
dp = [1, 1, 2]

for i in range(3, N):
    temp = 0
    for j in range(0, i//2):
        print(i, j)
        temp += (dp[j] * dp[i-j-1]) * 2
    if i%2:
        temp += dp[i//2]*dp[i//2]
    dp.append(temp)
    print(dp)

print(dp[-1])
