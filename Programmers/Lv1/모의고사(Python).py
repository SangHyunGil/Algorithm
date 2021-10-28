def solution(answers):
    answer = []
    # 각 방식의 획득 점수
    score = [0, 0, 0]
    # 각 방식의 패턴
    method_1 = [1, 2, 3, 4, 5]
    method_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    method_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 방식의 점수 계산
    for idx, ans in enumerate(answers):
        score[0] += 1 if method_1[idx%5] == ans else 0
        score[1] += 1 if method_2[idx%8] == ans else 0
        score[2] += 1 if method_3[idx%10] == ans else 0

    # 각 방식의 최대 점수 계산
    mx = max(score)
    for idx, value in enumerate(score):
        if mx == value:
            answer.append(idx+1)
            
    return sorted(answer)