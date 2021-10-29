def solution(num):
    cnt = 0
    while num != 1 and cnt <= 500:
        if num % 2:
            num = num*3+1     
        else:
            num //= 2
        print(num)
        cnt += 1
    return cnt if cnt <= 500 else -1

print(solution(6))