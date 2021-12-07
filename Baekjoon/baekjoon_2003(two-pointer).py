import sys
input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split())]
dp = [1] * n
for i in range(n):
    temp = dp[i]
    for j in range(i):
        print(dp)
        if arr[j] < arr[i]:
            temp = max(temp, dp[i]+dp[j])
    dp[i] = temp

print(max(dp))