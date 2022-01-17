"""
점수의 수가 10개이기에 충분히 브루트포스하게 접근가능하다.
backtracking을 통해 해당 경우를 모두 탐색하고 조건에 맞는 경우만 체크해준다.
조건이란 다음과 같다.
1. 모든 화살을 소진했는가
2. 이전까지의 최댓값보다 큰가
"""
import sys, copy

answer = -sys.maxsize
result = []
arrow = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def calculateScore(info):
    apeach, lion = 0, 0
    for idx, (a, l) in enumerate(zip(info, arrow)):
        if a == 0 and l == 0:
            continue
        
        score = (10-idx)
        if a < l:
            lion += score
        else:
            apeach += score
    
    return lion - apeach
            
def backtracking(info, n, cnt, idx):
    global answer, result, arrow
    if idx == 11:
        score = calculateScore(info)
        if n == cnt:
            if score > 0:
                if answer < score:
                    answer = score
                    result = []
                    result.append(copy.deepcopy(arrow))
                elif answer == score:
                    result.append(copy.deepcopy(arrow))
    else:
        for i in range(n-cnt+1):
            arrow[idx] = i
            backtracking(info, n, cnt+i, idx+1)
            arrow[idx] = 0
        
def solution(n, info):
    backtracking(info, n, 0, 0)
    result.sort(key = lambda x : [-x[i] for i in range(10, -1, -1)])
    return result[0] if result else [-1]