"""
이 문제는 DP 문제로 해결해보았다.
DP로 해결하기 위해 점화식을 세웠다.
DP는 2차원 배열로 DP[X][Y]에서 X는 자리수, Y는 끝 자리수로 생각해보자.
그렇다면 DP[X-1][Y]는 X-1자리수에서 Y와 끝자리가 같은 수의 개수이다. ex) X->1 Y-> 2 22
         DP[X][Y-1]는 X-1자리수에서 Y보다 작은수의 개수이다. ex) X->1 Y->2 => 12
이 둘을 합하면 해당 끝자리의 개수가 나오고 해당 자리수의 총 합을 구하면 정답이 된다.
여기서 주의할점은 SUM을 한 뒤의 값 또한 "10007을 넘을 수 있으므로" 나머지 처리해주어야한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
coin = [int(input()) for _ in range(N)]
DP = [0] * (M+1)

for i in range(M+1):
    if not i % coin[0]:
        DP[i] = 1

for i in range(1, N):
    for j in range(M+1):
        if j-coin[i] >= 0:
            DP[j] += DP[j-coin[i]]

print(DP[M])