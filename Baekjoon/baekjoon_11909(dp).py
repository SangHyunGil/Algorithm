"""
생각보다 시간이 빡빡한 문제였다.
처음에는 단순히 다익스트라로 접근했다.
다익스트라로 접근했을 때 시간초과가 발생했다.
그 원인을 확인하기 위해 시간복잡도를 확인해보려고 했다.
간선의 개수는 2222*2222*2이며 정점의 개수는 2222*2222이다.
다익스트라의 시간복잡도는 간선 * log(정점)인데 이를 계산하면 약 2억이 나와
사실상 2초안에 해결이 어렵다.
그래서 DP로 접근했다.
DP로 이전의 값을 유지하면서 최소값을 찾아가는 것을 구현했는데 Python3에서는 시간초과가나고
Pypy3에서는 1초의 시간이 걸린걸로 보아 생각보다 시간이 빡빡했다.
"""

import sys
input = sys.stdin.readline

def cal(i, j, x, y):
    return graph[i][j] - graph[i-x][j-y] + 1 if graph[i-x][j-y] <= graph[i][j] else 0

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[sys.maxsize] * N for _ in range(N)]
dp[0][0] = 0
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1] + cal(i, j, 0, 1))
        elif j == 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + cal(i, j, 1, 0))
        else:
            left = dp[i][j-1] + cal(i, j, 0, 1)
            up = dp[i-1][j] + cal(i, j, 1, 0)
            dp[i][j] = min(dp[i][j], left, up)

print(dp[N-1][N-1])