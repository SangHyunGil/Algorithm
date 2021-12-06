import sys, copy
from collections import deque
input = sys.stdin.readline

n = int(input())
temp = [int(input()) for _ in range(int(input()))] + [n+1]
m = [temp[0]]

for i in range(1, len(temp)):
    m.append(temp[i]-temp[i-1])
dp = [1, 1, 2]

for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-2])

ans = 1
for i in m:
    ans *= dp[i-1]
print(ans)