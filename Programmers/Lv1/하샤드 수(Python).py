def solution(x):
    # 자릿수 합
    div = sum(map(int, list(str(x))))
    return x % div == 0