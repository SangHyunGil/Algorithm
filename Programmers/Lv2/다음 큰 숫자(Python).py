def solution(n):
    answer = 0

    for i in range(n+1):
        temp = i

        for j in range(i+1, n+1):
            temp += j
            if temp >= n:
                break
        
        if n == temp:
            print(i)
            answer += 1

    return answer