def solution(N, stages):
    answer = []
    member = [0 for _ in range(N)]
    for stage in stages:
        if stage-1 < N:
            member[stage-1] += 1
    
    total = len(stages)
    for level, m in enumerate(member):
        print(m, total)
        answer.append([m/total, level+1])
        total -= m
    
    answer.sort(key=lambda x : (-x[0], x[1]))
    return [ans[1] for ans in answer]

print(solution(5, [1,1,1,1]))