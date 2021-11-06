def isSquare(board, i, j):
    if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j]\
        and board[i][j] == board[i+1][j+1]:
        return True
    else:
        return False

def solution(board):
    answer = 0
    n = len(board); m = len(board[0])

    dp = [[0] * m for _ in range(n)]
    for i in range(n-1):
        for j in range(m-1):
            if isSquare(board, i, j):
                dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1])

    print(dp[n-1][m-1])
    return answer