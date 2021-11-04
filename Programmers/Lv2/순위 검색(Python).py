answer = 0

def getPopBlocks(i, j, board):
    block = board[i][j]
    if block == board[i+1][j] and block == board[i][j+1] \
        and block == board[i+1][j+1]:
        return [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]
    
    return []

def popBlocks(n, m, board, popList):
    global answer
    for i, j in popList:
        answer += 1
        board[i][j] = 'X'
    
    for i in range(n):
        board[i] = list("".join(board[i]).replace("X", "").rjust(m, '-'))
        
def solve(m, n, board):
    global answer
    while True:
        popList = set()
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] != '-':
                    blocks = getPopBlocks(i, j, board)
                    for block in blocks:
                        popList.add(block)
        print(popList)
        if popList:
            popBlocks(n, m, board, popList)
        else:
            return answer

    
def solution(m, n, board):
    board = list(map(list, zip(*[list(b) for b in board])))
    return solve(m, n, board)

solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])