def solution(arr):
    answer = [arr[0]]

    # 중복 처리 
    for a in arr[1:]:
        if a != answer[-1]:
            answer.append(a)

    return answer