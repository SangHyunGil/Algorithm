def solution(board, moves):
    answer = 0
    pick = []

    for m in moves:
        # 인형 뽑기(아래로)
        for i in range(len(board)):
            if board[i][m-1]:
                # 같은 인형일시 점수 UP
                if pick and pick[-1] == board[i][m-1]:
                    pick.pop()
                    answer += 2
                # 아닐시 단순 추가
                else:
                    pick.append(board[i][m-1])

                board[i][m-1] = 0
                break

    return answer
