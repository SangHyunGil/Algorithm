"""
DP의 대표적인 예제인 피보나치이다.
하지만 조금의 변형이 있다. 음수에 대해서도 구할 수 있어야한다는 점이다.
나는 처음에 단순 100만의 수이기에 음수, 양수 둘다 구해도 O(N)으로 구해도 충분하여
단순 양수, 음수 피보나치를 둘 다 구하는 방식으로 정답처리되었다.
하지만, 피보나치 음수의 경우 짝수의 경우에만 음수처리되고 똑같은 것을 확인할 수 있었다.
효율적으로 진행하기 위해 다음과 같이 바꾸어 진행했고 약 2배의 시간을 절약할 수 있었다.
"""

import sys
input = sys.stdin.readline

def isValid(i, j):
    if 0 <= i < N and 0 <= j < 3:
        return True
    else:
        return False

d = [[0, -1], [-1, -1], [-1, 0], [-1, 1]]
cnt = 1
while True:
    if (N:=int(input())) == 0:
        break
    graph = [[*map(int, input().split())] for _ in range(N)]
    DP = [[sys.maxsize] * 3 for _ in range(N)]
    DP[0][1] = graph[0][1]

    for i in range(N):
        for j in range(3):
            for dx, dy in d:
                ni, nj = i+dx, j+dy
                if isValid(ni, nj):
                    DP[i][j] = min(DP[i][j], DP[ni][nj]+graph[i][j])

    print(str(cnt)+". "+str(DP[N-1][1]))
    cnt += 1