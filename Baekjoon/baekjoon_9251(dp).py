"""
LIS와 마찬가지로 DP의 전형적인 문제 중 하나이다.
LCS 중 에서도 Substring, Subsequence가 존재하는데, 이번 문제는 후자에 속한다.
즉, "떨어져있어도" 부분적으로 겹치면 된다.
Subsequence와 차이점은 DP의 점화식에서 갈린다.
Substring의 경우 겹치지 않는 경우, 이전 경우에서의 최대값을 받아와서 저장하지만
Subsequence의 경우 겹치지 않는 경우 버려 버린다.(0으로)
이 부분을 점화식으로 구하면
겹치는 부분에 대한 경우 DP[i][j] = DP[i-1][j-1]
겹치지 않는 부분에 대한 경우 DP[i][j] = max(DP[i-1][j], DP[i][j-1])
으로 나뉜다.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
DP = [[*map(int, list(input().rstrip()))] for _ in range(N)]

for i in range(1, N):
    for j in range(1, M):
        if DP[i][j]:
            DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1])+1

for d in DP:
    print(d)
print(max(map(max, DP))**2)