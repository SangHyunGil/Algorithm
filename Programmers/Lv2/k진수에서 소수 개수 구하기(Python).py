"""
간단히 생각하면 된다.
1. N진수로 바꾼다.
2. 0을 기준으로 자른다.
3. 소수인지 확인한다.
"""
from math import sqrt

def makeNth(n, k):
    s = ""
    while n > 0:
        s += str(n%k)
        n //= k
    return s[::-1]
    
def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True
    
def solution(n, k):
    answer = 0
    n = makeNth(n, k)
    n = n.split('0')
            
    for k in n:
        if k and isPrime(int(k)):
            answer += 1

    return answer