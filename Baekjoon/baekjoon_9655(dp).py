"""
1 -> CY, 2 -> SK, 3 -> CY, 4 -> SK
결국 1, 3개씩 나눠주는 거면 다시 4개가 되면 원점이기에 
단순 그 전의 경우의 수만 따지면 된다.
"""

import sys
arr = list(map(int, input()))
dp = [0 for _ in range(len(arr)+1)]
if (arr[0] == 0) :
    print("0")
else :
    arr = [0] + arr
    dp[0]=dp[1]=1
    for i in range(2, len(arr)):
        if arr[i] > 0:
            dp[i] += dp[i-1]
        temp = arr[i-1] * 10 + arr[i]
        if temp >= 10 and temp <= 26 :
            dp[i] += dp[i-2]
    print(dp[len(arr)-1] % 1000000)