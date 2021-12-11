"""
전형적인 DP이다.
여기서 많이 간과한 부분이 존재했는데, 단순 위에서 올 수 있는 것이 아니라 왼쪽에서도 올 수 있다.
올수 있는 방향은 왼쪽, 왼쪽 상단, 상단, 오른쪽 상단이다.
하지만, 범위가 맞는지 확인해줘야 하기에 이 부분에 대한 메소드를 하나 구성하였다.
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