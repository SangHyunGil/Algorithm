import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())
    stack = []
    data = sorted([list(map(int, input().split())) for _ in range(n)])

    for x, d in data:
        if stack:
            if d+stack[-1][1] < abs(x-stack[-1][0]):
                pass
            
            elif abs(x-stack[-1][0]) < abs(d-stack[-1][1]):
                stack.pop()
                stack.append([x, d])

            else:
                return "NO"
                

        else:
            stack.append([x, d])


    return "YES"


print(solve())