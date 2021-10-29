def solution(num):
    cnt = 0
    while num != 1 and cnt <= 500:
        if num % 2: # 홀수
            num = num*3+1     
        else: # 짝수
            num //= 2
        cnt += 1
    return cnt if cnt <= 500 else -1

print(solution(6))