"""
간단한 최대공배수 문제이다.
gcd를 통한 최대공약수로 두 수를 곱한 수를 나눠주면 최대공배수가 된다.
여러 개가 존재할 경우 연쇄적으로 구하면 그게 답이 된다.
"""

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)

def solution(arr):

    answer = arr[0]
    for a in arr[1:]:
        answer = answer*a // gcd(answer, a)
    return answer