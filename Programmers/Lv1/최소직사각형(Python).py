def solution(sizes):
    bigger, smaller = 0, 0
    for s1, s2 in sizes:
        # 큰 순으로 정렬
        if s1 < s2:
            s1, s2 = s2, s1
        
        # 대소비교
        bigger = max(bigger, s1)
        smaller = max(smaller, s2)
            
    return bigger*smaller