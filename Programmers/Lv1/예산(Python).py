def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    # 예산 계산
    while d and budget-d[-1] >= 0:
        budget -= d.pop()
        answer += 1
        
    return answer