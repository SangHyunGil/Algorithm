import math

def solution(progresses, speeds):
    answer = []
    
    day = 0
    for progress, speed in zip(progresses, speeds):
        # 작업 시간
        work = math.ceil((100-progress) / speed)

        # 이전에 작업이 끝나는지
        if answer and day >= work:
            answer[-1] += 1
        else:
            answer.append(1)
            day = work

    return answer