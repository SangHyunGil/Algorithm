"""
이 문제는 생각의 전환만 한다면 정말 간단하다.
행과 열의 길이가 각각 30밖에 되지 않아 브루트 포스로 충분히 가능하다.

단순히 터트려야할 프렌즈를 찾으려면 우측, 하단, 우측 하단을 확인해 자신과 같다면 터트린다.
그리고, 겹쳐있는 부분이 존재할 수 있으므로 집합에 추가한다.

하지만 터뜨리는 로직을 어떻게 구성해야할까?
터지는 부분들이 한 열에 여러 개가 있을 수 있고 그것들은 떨어져있을 수 있고 붙어 있을 수도 있다.
어떻게 효율적으로 해당 부분을 처리할까?
바로 행과 열을 바꾸는 것이다.
행과 열을 바꿔 터진 부분들을 싹 없애고 나머지 부분만 살린뒤 맨 왼쪽의 행의 크기만큼 터진 개수를 추가해준다.
그러면 터진 것이랑 다름이 없다.
해당 부분을 구현하면 다음과 같다.
"""

answer = 0

def canPop(i, j, board):
    block = board[i][j]
    if block == board[i+1][j] and block == board[i][j+1] \
        and block == board[i+1][j+1]:
        return True
    else:
        return False

def getPopBlocks(n, m, board):
    popList = set()
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j] != '-' and canPop(i, j, board):
                popList.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)})
    
    return popList

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
        popList = getPopBlocks(n, m, board)
        if popList:
            popBlocks(n, m, board, popList)
        else:
            return answer

def solution(m, n, board):
    board = list(map(list, zip(*[list(b) for b in board])))
    return solve(m, n, board)
