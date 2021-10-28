def solution(array, commands):
    answer = []

    for i, j, k in commands:
        # 정렬 후 slice
        arr = sorted(array[i-1:j])
        # 선택 후 추가
        answer.append(arr[k-1])

    return answer