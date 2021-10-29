def solution(arr1, arr2):
    answer = [[0] * len(arr1) for _ in range(arr1)]
    for i, a1, a2 in enumerate(zip(arr1, arr2)):
        for j, a, b in enumerate(zip(a1, a2)):
            answer[i][j] = a+b
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))