def isScore(c):
    return c.isdigit() or c == 'Z'

def isDart(c):
    return c in ['S', 'D', 'T']

def solution(dartResult):
    # 다트 영역
    dart = {'S' : 1, 'D' : 2, 'T' : 3}
    # 다트 상
    prize = {'*' : 2, '#' : -1}
    # 10을 Z로 대체
    dartResult = list(dartResult.replace("10", 'Z'))
    
    # 다트 점수 계산
    answer = []
    for d in dartResult:
        if isScore(d):
            answer.append(int(d) if d != 'Z' else 10)
        elif isDart(d):
            answer[-1] = answer[-1] ** dart[d]
        else:
            answer[-1] = answer[-1] * prize[d]
            if len(answer) > 1 and d == '*':
                answer[-2] = answer[-2] * prize[d]

    return sum(answer)