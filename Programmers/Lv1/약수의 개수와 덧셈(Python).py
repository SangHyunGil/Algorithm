def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        print(bin(a1 | a2).zfill(n))
    return answer