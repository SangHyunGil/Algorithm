"""
이 문제는 bfs를 통해 영역의 넓이를 찾는 문제 중 하나이다.
하지만 조금 다른 점이 접근이 불가능한 한 부분에 대해 접근을 가능하게 하여 최대 넓이를 찾는 문제이다.
이러한 부분에 있어 처음에는 접근이 불가능한 점에 대해 모두 bfs를 진행했는데
이렇게 진행한다면 visited를 처리하지 못해 단순 간선의 개수만큼의 복잡도를 가져야하지만
간선의 개수의 제곱만큼의 복잡도를 가져 O((NM)^2)의 복잡도를 가져 실패한다.
그래서 다른 방법으로 모든 영역의 넓이를 찾고 각 넓이를 차지하는 영역들에 번호를 매겨
불가능한 점을 기준으로 4방향을 겹치지 않게 넓이를 더해 처리하는 방식을 생각했다.
"""
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dic = {"S" : 0, "R" : 3, "L" : 1}

def calculate(k, i, j, grid, visited):
    cnt = 1
    queue = deque([[k, i, j]])
    visited[k][i][j] = 1

    while queue:
        d, x, y = queue.popleft()
        nd = (d + dic[grid[x][y]]) % 4
        nx, ny = (x+dx[nd])%len(grid), (y+dy[nd])%len(grid[0])

        if not visited[nd][nx][ny]:
            cnt += 1
            visited[nd][nx][ny] = 1
            queue.append([nd, nx, ny])

    return cnt

def solution(grid):
    answer = []
    visited = [[[0] * len(grid[0]) for i in range(len(grid))] for _ in range(4)]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for k in range(4):                
                if not visited[k][x][y]:
                    answer.append(calculate(k, x, y, grid, visited))

    return sorted(answer)   

print(solution(["R"]))