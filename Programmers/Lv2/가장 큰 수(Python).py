"""
이 문제의 핵심은 문자열의 정렬이다.
파이썬에서 문자열의 숫자를 정렬할 경우 문자열의 순서에 따라 정렬한다.
첫번째, 두번째, 세번째.. 이렇게 비교를 진행하는데
1000이하의 숫자이므로 최소한 3번째 자리까지 비교해야하므로 *3을 한 뒤 정렬을 수행하면된다.
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

