import sys
input = sys.stdin.readline

N = int(input())
dp = [[], [1], [1, 2], [1, 3]]

for i in range(4, N+1):

    dp.append(dp[i-1]+[i])

    if not i % 2 and len(dp[i]) > len(dp[i//2])+1:
        dp[i] = dp[i//2]+[i]

    if not i % 3 and len(dp[i]) > len(dp[i//3])+1:
        dp[i] = dp[i//3]+[i]

print(len(dp[N])-1)
print(*dp[N][::-1])