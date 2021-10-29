def solution(N, stages):
    answer = []
    # 스테이지별 멤버수 계산
    member = [0 for _ in range(N)]
    for stage in stages:
        if stage-1 < N:
            member[stage-1] += 1
    
    # 스테이지별 실패율 계산
    total = len(stages)
    for level, m in enumerate(member):
        if total:
            answer.append([m/total, level+1])
            total -= m
        else:
            answer.append([0, level+1])
    
    # 순위별 정렬(실패율 내림차순, 스테이지 오름차순)
    answer.sort(key=lambda x : (-x[0], x[1]))
    return [ans[1] for ans in answer]

print(solution(5, [1,1,1,1]))