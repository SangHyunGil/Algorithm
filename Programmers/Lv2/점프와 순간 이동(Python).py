"""
200 => 100
100 => 50
50 => 25
25 => 24 (ans += 1) 
24 => 12 
12 => 6
6 => 3
3 => 2 (ans += 1)
1 => 1 (ans += 1)
"""

def solution(n):
    ans = 0
    while n:
        ans += n % 2
        n //= 2
        
    return ans

print(solution(200))