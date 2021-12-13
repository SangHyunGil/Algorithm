"""
dp 문제로 해결해보았다.
첫자리가 0이라면 애초에 되지 않는 경우이다.
그리고 앞의 수를 포함했을때 26 이하라면 2자리로 사용가능한 경우이고
아니라면 1자리로만 사용이 가능한 경우이다.
1자리로만 사용이 가능하다면 DP[i-1]
2자리로 사용이 가능하다면 DP[i-1] + DP[i-2]가 될 것이다.
이를 이용해 구하면 된다.
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