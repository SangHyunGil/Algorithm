def solution(arr1, arr2):
    # list comprehension을 활용한 행렬 덧셈
    answer = [[a+b for a, b in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]
    return answer