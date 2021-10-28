def solution(n, lost, reserve):
    # 자기 자신이 옷을 입어야 하는 경우
    new_lost = (set(lost) - set(reserve))
    new_reserve = (set(reserve) - set(lost))
    
    # 여분 옷을 앞부터 빌림
    for res in new_reserve:
        if res-1 in new_lost:
            new_lost.remove(res-1)
            
        elif res+1 in new_lost:
            new_lost.remove(res+1)

    return n - len(new_lost)