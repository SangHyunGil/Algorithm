def solution(board, moves):
    answer = 0

    pick = []
    board = list(map(list, zip(*board)))
    print(board)
    for m in moves:
        print(pick)
        for i in range(len(board)):
            if board[m-1][i]:
                if pick and pick[-1] == board[m-1][i]:
                    pick.pop()
                    answer += 2
                else:
                    pick.append(board[m-1][i])
                board[m-1][i] = 0
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))