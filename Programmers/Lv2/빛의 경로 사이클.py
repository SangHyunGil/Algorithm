"""
bfs로 접근하여 문제를 풀었다.
이 문제는 방향에 따라 다른 케이스가 되기 때문에 visited 자체를 2차원 배열이 아닌
3차원 배열로 바꾸어 진행한다.
처음에 실수했던 부분은 단순 사이클을 구하는데 있어 0, 0 부분만 확인하면 되는줄 알았지만
0, 0만으로는 모든 사이클을 확인할 수 없고 전체 좌표들을 확인해야한다는 사실을 확인하여
이를 진행하니 통과되었다.
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