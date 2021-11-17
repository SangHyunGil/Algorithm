"""
간단한 규칙을 찾는 문제이다.
left, right 둘을 이용해 몫과 나머지를 구하고 1을 더한 값의 최댓값을 구하면 된다.
"""

def solution(n, left, right):
    return [max(i//n, i%n)+1 for i in range(left, right+1)]