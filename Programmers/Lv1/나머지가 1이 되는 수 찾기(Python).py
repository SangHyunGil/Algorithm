def solution(n):
    answer = 0
    # 브루트 포스로 탐색
    for i in range(1, n):
        answer = i
        if n % i == 1:
            break

    return answer

solution(11)