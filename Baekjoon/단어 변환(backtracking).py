from collections import deque

def init(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    for x, y in puddles:
        board[x-1][y-1] = 1

    return board

def isValid(i, j, m, n):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def bfs(m, n, board):
    queue = deque([[0, 0]])
    board[0][0] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            return board[x][y]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if isValid(nx, ny) and not board[nx][ny]:
                board[nx][ny] += board[x][y]
                queue.append([nx, ny])


def solution(m, n, puddles):
    board = init(m, n, puddles)
    return bfs(m, n, board)