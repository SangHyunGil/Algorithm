"""
전형적인 피보나치 문제이다.
DP를 통해 해결하였다.
"""

def fibonacci(n):
    fib = [0, 1, 1]
    for i in range(3, n+1):
        fib += [(fib[i-2]+fib[i-1]) % 1234567]
    
    return fib[n] 

def solution(n):
    return fibonacci(n)