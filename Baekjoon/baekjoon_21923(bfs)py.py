"""
이 문제는 DP 문제로 해결해보았다.
DP로 해결하기 위해 점화식을 세웠다.
DP는 2차원 배열로 DP[X][Y]에서 X는 자리수, Y는 끝 자리수로 생각해보자.
그렇다면 DP[X-1][Y]는 
         DP[X][Y-1]는 X-1자리수에서 Y보다 작은수의 개수이다. ex) X->1 Y->2 => 11
"""

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
DP = [[1] * 10 for _ in range(N)]

for i in range(1, N):
    for j in range(10):
        if j == 0:
            DP[i][j] = 1
        else:
            DP[i][j] = (DP[i-1][j]+DP[i][j-1])%10007

print(sum(DP[N-1]))